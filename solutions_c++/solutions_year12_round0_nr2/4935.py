#include<cstdio>

int t[200];
int n,s,p,C,caso=0;
void doit(){
    scanf("%d%d%d",&n,&s,&p);
    for(int i=0;i<n;++i)scanf("%d",t+i);
    int ans=0;
    for(int i=0;i<n;++i){
        int k=t[i]/3;
        if(t[i]%3==0){
            if(k>=p)++ans;
            else if(s>0 && k+1>=p && k-1>=0)++ans,--s;
            }
        if(t[i]%3==1)if(k+1>=p)++ans;
        if(t[i]%3==2){
            if(k+1>=p)++ans;
            else if(s>0 && k+2>=p)++ans,--s;
            }
        }
    printf("Case #%d: %d\n",++caso,ans);
    }
int main(){
    scanf("%d",&C);
    for(int i=0;i<C;++i)doit();
    }
