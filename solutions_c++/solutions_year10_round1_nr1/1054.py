#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<numeric>
#include<map>
#include<set>
#include<queue>
using namespace std ;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int cas;cin>>cas;
    for(int caso=0;caso<cas;caso++){
        cout<<"Case #"<<caso+1<<": ";
        int x,K;
        cin>>x>>K;
        vector<string>v(51,string(51,'.'));
        vector<string>v2=v;
        vector<string>v4=v;
        for(int i=0;i<x;i++){
            string aux;cin>>aux;
            v[i]=aux;   
        }
        for(int i=x-1;i>=0;i--){
            string a=v[i];
            for(int j=0;j<x;j++)
                v2[j][x-1-i]=a[j];    
        }
        int cont=0;
        for(int i=0;i<v2.size();i++){
            string h="";
            for(int j=0;j<v2.size();j++){
                if(v2[j][i]!='.'){
                    h+=v2[j][i];
                }
            }
            int beso=0;
            for(int j=v4.size()-h.size();j<v4.size();j++)
                v4[j][i]=h[beso++];
        }    
        v=v4;
        int cont1=0,cont2=0;
        for(int i=0;i<v.size();i++)
            for(int j=0;j<v[0].size();j++){
                bool azul=0;bool rojo=0;
                int cont=0;
                for(int k=0;k<K && i<v.size() && j+k<v[0].size();k++)if(v[i][j+k]=='R')cont++;    
                if(cont==K)rojo=1;
                cont=0;
                for(int k=0;k<K && i+k<v.size() && j<v[0].size();k++)if(v[i+k][j]=='R')cont++;    
                if(cont==K)rojo=1;
                cont=0;
                for(int k=0;k<K && i+k<v.size() && j+k<v[0].size();k++)if(v[i+k][j+k]=='R')cont++;    
                if(cont==K)rojo=1;
                cont=0;
                for(int k=0;k<K && i+k<v.size() && j-k<v[0].size();k++)if(v[i+k][j-k]=='R')cont++;    
                if(cont==K)rojo=1;
                cont=0;
                
                
                for(int k=0;k<K && i<v.size() && j+k<v[0].size();k++)if(v[i][j+k]=='B')cont++;    
                if(cont==K)azul=1;
                cont=0;
                for(int k=0;k<K && i+k<v.size() && j<v[0].size();k++)if(v[i+k][j]=='B')cont++;    
                if(cont==K)azul=1;
                cont=0;
                for(int k=0;k<K && i+k<v.size() && j+k<v[0].size();k++)if(v[i+k][j+k]=='B')cont++;    
                if(cont==K)azul=1;
                cont=0;
                for(int k=0;k<K && i+k<v.size() && j-k<v[0].size();k++)if(v[i+k][j-k]=='B')cont++;    
                if(cont==K)azul=1;
                cont=0;
                
                cont=0;
                if(azul)cont1++;
                if(rojo)cont2++;
            }
        if(cont1>0&& cont2>0)cout<<"Both"<<endl;
        if(cont1>0&& cont2==0)cout<<"Blue"<<endl;
        if(cont1==0&& cont2>0)cout<<"Red"<<endl;
        if(cont1==0&& cont2==0)cout<<"Neither"<<endl;
    }
    //system("pause");
    return 0;
}


