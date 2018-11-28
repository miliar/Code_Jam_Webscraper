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
    int caso;
    cin>>caso;
    for(int casos=0;casos<caso;casos++){
        int dev=0;
        int N,M;
        cin>>N>>M;
        vector<vector<string> >x(N);
        for(int i=0;i<N;i++){
            string a="";
            cin>>a;
            for(int j=0;j<a.size();j++)if(a[j]=='/')a[j]=' ';
            istringstream is(a);
            string aux;
            vector<string>aux2;
            while(is>>aux){
                aux2.push_back(aux);
            }
            x[i]=aux2;
        }
        for(int i=0;i<M;i++){
            string a="";
            cin>>a;
            for(int j=0;j<a.size();j++)if(a[j]=='/')a[j]=' ';
            istringstream is(a);
            string aux;
            vector<string>aux2;
            while(is>>aux){
                aux2.push_back(aux);
            }
            int mini=aux2.size();
            for(int j=0;j<x.size();j++){
                vector<string> h=x[j];
                int cont=0;
                for(int k=0;k<min((int)aux2.size(),(int)h.size());k++){
                    if(aux2[k]==h[k]){
                        cont++;    
                    }else{
                        break;
                    }       
                }
                cont=aux2.size()-cont;
                mini=min(mini,cont);
            }
            x.push_back(aux2);
            dev+=mini;
        }
        cout<<"Case #"<<casos+1<<": "<<dev<<endl;
    }

    //system("pause");
    return 0;
}


