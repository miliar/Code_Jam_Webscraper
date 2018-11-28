#include<cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
char res[200];
int t;
int C,D,N;
struct cb
{
    char A,B,C;
}cm[40];
struct op
{
    char A,B;
}p[40];
int check(char A,char B)
{
    for(int i=0;i<C;i++){
        if(A==cm[i].A&&B==cm[i].B) return i;
        if(A==cm[i].B&&B==cm[i].A) return i;
    }
    return -1;
}
int run(char A)
{
    for(int i=0;i<t;i++){
        char B=res[i];
        for(int j=0;j<D;j++){
            if(A==p[j].A&&B==p[j].B) return 1;
            if(B==p[j].A&&A==p[j].B) return 1;
        }
    }
    return 0;
}

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T,ca=0;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++ca);
        char s[200];
        scanf("%d",&C);
        for(int i=0;i<C;i++){
            scanf("%s",s);
            cm[i].A=s[0],cm[i].B=s[1],cm[i].C=s[2];
        }
        scanf("%d",&D);
        for(int i=0;i<D;i++){
            scanf("%s",s);
            p[i].A=s[0],p[i].B=s[1];
        }
        scanf("%d",&N);
        scanf("%s",s);
        t=0;
        for(int i=0;i<N;i++){
            if(t==0) res[t++]=s[i];
            else {
                char tmp=s[i];
                int p=check(tmp,res[t-1]);
                while(p!=-1){
                    t--;
                    tmp=cm[p].C;
                    if(t==0) p=-1;
                    else p=check(tmp,res[t-1]);
                }
                if(run(tmp)) t=0;
                else res[t++]=tmp;
            }
        }
        if(t==0) puts("[]");
        else {
            printf("[%c",res[0]);
            for(int i=1;i<t;i++)
                printf(", %c",res[i]);
            puts("]");
        }
    }
}




