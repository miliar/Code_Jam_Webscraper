#include<iostream>
using namespace std;
int main(void)
{
    FILE *fin = fopen("C-small-attempt0.in","r");
    FILE *fout = fopen("C-small-attempt0.out","w");
    
    int l,alp[256][10]={0};
    char s[601]="welcome to code jam";
    for(int i=0;i<19;i++){
        alp[s[i]][++alp[s[i]][0]]=i+1;
    }    
    fscanf(fin,"%d ",&l);
    for(int cas=1;cas<=l;cas++){
        fgets(s,600,fin);
        int ans[20]={1,0};
        for(int i=0;s[i]!=0;i++){
            for(int j=1;j<=alp[s[i]][0];j++){
                //printf("%d %d\n",i,alp[s[i]][j]);
                ans[alp[s[i]][j]]+=ans[alp[s[i]][j]-1];
                if(ans[alp[s[i]][j]]>10000)
                    ans[alp[s[i]][j]]-=10000;
            }    
        }    
        fprintf(fout,"Case #%d: %d%d%d%d\n",cas,ans[19]/1000,ans[19]/100%10,ans[19]/10%10,ans[19]%10);
    }    
    //system("pause");
    return 0;
}    
