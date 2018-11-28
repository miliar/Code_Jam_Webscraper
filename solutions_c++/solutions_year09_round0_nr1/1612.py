#include <stdio.h>
#include <string.h>
#define maxd 5000+50
#define maxl 20
char s[maxd][maxl];
char st[50000];
int tag[maxl][26];
int l,d,tn,m,tp;
int ans;
int main(){
    int i,j,k;
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d %d %d",&l,&d,&m);
    for (i=0;i<d;i++) scanf("%s",&s[i]);
    for (tp=1;tp<=m;tp++){
        scanf("%s",&st);
        memset(tag,0,sizeof(tag));
        int left=0,right;
        for (i=0;i<l;i++){
            if (st[left]=='('){
               for (right=left+1;st[right]!=')';right++);
               for (j=left+1;j<right;j++)
                   tag[i][st[j]-'a']++;
            }else{
                  tag[i][st[left]-'a']++;
                  right=left;
            }
            left=right+1;
        }
        ans=0;
        for (i=0;i<d;i++){
            k=1;
            for (j=0;j<l && k;j++)
                if (!tag[j][s[i][j]-'a']) k=0;
            if (k) ans++;
        }
        printf("Case #%d: %d\n",tp,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
