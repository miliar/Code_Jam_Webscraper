#include<cstdio>
#define fo(i,u,d) for(int i=u;i<=d;i++)
#define fr(i,u,d) for(int i=u;i>=d;i--)
using namespace std;
int n,k;
char s[20];
int ca;
char a[100][100];
void init(){
    scanf("%d%d",&n,&k);
    gets(s);
    fo(i,1,n){
        fo(j,1,n)scanf("%c",&a[j][n-i+1]);
        gets(s);
    }
}
void swap(char &a,char &b){
    char tmp=a;
    a=b;
    b=tmp;
}
bool check(char x){
    fo(i,1,n){
        fo(j,1,n){
            int t=0;
            int ii=i;
            int jj=j;
            while ((ii<=n)&&(a[ii][jj]==x)){
                ii++;
                t++;
            }
            if (t>=k)return true;

            ii=i;
            jj=j;
            t=0;
            while ((jj<=n)&&(a[ii][jj]==x)){
                jj++;
                t++;
            }
            if (t>=k)return true;


            ii=i;
            jj=j;
            t=0;
            while ((jj<=n)&&(ii<=n)&&(a[ii][jj]==x)){
                jj++;
                ii++;
                t++;
            }
            if (t>=k)return true;


            ii=i;
            jj=j;
            t=0;
            while ((ii<=n)&&(jj>=1)&&(a[ii][jj]==x)){
                ii++;
                jj--;
                t++;
            }
            if (t>=k)return true;
        }
    }
    return false;
}
void work(){
    fr(i,n,1){
        fo(j,1,n){
            if (a[i][j]=='.')continue;
            int ii=i;
            while ((ii+1<=n)&&(a[ii+1][j]=='.')){
                swap(a[ii+1][j],a[ii][j]);
                ii++;
            }
        }
    }
    /*fo(i,1,n){
        fo(j,1,n)printf("%c",a[i][j]);
        printf("\n");
    }*/
    bool R=check('R');
    bool B=check('B');
    if (R && B){
        printf("Both\n");
    }else
        if (R){
            printf("Red\n");
        }
        else if (B){
            printf("Blue\n");
        }
        else{
            printf("Neither\n");
        }
}
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&ca);
    fo(i,1,ca){
        init();
        printf("Case #%d: ",i);
        work();
    }
    return 0;
}
