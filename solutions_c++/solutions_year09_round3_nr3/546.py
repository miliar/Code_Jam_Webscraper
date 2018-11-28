//Made by: Albert Villalobos

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <fstream>
using namespace std;

int main(){
    ifstream fin("C-Small.in");
    ofstream fout("C-Small.out");
    int n;
    fin>>n;
    for (int z=1;z<=n;z++){
        int p,q;
        fin>>p>>q;
        vector <int> v(q);
        for (int i=0;i<q;i++) fin>>v[i];
        int min=-1;
        do{
            int tot=0;
            map <int,bool> m;
            m[0]=true;
            m[p+1]=true;
            for (int i=0;i<v.size();i++){
                for (int j=v[i]+1;m[j]==false&&j<=p;j++){tot++;}
                for (int j=v[i]-1;m[j]==false&&j>0;j--){tot++;}
                m[v[i]]=true;
            }
            if (min==-1||tot<min) min=tot;
        }while (next_permutation(v.begin(),v.end()));
        fout<<"Case #"<<z<<": "<<min<<endl;
    }
    fin.close();
    fout.close();
}
