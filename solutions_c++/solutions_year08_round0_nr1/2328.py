#include<iostream>
#include<vector>
#include<string>
#include<fstream>
using namespace std;
int main() {
    ofstream fout("resultat.txt");
    int casos,s,q;
    cin>>casos;
    vector<int> ccc(casos);
    for(int cas=0;cas<casos;cas++) {
        cin>>s;
        vector<string> g(s);
        cin.ignore();
        for(int i=0;i<s;i++) getline(cin,g[i]);
        cin>>q;
        vector<string> b(q);
        cin.ignore();
        for(int i=0;i<q;i++) getline(cin,b[i]);
        //cout<<"comensa"<<endl;
        if(q==0) {
                 cout<<"Case #"<<cas+1<<": 0"<<endl;
                 ccc[cas]=0;
        }
        else {
             vector< vector<bool> > vb(s,q);
             for(int i=0;i<s;i++) for(int a=0;a<q;a++) vb[i][a]=(g[i]!=b[a]);
             vector< vector<int> > v(s,q);
             for(int i=0;i<s;i++) {
                 if(vb[i][0]) v[i][0]=0;
                 else v[i][0]=10000;
             }
             for(int a=1;a<q;a++) {
                 for(int i=0;i<s;i++) {
                     int mini=v[i][a-1];
                     for(int z=0;z<s;z++) if((v[z][a-1]+1)<mini) mini=v[z][a-1]+1;
                     v[i][a]=mini;
                     if(!vb[i][a]) v[i][a]=10000;
                 }
             }
             int min=100000;
             for(int i=0;i<s;i++) if(v[i][q-1]<min) min=v[i][q-1];
             for(int i=0;i<s;i++) {
                 for(int a=0;a<q;a++) cout<<v[i][a]<<" ";
                 cout<<endl;
             }
             cout<<"Case #"<<cas+1<<": "<<min<<endl;
             ccc[cas]=min;
        }
    }
    for(int i=0;i<casos;i++) fout<<"Case #"<<i+1<<": "<<ccc[i]<<endl;
    system("pause");
}
             
