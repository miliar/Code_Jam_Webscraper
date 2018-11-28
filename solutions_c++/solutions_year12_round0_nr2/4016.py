#include<stdio.h>

int main(){
    int cases = 0 , n=0 , googler , sur=0 , up=0;
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&cases);
    for(int i=0;i<cases;i++)
    {
        int j=0,ans=0,llimit=0,uplimit=0;
        scanf("%d%d%d",&n,&sur,&up);
        llimit = 3*up-4;
        uplimit = 3*up-2;
        for(j=0; j<n; j++){
             scanf("%d",&googler);
             if(sur>0)
                 if(googler>=up && googler>=llimit && googler<uplimit){ ans++;sur--;}
             if(googler>=up && googler>=uplimit) ans++;
        }
        printf("Case #%d: %d\n",i+1,ans);    
    }         
    
    return 0;    
}
