#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,k,n;
    int d,tmp;
    int o[1000],b[1000];
    int t[1000];
    int po,pb;
    char s[3];
    int count;
    int no,nb;
    int p,oo,bb;
    scanf("%d",&n);
    for(k=1;k<=n;k++){
        scanf("%d",&tmp);
        for(j=0,po=0,pb=0;j<tmp;j++){
            scanf("%s%d",s,&d);
            if(s[0]=='O'){
                t[j]=0;
                o[po++]=d;
            }
            else {
                t[j]=1;
                b[pb++]=d;
            }
        }
        no=po;
        nb=pb;
        for(count=0,po=0,pb=0,p=0,oo=1,bb=1;po!=no||pb!=nb;count++){
            if(t[p]==0){
                if(o[po]!=oo){
                    oo+=((o[po]-oo)/(int)abs(o[po]-oo));
                    if(b[pb]-bb!=0&&pb!=nb) bb+=((b[pb]-bb)/(int)abs(b[pb]-bb));
                }
                else{
                    po++;
                    p++;
                    if(b[pb]-bb!=0&&pb!=nb) bb+=((b[pb]-bb)/(int)abs(b[pb]-bb));
                }
            }
            else{
                if(b[pb]!=bb){
                    bb+=((b[pb]-bb)/(int)abs(b[pb]-bb));
                    if(o[po]-oo!=0&&po!=no) oo+=((o[po]-oo)/(int)abs(o[po]-oo));
                }
                else{
                    pb++;
                    p++;
                    if(o[po]-oo!=0&&po!=no) oo+=((o[po]-oo)/(int)abs(o[po]-oo));
                }
            }
        }
        printf("Case #%d: %d\n",k,count);
    }
    //system("pause");
    return 0;
    
}
