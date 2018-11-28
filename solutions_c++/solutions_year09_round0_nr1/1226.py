#include<iostream>
#include<cstring>
char dict[30000][100],s[30000];
int ivald[30000];
int h[30000];
main(){
    int l,d,n,i,j,sl,k,r=0,cnt,ii,f;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&l);
    scanf("%d",&d);
    scanf("%d",&n);
    for(i=0;i<d;i++){
        scanf("%s",dict[i]);
    }
    for(i=1;i<=n;i++){
        scanf("%s",s);
        k = 0;
        cnt = 0;
        sl = strlen(s);
        for(j=0;j<l;j++){
            r++;
            if(s[k]=='('){
                while(s[++k]!=')'){
                    h[s[k]]=r;
                }
            }else{
                h[s[k]]=r;
            }
            k++;
            for(ii=0;ii<d;ii++){
                if(h[dict[ii][j]]!=r){
                    ivald[ii]=i;
                }
            }
        }
        for(ii=0;ii<d;ii++){
            if(ivald[ii]!=i){
                cnt++;
            }
        }
        printf("Case #%d: %d\n",i,cnt);
    }
}
