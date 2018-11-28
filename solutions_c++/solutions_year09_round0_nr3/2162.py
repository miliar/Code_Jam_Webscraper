#include <cstdio>
#include <algorithm>
using namespace std;
int n;
char str[]="welcome to code jam";
char st[1000];
int pos[256][510];
int mat[256][510];
int len[256];
int main()
{
    freopen("F:\\C-large.in", "r", stdin);
	freopen("F:\\c-large.out", "w", stdout);
    scanf("%d",&n);
    gets(st);
    for(int p=1;p<=n;p++){
        gets(st);
        memset(len,0,sizeof(len));
        for(int i=0;st[i]!='\0';i++){
            pos[st[i]][len[st[i]]++]=i;
        }
        for(int i=0;i<len[str[18]];i++)
            mat[str[18]][pos[str[18]][i]]=1;
        for(int i=17;i>=0;i--){
            for(int j=len[str[i]]-1;j>=0;j--){
                int ppos=lower_bound(&pos[str[i+1]][0],&pos[str[i+1]][len[str[i+1]]],pos[str[i]][j])-pos[str[i+1]];
                mat[str[i]][pos[str[i]][j]]=0;
                for(int k=ppos;k<len[str[i+1]];k++){
                    mat[str[i]][pos[str[i]][j]]=(mat[str[i+1]][pos[str[i+1]][k]]+mat[str[i]][pos[str[i]][j]])%10000;
                }
            }
        }
        int ans=0;
        for(int i=0;i<len[str[0]];i++){
            ans=(ans+mat[str[0]][pos[str[0]][i]])%10000;
        }
        printf("Case #%d: %04d\n",p,ans);
    }
}
