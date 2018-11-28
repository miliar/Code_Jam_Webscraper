#include<cstdio>
#include<cstring>
#define abs(x) ((x)<0?-(x):(x))
#define min(x,y) (x<y?x:y)
#define clr(a,b) memset(a,b,sizeof(a))
#define maxn 200

using namespace std;

int T,n;
char d[maxn][maxn];
double wp[maxn],op[maxn],oop[maxn],wpt[maxn][maxn];

void init()
{
    scanf("%d",&n);
    for (int i=0;i<n;i++)
        for (int j=0;j<n;j++){
            char c;
            do{
                scanf("%c",&c);
            }while (c!='.'&&c!='0'&&c!='1');
            d[i][j]=c;
        }
}

int work()
{
    for (int i=0;i<n;i++){
        double x=0,y=0;
        for (int j=0;j<n;j++){
            if (d[i][j]!='.') y+=1;
            if (d[i][j]=='1') x+=1;
        }
        wp[i]=x/y;
        for (int j=0;j<n;j++){
            if (d[i][j]=='.') wpt[i][j]=-1;
            if (d[i][j]=='1') wpt[i][j]=(x-1)/(y-1);
            if (d[i][j]=='0') wpt[i][j]=(x)/(y-1);
        }
    }

    for (int i=0;i<n;i++){
        double x=0,y=0;
        for (int j=0;j<n;j++){
            if (d[i][j]!='.'){
                x+=wpt[j][i];y++;
            }
        }
        op[i]=x/y;
    }

    for (int i=0;i<n;i++){
        double x=0,y=0;
        for (int j=0;j<n;j++){
            if (d[i][j]!='.'){
                x+=op[j];y++;
            }
        }
        oop[i]=x/y;
    }
}

int main()
{
    FILE *cin=freopen("B.txt", "w", stdout);
    scanf("%d",&T);
    for (int tnum=1;tnum<=T;tnum++){
        init();
        work();
        printf("Case #%d:\n",tnum);
        for (int i=0;i<n;i++){
            printf("%0.12f\n",0.25*wp[i]+0.5*op[i]+0.25*oop[i]);
        }
    }
}
