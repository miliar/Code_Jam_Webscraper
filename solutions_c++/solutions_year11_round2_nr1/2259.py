#include<iostream>
using namespace std;
int t,k,n;
int main(){
   freopen("A-large (1).in", "r",stdin);
   freopen("A-large (1).out", "w",stdout);
   scanf("%d",&t);
   k=1;
   char ch[100];
   int i,j,a[100][100];
   float w0[100],w1[100],w2[100];
   int data[100][2];
   int w,l;
   while(k<=t){
               scanf("%d",&n);
               for(i=0;i<n;i++){
                               scanf("%s",ch);
                               w=0; l=0;
                               for(j=0;j<n;j++){
                                                if(ch[j]=='1'){ a[i][j]=1; w++;}
                                                else if(ch[j]=='.') a[i][j]=-1;
                                                else { a[i][j]=0; l++; }
                               }
                               data[i][0]=w;
                               data[i][1]=l;
                               w0[i]=(float)w/(float)(w+l);
                                   
               }
               for(j=0;j<n;j++)
               {
                       w1[j]=0.0;
                       int ct=0;
                       for(int p=0;p<n;p++)
                       {
                               if(p==j || a[p][j]==-1) continue;
                               ct++;
                               w=data[p][0];
                               l=data[p][1];
                               if(a[p][j]==1) w--;
                               else if(a[p][j]==0) l--;
                               w1[j]+=(float)w/(float)(w+l);
                       }
                       w1[j]/=ct;
               }
               for(int j=0;j<n;j++)
               {
                        w2[j]=0.0;
                        int ct=0;
                        for(int p=0;p<n;p++)
                        {
                                if(p==j || a[j][p]==-1) continue;
                                ct++;
                                w2[j]+=w1[p];
                        }
                        w2[j]/=ct;
                }
                printf("Case #%d:\n",k);
                for(int j=0;j<n;j++)
                printf("%f\n",0.25*w0[j]+0.5*w1[j]+0.25* w2[j]);

               k++;
              //printf("Case #%d: %d\n",t);
   

   }
   getchar();
   getchar();
   return 0;
}
