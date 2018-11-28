# include <stdio.h>
# include <stdlib.h>
# include <queue>
# include <string.h>
using namespace std;
struct pos{
    int num,com,r1,r2;
};
bool Y[104][104][104];
struct comandos{
    int pos;
    bool rob;
};
comandos A[110];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int c,n,i,j,k,t;
    char a;
    pos temp,val;
    queue <pos> cola;
    scanf("%d",&c);
    for(k=1;k<=c;k++){
        scanf("%d",&n);
        for(i=0;i<n;i++){
            scanf("%c",&a);
            scanf("%c",&a);
            if(a=='O'){
                A[i].rob=0;
            }else{
                A[i].rob=1;
            }
            scanf("%d",&t);
            A[i].pos=t;
        }
        memset(Y,0,sizeof(Y));
        Y[0][1][1]=1;
        temp.num=0,temp.com=0,temp.r1=1,temp.r2=1;
        cola.push(temp);
        while(!cola.empty()){
            temp=cola.front();
            cola.pop();
            //printf("%d %d %d %d\n",temp.r1,temp.r2,temp.com,temp.num);
            //getchar();
            if(temp.com==n){
                printf("Case #%d: %d\n",k,temp.num);
                while(!cola.empty()){
                    cola.pop();
                }
            }else{
                if(temp.r1<100){
                    val=temp;
                    val.r1++,val.num++;
                    if(temp.r2<100){
                        val.r2++;
                        if(!Y[val.com][val.r1][val.r2]){
                            Y[val.com][val.r1][val.r2]=1;
                            cola.push(val);
                        }
                    }
                    val=temp;
                    val.r1++,val.num++;
                    if(temp.r2>1){
                        val.r2--;
                        if(!Y[val.com][val.r1][val.r2]){
                            Y[val.com][val.r1][val.r2]=1;
                            cola.push(val);
                        }
                    }
                    val=temp;
                    val.r1++,val.num++;
                    if(!Y[val.com][val.r1][val.r2]){
                        Y[val.com][val.r1][val.r2]=1;
                        cola.push(val);
                    }
                    val=temp;
                    val.r1++,val.num++;
                    if(temp.r2==A[temp.com].pos && A[temp.com].rob==1 ){
                        val.com++;
                        if(!Y[val.com][val.r1][val.r2]){
                            Y[val.com][val.r1][val.r2]=1;
                            cola.push(val);
                        }
                    }
                }

                if(temp.r1>1){
                    val=temp;
                    val.r1--,val.num++;
                    if(temp.r2<100){
                        val.r2++;
                        if(!Y[val.com][val.r1][val.r2]){
                            Y[val.com][val.r1][val.r2]=1;
                            cola.push(val);
                        }
                    }
                    val=temp;
                    val.r1--,val.num++;
                    if(temp.r2>1){
                        val.r2--;
                        if(!Y[val.com][val.r1][val.r2]){
                            Y[val.com][val.r1][val.r2]=1;
                            cola.push(val);
                        }
                    }
                    val=temp;
                    val.r1--,val.num++;
                    if(!Y[val.com][val.r1][val.r2]){
                        Y[val.com][val.r1][val.r2]=1;
                        cola.push(val);
                    }
                    val=temp;
                    val.r1--,val.num++;
                    if(temp.r2==A[temp.com].pos && A[temp.com].rob==1 ){
                        val.com++;
                        if(!Y[val.com][val.r1][val.r2]){
                            Y[val.com][val.r1][val.r2]=1;
                            cola.push(val);
                        }
                    }
                }
                    val=temp;
                    val.num++;
                    if(temp.r2<100){
                        val.r2++;
                        if(!Y[val.com][val.r1][val.r2]){
                            Y[val.com][val.r1][val.r2]=1;
                            cola.push(val);
                        }
                    }
                    val=temp;
                    val.num++;
                    if(temp.r2>1){
                        val.r2--;
                        if(!Y[val.com][val.r1][val.r2]){
                            Y[val.com][val.r1][val.r2]=1;
                            cola.push(val);
                        }
                    }
                    val=temp;
                    val.num++;
                    if(!Y[val.com][val.r1][val.r2]){
                        Y[val.com][val.r1][val.r2]=1;
                        cola.push(val);
                    }
                    val=temp;
                    val.num++;
                    if(temp.r2==A[temp.com].pos && A[temp.com].rob==1 ){
                        val.com++;
                        if(!Y[val.com][val.r1][val.r2]){
                            Y[val.com][val.r1][val.r2]=1;
                            cola.push(val);
                        }
                    }
                if(temp.r1==A[temp.com].pos && A[temp.com].rob==0){
                    val=temp;
                    val.com++,val.num++;
                    if(temp.r2<100){
                        val.r2++;
                        if(!Y[val.com][val.r1][val.r2]){
                            Y[val.com][val.r1][val.r2]=1;
                            cola.push(val);
                        }
                    }
                    val=temp;
                    val.com++,val.num++;
                    if(temp.r2>1){
                        val.r2--;
                        if(!Y[val.com][val.r1][val.r2]){
                            Y[val.com][val.r1][val.r2]=1;
                            cola.push(val);
                        }
                    }
                    val=temp,val.num++;
                    val.com++;
                    if(!Y[val.com][val.r1][val.r2]){
                        Y[val.com][val.r1][val.r2]=1;
                        cola.push(val);
                    }
                }
            }
        }
    }
    return 0;
}
