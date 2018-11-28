#include<iostream>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cnt=1;
    cin>>T;
    while(T--)
    {
              int ans=0;
              int N,S,P;
              int score[105];
              cin>>N>>S>>P;
              for(int i=0;i<N;i++)
              cin>>score[i];
              
              for(int i=0;i<N;i++)
              if(score[i]/3>=P)
              ans++;
              else if(score[i]>score[i]/3*3&&score[i]/3+1==P)
              ans++;
              else if(score[i]==score[i]/3*3&&score[i]/3>0&&score[i]/3+1==P&&S>0)
              {ans++;S--;}
              
              else if(score[i]==2+score[i]/3*3&&score[i]/3+2==P&&S>0)
              {ans++;S--;}
                   
              printf("Case #%d: %d\n",cnt++,ans);
              }
    return 0;
}
              
