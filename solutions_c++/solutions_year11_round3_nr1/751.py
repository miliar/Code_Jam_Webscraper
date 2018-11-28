#include<cstdio>
#include<cstring>
#define abs(x) ((x)<0?-(x):(x))
#define min(x,y) (x<y?x:y)
#define clr(a,b) memset(a,b,sizeof(a))
#define maxn 200

using namespace std;

int T,n,m;
char d[maxn][maxn];

void init()
{
    scanf("%d%d",&n,&m);
    for (int i=0;i<n;i++)
        for (int j=0;j<m;j++){
            char c;
            do{
                scanf("%c",&c);
            }while (c!='#'&&c!='.');
            d[i][j]=c;
        }
}

bool work()
{
    bool e=true;
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            if (d[i][j]=='#'){
                if (d[i][j+1]=='#'&&d[i+1][j+1]=='#'&&d[i+1][j]=='#'){
                    d[i][j]='/';
                    d[i+1][j]='\\';
                    d[i][j+1]='\\';
                    d[i+1][j+1]='/';
                }else{
                    e=false;
                    break;
                }
            }
        }
        if (e==false)
            break;
    }
    return e;
}

int main()
{
    FILE *cin=freopen("a.txt", "w", stdout);
    scanf("%d",&T);
    for (int tnum=1;tnum<=T;tnum++){
        init();
        printf("Case #%d:\n",tnum);
        if (work()){
            for (int i=0;i<n;i++){
                for (int j=0;j<m;j++)
                    printf("%c",d[i][j]);
                printf("\n");
            }
        }else
            printf("Impossible\n");
    }
}
