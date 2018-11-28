#include<cstdio>
#include<algorithm>
using namespace std;
main()
{
    int i,j,k,n,T,C=1,s[99],t[99];
    char tmp[99];
    scanf("%d",&T);
    while(T--){
        scanf("%d",&n);
        for(i=0;i<n;i++){
            scanf("%s",tmp);
            for(j=0;tmp[j];j++);
            while(tmp[--j]=='0');
            t[i]=j;
            s[i]=-1;
        }
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                if(i>=t[j] && s[j]<0){
                    s[j]=i;
                    break;
                }
        for(i=k=0;i<n;i++){
            for(j=1;j<n;j++)
                if(s[j-1]>s[j])
                    k++,swap(s[j-1],s[j]);
        }
        printf("Case #%d: %d\n",C++,k);
    }
}
