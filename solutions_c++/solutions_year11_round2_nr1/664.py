#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>

using namespace std;

int m[100][100];

int main()
{
    int t,T,n,i,j;
    char s[200];
    freopen("A-large.in","r",stdin);
   freopen("output.txt","w",stdout);   
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);
        memset(m,0,sizeof m);
int wp[100]={},np[100]={};
double owp[100]={},oowp[100]={};
                        
        for(i=0;i<n;i++)
        {
            scanf("%s",&s);
            for(j=0;j<n;j++)
                if(s[j]=='1') {m[i][j]=1; wp[i]++;np[i]++;}
                else if(s[j]=='0') {m[i][j]=-1; np[i]++;}
                else m[i][j]=0;
    //        cout<<wp[i]<<" "<<np[i]<<endl;
        }
        for(i=0;i<n;i++)
        {
            int k=0;
            for(j=0;j<n;j++)
                if(i==j) continue;
                else
                {
                    if(m[i][j]) { owp[i]+=1.0*(wp[j]- (m[i][j]==-1))/(np[j]-1);
                    k++;}
                }   
            owp[i]/=k;
  //          cout<<owp[i]<<endl;        
        }
                
        for(i=0;i<n;i++)
        {
            int k=0;
            for(j=0;j<n;j++)
                if(m[i][j]) {oowp[i]+=owp[j];k++;};
            if(k)
            oowp[i]/=k;
//            cout<<oowp[i]<<endl;        
            
        }
        
        printf("Case #%d: \n",t);
        for(i=0;i<n;i++)
            printf("%.12f\n",0.25*wp[i]/np[i]+0.5*owp[i]+0.25*oowp[i]);
    }
//system("pause");

    return 0;
}
