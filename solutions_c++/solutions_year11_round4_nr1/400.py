#include<stdio.h>
#include<algorithm>
using namespace std;
struct data{
    int len,speed;
    bool operator<(data z)const{
        return speed<z.speed;
    }
}a[1011];
int main(){
    int C,x,s,r,t,n,sum,Case=1;
    double time,remain;
    scanf("%d",&C);
    while(C--){
        scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
        sum=0;
        for(int i=0;i<n;i++){
            int tempx,tempy;
            scanf("%d%d%d",&tempx,&tempy,&a[i].speed);
            a[i].len=tempy-tempx;
            sum+=a[i].len;
        }
        a[n].len=x-sum;
        a[n].speed=0;
        n++;
        sort(a,a+n);
        time=0.0,remain=t;
        for(int i=0;i<n;i++)
            if(remain>0){
                double temp=(double)a[i].len/(r+a[i].speed);
                if(remain>=temp){
                    time+=temp;
                    remain-=temp;
                }else{
                    double len=(r+a[i].speed)*remain;
                    time+=remain;
                    remain=0;
                    len=a[i].len-len;
                    time+=len/(s+a[i].speed);
                } 
            }else time+=(double)a[i].len/(s+a[i].speed);
        printf("Case #%d: %.10lf\n",Case++,time);
    }
}
