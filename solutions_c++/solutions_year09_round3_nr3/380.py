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

int main(){
    ifstream fin("C-small-attempt.in");
    ofstream fout("C-small.out");
    
    int n;
    fin >> n;
    for(int Z=0; Z<n; Z++){
        int p, q, min = 99999999;
        fin >> p >> q;
        int release[q];
        fori(q){
             fin >> release[i];
            release[i]--;
        }
        sort(release, release+q);
        fori(q) cout << release[i] << " ";
            cout << endl;
            bool in[p];
            int coin[p];
            int tot = 0;
            fori(p){
                 in[i] = true;
                 coin[i] = 0;
            }
            fori(q){
                in[release[i]] = false;
                for(int j=release[i]+1;j<p;j++){
                    if(!in[j]) break;
                    coin[j]++;
                }
                for(int j=release[i]-1;j>=0;j--){
                    if(!in[j]) break;
                    coin[j]++;
                }
            }
            fori(p) tot += coin[i];
            if(tot < min) min = tot;
        while(next_permutation(release, release+q)){
            fori(q) cout << release[i] << " ";
            cout << endl;
            bool in[p];
            int coin[p];
            int tot = 0;
            fori(p){
                 in[i] = true;
                 coin[i] = 0;
            }
            fori(q){
                in[release[i]] = false;
                for(int j=release[i]+1;j<p;j++){
                    if(!in[j]) break;
                    coin[j]++;
                }
                for(int j=release[i]-1;j>=0;j--){
                    if(!in[j]) break;
                    coin[j]++;
                }/*
                fori(p){
                    //if(in[i]) cout << "1";
                    //else cout << "0";
                    cout << coin[i];
                    cout << " ";
                }
                cout << endl;*/
            }
            fori(p) tot += coin[i];
            if(tot < min) min = tot;
        }
        
        fout << "Case #" << Z+1 <<": " << min<< endl;
    }
     cin.get();
    return 0;   
}
