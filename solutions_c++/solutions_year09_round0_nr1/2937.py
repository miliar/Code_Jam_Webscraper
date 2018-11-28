#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;

int main(){
    ifstream fin("A-Large.in");
    ofstream fout("A-Large.out");
    int l,d,n;
    fin>>l>>d>>n;
    vector <string> v(d);
    for (int i=0;i<d;i++) fin>>v[i];
    for (int z=1;z<=n;z++){
        string s;
        vector <vector <char> > w(l, vector <char> (0));
        fin>>s;
        int cont=0;
        for (int i=0;i<s.size();i++){
            if (s[i]=='('){
                i++;
                while (s[i]!=')'){
                    w[cont].push_back(s[i]);
                    i++;
                }
            }
            else w[cont].push_back(s[i]);
            cont++;
        }
        int tot=0;
        for (int i=0;i<d;i++){
            for (int j=0;j<l;j++){
                bool trobat=false;
                for (int k=0;k<w[j].size();k++) if (v[i][j]==w[j][k]){trobat=true; break;}
                if (trobat){
                    if (j==l-1) tot++;
                    continue;
                }
                break;
            }
        }
        fout<<"Case #"<<z<<": "<<tot<<endl;
    }
    fin.close();
    fout.close();
}
