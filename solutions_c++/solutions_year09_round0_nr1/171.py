#include<iostream>
#include<vector>
using namespace std;
char T[5010][30][20];
int main(){
    int L,D,N;
    cin>>L>>D>>N;
    int test=1;
    for(int i=0;i<D;++i){
        string s;
        cin>>s;
        for(int j=0;j<L;++j)
            T[i][s[j]-'a'][j]=1;
    }
    while(N--){
        vector<int> V;
        for(int i=0;i<D;++i){
            V.push_back(i);
        }
        string s;
        cin>>s;
        int index=0;
        for(int i=0;i<L;++i){
            vector<int> V2;
            vector<int> opciones;
            if(s[index]!='('){
                opciones.push_back(s[index]-'a');
                index++;
            }
            else{
                index++;
                while(s[index]!=')'){
                    opciones.push_back(s[index]-'a');
                    index++;
                }
                index++;
            }
            for(int j=0;j<V.size();++j){
                for(int k=0;k<opciones.size();++k)
                    if(T[V[j]][opciones[k]][i]){
                        V2.push_back(V[j]);
                        break;
                    }
            }
            V=V2;
        }
        cout<<"Case #"<<test++<<": "<<V.size()<<endl;
    }
}
