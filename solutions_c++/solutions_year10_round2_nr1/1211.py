#include<iostream>
#include<cstring>
#include<map>
#include<cctype>
using namespace std;


char S[1001][1001],S1[1001][1001];
char S3[1001],S4[1001];


map<string,int>mp;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("o.txt","w",stdout);
       int n,m,t,cas=1,i,j,k,cnt;
       scanf("%d",&t);
       while(t--)
       {

           mp.clear();
           cnt=0;
             scanf("%d %d",&n,&m);
             for(i=0;i<n;i++)
             {
                scanf("%s",S[i]);
                mp[S[i]]=1;
             }

             for(j=0;j<m;j++)
             scanf("%s",S1[j]);
             int c=0;
             for(i=0;i<m;i++)
             {
                 memset(S4,0,sizeof(S4));
                 if(mp[S1[i]])
                     continue;
                 else
                 {
                   strcat(S1[i],"/") ;
                   for(j=k=0;S1[i][j];j++)
                    if(isdigit(S1[i][j])||isalpha(S1[i][j]) || c==0)
                    {
                        S3[k++]=S1[i][j];
                        c=1;
                    }
                    else if(S1[i][j]=='/' && c==1)
                    {
                       S3[k]=0;k=0;
                       c=0;
                       strcat(S4,S3);
                       if(!mp[S4])
                       {
                           cnt++;
                           mp[S4]=1;
                           //printf("%s\n",S4);
                       }

                        S3[k++]=S1[i][j];
                    }

                 }

             }
             printf("Case #%d: %d\n",cas++,cnt);
       }

    return 0;
}
