#include<iostream>
#include<string.h>
using namespace std;

#define MAXN 102

string mat[MAXN];
double WP[MAXN];
double WP2[MAXN][MAXN];
double OWP[MAXN];
double OOWP[MAXN];

int main()
{
//    freopen("A.in","r",stdin);
//    freopen("A.out","w",stdout);
    int t;
    cin>>t;
    int num=1;
    while(t--){
       int n;
       scanf("%d",&n);
       int i,j,k;
       for(i=0;i<n;i++)
         cin>>mat[i];
       int win,sum;
       for(i=0;i<n;i++){
          win=sum=0;
          for(j=0;j<n;j++)
            if(mat[i][j]=='1'){sum++;win++;}
            else if(mat[i][j]=='0'){sum++;}
          if(sum) WP[i]=win*1.0/sum;
          else WP[i]=0;
       }
       for(i=0;i<n;i++)
         for(k=0;k<n;k++)
           if(i!=k){
                  win=sum=0;
                  for(j=0;j<n;j++)
                  if(j!=k){
                    if(mat[i][j]=='1'){sum++;win++;}
                    else if(mat[i][j]=='0'){sum++;}
                  }
                  if(sum) WP2[i][k]=win*1.0/sum;
                  else WP2[i][k]=0;
           }
       double tmp;
       for(i=0;i<n;i++){
          sum=0;
          tmp=0.0;
          for(j=0;j<n;j++)
            if(mat[i][j]!='.'){
               sum++;
               tmp+=WP2[j][i];
            }
          if(sum) OWP[i]=tmp/sum;
          else OWP[i]=0;
       }
       for(i=0;i<n;i++){
          sum=0;
          tmp=0.0;
          for(j=0;j<n;j++)
            if(mat[i][j]!='.'){
               sum++;
               tmp+=OWP[j];
            }
          if(sum) OOWP[i]=tmp/sum;
          else OOWP[i]=0;
       }
       printf("Case #%d:\n",num++);
       for(i=0;i<n;i++){
   //      cout<<WP[i]<<" "<<OWP[i]<<" "<<OOWP[i]<<endl;
    //     cout<<0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]<<endl;
          printf("%.8lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
       }
    }
}
