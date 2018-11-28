#include<cstdio>
struct but{
    int r;
    int p;
    but(){}
    but(int _r,int _p){
        r=_r;
        p=_p;
        }
    };
but b[101];
int caso;
void doit(){
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        char rob[2];
        int pos;
        scanf("%s%d",&rob,&pos);
        b[i]=but((rob[0]=='O')?0:1,pos);
        }
    int t1=0,tt1=0;
    int t2=0;
    int time=0;
    int pos[2]={1,1};
    for(int i=0;i<n;i++){
        int ro=b[i].r;
        if(i!=0 && b[i].r!=b[i-1].r){
            t2=b[i].p-pos[ro];
            if(t2<0)t2*=-1;
            pos[ro]=b[i].p;
            if(t2>=tt1){
                time+=(t2-tt1);
                tt1=t2-tt1;
                }
            else tt1=0;
            tt1++;
            time++;
            }
        else{
            t1=b[i].p-pos[ro];
            if(t1<0)t1*=-1;
            t1++;
            tt1+=t1;
            pos[ro]=b[i].p;
            time+=t1;
            }
        //printf("%d\n",time);
        }
    printf("Case #%d: %d\n",++caso,time);
    }
int main(){
    int C;
    caso=0;
    scanf("%d",&C);
    for(int i=0;i<C;i++)doit();
    }
