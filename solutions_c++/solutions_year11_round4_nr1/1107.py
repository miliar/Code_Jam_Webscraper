#include<iostream>
using namespace std;
int T,S,R,X,N,T1;
int a[1001],b[1001],c[1001];
int num;
int par(int low,int high)
{
    int key=c[low],key1=a[low],key2=b[low];
    while(low<high){
                    while(low<high&&c[high]>=key)high--;
                    c[low]=c[high];a[low]=a[high];b[low]=b[high];
                    while(low<high&&c[low]<=key)low++;
                    c[high]=c[low];a[high]=a[low];b[high]=b[low];
                    }
    c[low]=key;b[low]=key2;a[low]=key1;
    return low;
}
void qsort(int low,int high)
{
     if(low<high)
     {
     int piv=par(low,high);
     qsort(low,piv-1);
     qsort(piv+1,high);
     }
}
int main()
{
    //freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    double sum=0;
    int i,j;
    scanf("%d",&T);
    for(i=1;i<=T;i++){
                      double sum=0,y,s,r;
                      scanf("%d%d%d%d%d",&X,&S,&R,&T1,&N);y=double(T1);s=double(S);r=double(R);
                      num=X;
                      for(j=1;j<=N;j++){scanf("%d%d%d",&a[j],&b[j],&c[j]);num-=b[j]-a[j];}
                      a[N+1]=0;b[N+1]=num;c[N+1]=0;
                      qsort(1,N+1);
                      for(j=1;j<=N+1;j++){
                                          //printf("%d %d %d\n",a[j],b[j],c[j]);
                                          if(y!=0){
                                                   if(y*(r+c[j])>double(b[j]-a[j])){
                                                                                    sum+=double(b[j]-a[j])/(r+c[j]);
                                                                                    y-=double(b[j]-a[j])/(r+c[j]);
                                                                                    }
                                                   else{
                                                        sum+=y+(double(b[j]-a[j])-y*(r+c[j]))/(s+c[j]);
                                                        y=0;
                                                        }
                                                   }
                                          else sum+=double(b[j]-a[j])/(s+c[j]);
                                          //printf("%lf\n",sum);
                                          }
                      printf("Case #%d: %lf\n",i,sum);
                      }
    while(1);
}
    
