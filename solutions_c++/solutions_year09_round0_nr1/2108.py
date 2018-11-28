#include <cstdio>
#include <algorithm>
using namespace std;
int L,D,N;
char mat[5050][20];
char mmat[510];
char str[20][30];
int tot;
int main()
{
    freopen("F:\\A-large.in", "r", stdin);
	freopen("F:\\A-large.out", "w", stdout);
    scanf("%d%d%d",&L,&D,&N);
    for(int i=0;i<D;i++){
        scanf("%s",mat[i]);
    }
    for(int p=1;p<=N;p++){
        scanf("%s",mmat);
        tot=0;
        for(int i=0;mmat[i]!='\0';){
            if(mmat[i]=='('){
                int cnt=0;
                int tot2=1;
                while(mmat[++i]!=')'){
                    str[tot][tot2++]=mmat[i];
                }
                ++i;
                str[tot++][0]=tot2;
            }
            else {
                str[tot][0]=2;
                str[tot++][1]=mmat[i++];
            }
        }

        int ans=0;
        for(int i=0;i<D;i++){
            int cnt=0;
            for(int j=0;j<L;j++){
                bool flag=false;
                for(int k=1;k<str[j][0];k++){
                    if(mat[i][j]==str[j][k]){
                        flag=true;
                        break;
                    }
                }
                if(flag)
                    ++cnt;
                else
                    break;
            }
            if(cnt==L)
                ++ans;
        }
        printf("Case #%d: %d\n",p,ans);
    }
}
