#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

const int N=104;
int data[N];

int cmp(const void * a,const void * b)
{
    return * (int *)b - * (int *)a;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cases,cnt=0,n,s,p,x,res,len;
    scanf("%d",&cases);
    while(cases--){
        scanf("%d%d%d",&n,&s,&p);
        res=0;
        len=0;
        while(n--){
            scanf("%d",&x);
            if(x<=1){
                if(x>=p) res++;
            }
            else{
                data[len++]=x;
            }
        }
        qsort(data,len,sizeof(int),cmp);
        for(int i=0;i<len;i++){
            int tmp=data[i]%3;
            if(tmp==0){
                if(len-i<=s){
                    if((data[i]-3)/3+2>=p){
                        res++;
                    }
                    s--;
                }
                else if(data[i]/3>=p) res++;
                else if(s>0&&(data[i]-3)/3+2>=p){
                    s--;
                    res++;
                }
            }
            else if(tmp==1){
                if(len-i<=s){
                    if((data[i]-4)/3+2>=p){
                        res++;
                    }
                    s--;
                }
                else if(data[i]/3+1>=p) res++;
                else if(s>0&&(data[i]-4)/3+1>=p){
                    s--;
                    res++;
                }
            }
            else{
                if(len-i<=s){
                    if(data[i]/3+2>=p){
                        res++;
                    }
                    s--;
                }
                else if(data[i]/3+1>=p) res++;
                else if(s>0&&data[i]/3+2>=p){
                    s--;
                    res++;
                }
            }
        }
        printf("Case #%d: %d\n",++cnt,res);
    }
    return 0;
}
