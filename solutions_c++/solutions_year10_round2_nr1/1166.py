using namespace std;
#include<cstdio>
#include<iostream>
#include<vector>
#include<string>
#include<map>
int main()
{   int x,y,z,N,T,M,ans;
    scanf("%d",&T); 
    for(x=0;x<T;x++)
    {  string S,w;
       scanf("%d %d",&N,&M); 
       getline(cin,S);
       map<string,bool> di;
       ans=0;
       for(z=0;z<N;z++)
       {  getline(cin,S); w.clear(); di[S]=1; 
          for(y=0;y<S.length();y++)
          { if(S[y]=='/' && y!=0) di[w]=1;
              w.push_back(S[y]);
          }
       }
       for(z=0;z<M;z++)
       {  getline(cin,S); w.clear(); 
          for(y=0;y<S.length();y++)
          { if(S[y]=='/' && y!=0)
            { //cout<<endl<<w<<" "<<di[w]<<" "<<ans<<endl;
              if(!di[w]) { ans++; di[w]=1;}
              //cout<<w<<" "<<di[w]<<" "<<ans<<endl<<endl;
            }
            w.push_back(S[y]);
          }
          if(!di[S]) { ans++; di[w]=1;} 
      }
       printf("Case #%d: %d\n",x+1,ans);    
     }
     return 0;
}     
