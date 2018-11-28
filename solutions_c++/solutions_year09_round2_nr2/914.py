//Made by: Albert Villalobos

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;

int main(){
    ifstream fin("B-Large.in");
    ofstream fout("B-Large.out");
    int n;
    fin>>n;
    for (int z=1;z<=n;z++){
        string s;
        fin>>s;
        vector <int> v(0);
        for (int i=0;i<s.size();i++) v.push_back(s[i]-'0');
        next_permutation(v.begin(),v.end());
        bool aux=true;
        for (int i=1;i<v.size()&&aux;i++) if (v[i]<v[i-1]) aux=false;
        fout<<"Case #"<<z<<": ";
        if (aux){
            int mem=0;
            if (v[0]==0){
                for (int i=0;i<v.size();i++){
                    if (v[i]!=0){
                        mem=v[i];
                        v[i]=0;
                        break;
                    }
                }
                fout<<mem;
            }
            else{
                fout<<v[0];
                v[0]=0;
            }
        }
        for (int i=0;i<v.size();i++) fout<<v[i];
        fout<<endl;
    }
    fin.close();
    fout.close();
}
