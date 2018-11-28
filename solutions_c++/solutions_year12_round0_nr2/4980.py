#include<cstdio>

int a[150];
int n,s,p,t;
void doit(){

    }
int main(){
    scanf("%d",&t);
    for(int i=1;i<=t;++i){
        scanf("%d%d%d",&n,&s,&p);
        for(int j=0;j<n;++j)scanf("%d",&a[j]);
        int res=0;
        for(int j=0;j<n;++j){
            int q=a[j]/3;
            if(a[j]%3==0){
                if(q>=p)res++;
                else if(s>0 && q+1>=p && q-1>=0){
                    res++;
                    s--;
                    }
                }
            if(a[j]%3==1)if(q+1>=p)res++;
            if(a[j]%3==2){
                if(q+1>=p)res++;
                else if(s>0 && q+2>=p)res++,s--;
                }
            }
        printf("Case #%d: %d\n",i,res);
        }
    }
