#include <iostream>

using namespace std;

int a[30], cc;
int cnt[10];

int main()
{
    int i, j, k, ca;
    int n;
    
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    char ss[50];
    scanf("%d",&ca);
    getchar();
    for(int cs=1;cs<=ca;cs++)
    {
        printf("Case #%d: ",cs);
        gets(ss);
        //puts(ss);
        for(i=0;i<strlen(ss);i++)
            a[i+1]=ss[i]-'0';
        
        cc = strlen(ss);
        
        
        if(!next_permutation(a+1,a+cc+1)){
            sort(a+1,a+cc+1);
            i=1;
            while(a[i]==0)i++;
            printf("%d0",a[i]);
            for(j=1;j<i;j++)printf("0");
            for(++i;i<=cc;i++) printf("%d",a[i]);
            printf("\n");
        }
        else{
            for(i=1;i<=cc;i++)
                printf("%d",a[i]);
            printf("\n");
        }
    }
    return 0;
}
        
            
                
            
            
        
