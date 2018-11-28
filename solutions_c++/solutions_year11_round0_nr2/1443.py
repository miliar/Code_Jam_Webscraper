#include<iostream>
#include<stdio.h>
#include<map>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
using namespace std;

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t,C,D,n,i,k,j,ct,cob[300][300];
    bool df[300][300],flag;
    char s[1000],ans[1000];
    scanf("%d",&t);
    for(ct=1;ct<=t;ct++) {
        memset(cob,0,sizeof(cob));
        memset(df,0,sizeof(df));
        scanf("%d",&C);
        for(i=0;i<C;i++) {
            scanf("%s",s);
            cob[s[0]][s[1]]=cob[s[1]][s[0]]=s[2];
        }
        scanf("%d",&D);
        for(i=0;i<D;i++) {
            scanf("%s",s);
            df[s[0]-'A'][s[1]-'A']=df[s[1]-'A'][s[0]-'A']=1;
        }
        scanf("%d",&n);
        scanf("%s",s);
        ans[0]=s[0];
        k=1;
        for(i=1;i<n;i++) {
            if(cob[ans[k-1]][s[i]]!=0) {
                ans[k-1]=cob[ans[k-1]][s[i]];
            }
            else {
                flag=1;
                for(j=0;j<k;j++) {
                    if(df[ans[j]-'A'][s[i]-'A']) {
                        k=0;
                        flag=0;
                        break;
                    }
                }
                if(flag) {
                    ans[k++]=s[i];
                }
            }
        }
        printf("Case #%d: [",ct);
        if(k!=0) {
            for(i=0;i<k-1;i++) printf("%c, ",ans[i]);
            printf("%c",ans[k-1]);
        }
        printf("]\n");
    }
    return 0;
}
