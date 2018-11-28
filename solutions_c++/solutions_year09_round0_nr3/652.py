#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#define fori(N) for(int i=0; i<N; i++)
#define forj(N) for(int j=0; j<N; j++)

using namespace std;

int n,k,cl;
long pos[20][502];

int main(){
    ifstream fin("C-large.in");
    ofstream fout("C-large.out");
    string curr;
    string cmp = "welcome to code jam"; //19 characters
    fin >> n;
    getline(fin, curr);
    
    for(int Z=0; Z<n; Z++){
        getline(fin, curr);
        if(curr.find('w') == string::npos) fout << "Case #" << Z+1 << ": 0000" << endl;
        else{
            string t = curr.substr(curr.find('w'));
            cl = t.length()+1;
            
            fori(20){
                forj(cl) pos[i][j] = 0;
            }
            int w=0;
            fori(cl-1){
                if(t[i] == 'w') w++;
                pos[1][i] = w;
            }
            
            for(int i=2; i<20; i++){
                //fout << pos[i][1] << "\t";
                for(int j=2; j<cl; j++){
                    if(t[j-1] == cmp[i-1]) pos[i][j] = pos[i][j-1]+pos[i-1][j-1];
                    else pos[i][j] = pos[i][j-1];
                    if(pos[i][j] > 10000) pos[i][j] -= 10000;
                    //fout << pos[i][j] << "\t";
                }
                //fout << endl;
            }
            //fout << "-----" << endl;
            char ans[5];
            sprintf(ans, "%.4d", pos[19][cl-1]%10000);
            fout << "Case #" << Z+1 << ": " << ans << endl;
        }
        cout << "boo";
    }   
    
    cin.get();
    return 0;   
}
