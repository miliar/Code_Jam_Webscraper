#include<cstdio>
#include<cstdlib>
int N,T;
char str[101][101];
double ans[101],owp[101],all[101],c[101];
int main()
{
    freopen("test.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(int r =1;r<=T;r++)
    {
        printf("Case #%d:\n",r);
        scanf("%d",&N);
        for(int i=0;i<N;i++)
          scanf("%s",str[i]);
        for(int i=0;i<N;i++)
        {
            ans[i] = 0; 
            all[i]=0;c[i]=0;
            for(int j=0;j<N;j++)
            {
               if(str[i][j]=='1')
                  {all[i]++;c[i]++;}
               else if(str[i][j]=='0')
                  all[i]++;  
            }    
            ans[i] = 0.25*(c[i])/all[i];
        }
        for(int i=0;i<N;i++)
        {
           owp[i]=0.0;
           for(int j=0;j<N;j++)
           {
              if(i!=j&&str[i][j]=='1')      
                 {owp[i]+=c[j]/(all[j]-1);}
              else if(i!=j&&str[i][j]=='0') 
                 {owp[i]+=(double)(c[j]-1)/(double)(all[j]-1);}
           }        
           //printf("%d %lf\n",i,owp[i]);
           owp[i] = owp[i]/all[i];
           ans[i] += 0.5*owp[i];
        }
        for(int i=0;i<N;i++)
        {
           double x=0;
           for(int j=0;j<N;j++)
              if(i!=j&&str[i][j]!='.')
                 x+=owp[j];
           ans[i] += 0.25*x/(double)(all[i]);
        }/**/
        for(int i=0;i<N;i++)
          printf("%lf\n",ans[i]);
    }
    //system("pause");
    return 0;
}
