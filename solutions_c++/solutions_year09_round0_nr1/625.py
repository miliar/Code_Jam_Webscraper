#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#define fori(N) for(int i=0; i<N; i++)
#define forj(N) for(int j=0; j<N; j++)

using namespace std;

int l,d,n,k, tstl;
string tst;
vector<string> dict;

bool works(string test, string search){
    int sl = search.length();
    int b = 0;
    fori(sl){
        if(test[b] == '('){
            bool match = false;
            b++;
            while(test[b] != ')'){
                if(test[b] == search[i]) match = true;
                b++;
            }
            if(!match) return false;
            b++;
        }
        else{
            if(test[b++] != search[i]) return false;
        }
    }
}

int main(){
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    fin >> l >> d >> n;
    dict.resize(d);
    
    //Read dictionary
    string line;
    getline(fin,line);
    fori(d){
        getline(fin, dict[i]);
    }
    //Process
    fori(n){
        k=0;
        getline(fin, tst);
        tstl = tst.length();
        forj(d){
            if(works(tst,dict[j])) k++;
        }
        fout << "Case #" << i+1 << ": " << k << endl;
    }
    cout << "done";
    cin.get();
    return 0;   
}
