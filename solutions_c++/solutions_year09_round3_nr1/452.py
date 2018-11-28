#include <iostream>
#include <fstream>
#include <cstdlib>
#include <sstream>

#include <algorithm>
#include <vector>
#include <string>
#define fori(N) for(int i=0; i<N; i++)
#define forj(N) for(int j=0; j<N; j++)

using namespace std;

long power(long a, long b){
    long ans = 1;
    fori(b) ans *= a;
    return ans;
}

int getBase(string s){
    string tmp = s;
    int ret = 0;
    fori(s.length()){
        if(s[i] == '*') continue;
        else{
             ret++;
             for(int j=i+1; j<s.length(); j++){
                    if(s[j] == s[i]) s[j] = '*';
            }
            s[i] ='*';
        }
    }
    if(ret == 1) return 2;
    return ret;
    
}

int main(){
    ifstream fin("A-small-attempt1.in");
    ofstream fout("A-small.out");
    
    int n;
    char one,zero;
    string line;
    fin >> n;
    getline(fin, line);
    for(int Z=0; Z<n; Z++){
        cout << Z << endl;
        int d=2, k = 0;
        getline(fin, line);
        one = line[0];
        for(k=0; k<line.length() && line[k] == one; k++); 
        zero= line[k];
        int b = getBase(line);
        //do 1
        long ans = 0;
        fori(line.length()){
            if(line[i] == one){
                 ans += power(b, line.length()-i-1);
                 line[i] = '*';
            }
            else if(line[i] == zero)  line[i] = '*';
        }
        //cout << zero << " " << one << endl;
        for(int a=2; a<line.length(); a++){
            //cout << line << " " << ans << endl;
            if(line[a] == '*') continue;
            for(int c=a+1; c<line.length(); c++){
                if(line[c] == line[a]){
                    ans += d*power(b, line.length()-c-1);
                    line[c] = '*';
                }
            }
            ans += d*power(b, line.length()-a-1);
            //cout << d << "*" << b <<"^" << line.length()-a-1 << endl;
            line[a] = '*';
            d++;
        }
        fout << "Case #" << Z+1 <<": " << ans << endl;
    }
     
    return 0;   
}
