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
        int t;
        cin>>t;
        for(int i=1;i<(1<<(t-1));i++){
            vector<int>v;
            for(int j=0;j<(t-1);j++){
                if((i&(1<<j))!=0){
                    v.push_back(2+j);
                }    
            }
            if(v.size()==0)continue;
            int ind=(int)v.size()-1;
            if(v[v.size()-1]!=t)continue;
            bool ok=0;  
            int aux=t;
            while(true){
                if(aux==1){ok=0;break;}
                bool oka=0;
                for(int j=0;j<v.size();j++)
                    if(v[j]==aux){
                        aux=j+1;
                        oka=1;
                    }    
                if(!oka){ok=1;break;}
            }
            if(!ok){
                dev++;      
            }
             
        }
        cout<<"Case #"<<casos+1<<": "<<dev<<endl;
    }
    
    //system("pause");
    return 0;
}


