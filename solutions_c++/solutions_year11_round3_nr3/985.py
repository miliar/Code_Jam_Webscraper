#include<stdio.h>

int main(){

    int t,n,l,h;
    unsigned long long ans,note[10001];
    char cannot=0;
    scanf("%d",&t);
    for(int casenum=1;casenum<=t;++casenum)
    {
        scanf("%d%d%d",&n,&l,&h);
        for(int i=0;i<n;i++)
            scanf("%llu",&note[i]);

        for(ans=l;ans<=h;ans++){
            int j=0;
//            printf("ans=%d\n",ans);
            for(;j<n;j++){
                if(note[j]>ans&&note[j]/ans*ans!=note[j]){
//                    printf("/*=%llu\n",note[j]/ans*ans);
//                    printf("%llu\n",note[j]);
                    break;
                }
                else
                    if(note[j]<ans&&ans/note[j]*note[j]!=ans){
//                        printf("%llu\n\n",note[j]);
                        break;
                    }
            }
            if(j==n)
                break;
        }


        if(ans>h)
            printf("Case #%d: NO\n",casenum);
        else
            printf("Case #%d: %llu\n",casenum,ans);

    }

    return 0;
}
