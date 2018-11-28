#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<math.h>
#include<set>
#include<map>
#define f first
#define s second
char Z[100][100];
using namespace std;
int main()
{
 int T;
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 scanf("%d\n",&T);
 for(int caso=1;caso<=T;caso++)
 {
     int N;
     scanf("%d\n",&N);
     for(int i=0;i<N;i++){for(int j=0;j<N;j++)scanf("%c",&Z[i][j]);scanf("\n");}
     
     int s=0;
     vector<int>V;
     for(int i=0;i<N;i++)V.push_back(0);
     for(int i=0;i<N;i++)for(int j=N-1;j>=0;j--)if(Z[i][j]=='1'){V[i]=j;break;}
     //for(int i=0;i<N;i++)cout<<V[i];cout<<endl;
     
     queue<pair<vector<int>,int> >Q;
     map<vector<int>,int >S;
     Q.push(make_pair(V,0));
     bool zz=true;
     for(int i=0;i<N;i++)if(V[i]>i){zz=false;break;}
     while(!zz)
     {
            vector<int>U=Q.front().f;
            
            int a=Q.front().s;
            Q.pop();
            
            for(int i=0;i<N-1;i++)for(int j=i+1;j<i+2;j++)
            {
                int t=U[i];    
                U[i]=U[j];
                U[j]=t;
                //for(int h=0;h<N;h++)cout<<U[h]<<" ";cout<<endl;    
                if(S.count(U))
                {
                    t=U[i];    
                U[i]=U[j];
                U[j]=t;
                continue;          
                }
                S[U]=1;
                Q.push(make_pair(U,a+1));
                int u;
                for(u=0;u<N;u++)if(U[u]>u)break;
                
                if(u==N)
                {
                    j=N;
                    i=N;
                    zz=true;
                    s=a+1;        
                }
                t=U[i];    
                U[i]=U[j];
                U[j]=t;        
            }
     } 
     cout<<"Case #"<<caso<<": "<<s<<endl;
             
 }   
return 0;    
}
