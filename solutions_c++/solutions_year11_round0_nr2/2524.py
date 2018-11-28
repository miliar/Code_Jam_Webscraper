#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<vector>
#include<cmath>

using namespace std;
int main(){
    int nc;
    cin>>nc;
    for(int k=0;k<nc;k++){
        int c,d,n;
        char trans[27][27];
        bool op[27][27];
        memset(trans,0,sizeof(trans));
        memset(op,0,sizeof(op));
        cin>>c;
        for(int i=0;i<c;i++){
            string s;
            cin>>s;
            trans[s[0]-'A'][s[1]-'A']=s[2];
            trans[s[1]-'A'][s[0]-'A']=s[2];    
        }
        cin>>d;
        for(int i=0;i<d;i++){
            string s;
            cin>>s;
            op[s[0]-'A'][s[1]-'A']=1;
            op[s[1]-'A'][s[0]-'A']=1;    
        }
        cin>>n;
        string s;
        cin>>s;
        string aux="";
        aux+=s[0];
        for(int i=1;i<n;i++){
            aux+=s[i];
            if(aux.length()>1){
                if(trans[aux[aux.length()-1]-'A'][aux[aux.length()-2]-'A']!=0){
                    char tt=trans[aux[aux.length()-1]-'A'][aux[aux.length()-2]-'A'];
                    aux=aux.substr(0,aux.length()-2);
                    aux+=tt;
                }
                else{
                    for(int j=0;j<aux.length()-1;j++){
                        if(op[aux[aux.length()-1]-'A'][aux[j]-'A']){
                            aux="";
                            break;     
                        }
                    }
                }
            }   
        }
        //reverse(aux.begin(),aux.end());
        cout<<"Case #"<<k+1<<": [";
        for(int i=0;i<aux.length();i++){
            if(i>0)cout<<", ";
            cout<<aux[i];
        }    
        cout<<"]"<<endl;
    }    
}
