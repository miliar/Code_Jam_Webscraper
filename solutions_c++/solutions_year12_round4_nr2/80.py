#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<assert.h>
#include<stdarg.h>
#include<time.h>
#include<string>
#include<map>
#include<set>
#include<algorithm>
#include<vector>
using namespace std;
int ri[1010];
int id[1010];
int xi[1010],yi[1010];
inline int cmp(int a,int b){return ri[a]>ri[b];}
int main(){
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
        int n,i,j,k;
        int w,l;
        scanf("%d%d%d",&n,&w,&l);
        for(i=0;i<n;i++){
            scanf("%d",&ri[i]);
            id[i]=i;
        }
        sort(id,id+n,cmp);
        int ii,jj,kk;
        int x=0;
        for(ii=0;ii<n;ii=jj){
            i=id[ii];
            //printf("ii=%d %d\n",ii,i);
            int tt;
            if(ii==0){
                xi[i]=0;
                tt=ri[i];
            }else{
                xi[i]=x+ri[i];
                tt=2*ri[i];
            }
            yi[i]=0;
            int y=ri[i];
            if(tt>w)tt=w;
            for(jj=ii+1;jj<n;jj=kk){
                int j=id[jj];
                if(y+ri[j]>l)break;
                //printf("jj=%d %d\n",jj,j);
                int xx;
                if(ii==0){
                    xi[j]=0;
                    xx=ri[j];
                }else{
                    xi[j]=x+ri[j];
                    xx=2*ri[j];
                }
                yi[j]=y+ri[j];
                for(kk=jj+1;kk<n;kk++){
                    int k=id[kk];
                    if(xx+2*ri[k]>tt)break;
                    //printf("kk=%d %d %d\n",kk,k,xx);
                    xi[k]=x+xx+ri[k];
                    yi[k]=y+ri[k];
                    xx+=2*ri[k];
                }
                y+=2*ri[j];
            }
            x+=2*ri[i];
        }
        printf("Case #%d:",cas++);
        for(i=0;i<n;i++)printf(" %d %d",xi[i],yi[i]);
        puts("");
    }
}

