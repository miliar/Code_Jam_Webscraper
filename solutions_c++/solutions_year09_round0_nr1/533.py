#include<iostream>
using namespace std;
char ss[6000][20];
bool p[20][300];
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int l,d,n;
    char s[2000];
    scanf("%d%d%d",&l,&d,&n);
    int i,j,k;
    for(i=0;i<d;i++)
        scanf("%s",ss[i]);
    for(i=0;i<n;i++){
        scanf("%s",s);
        memset(p,0,sizeof(p));
        for(k=0,j=0;j<strlen(s);k++,j++)
            if(s[j]=='(')
                for(j++;s[j]!=')';j++)
                    p[k][s[j]]=1;
            else p[k][s[j]]=1;
        int sum=0,flag;
        for(j=0;j<d;j++){
            flag=1;
            for(k=0;k<l;k++)
                if(!p[k][ss[j][k]]){
                    flag=0; break;
                }
            sum+=flag;
        }
        printf("Case #%d: %d\n",i+1,sum);
    }
    return(0);
}



