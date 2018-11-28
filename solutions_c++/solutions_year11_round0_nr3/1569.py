#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int main(){
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    
    int T,t,i,temp,N,C[1005];
    scanf("%d",&T);
    for (t=1;t<=T;t++){
        scanf("%d",&N);
        for(i=0;i<N;i++)
           scanf("%d",&C[i]);
        sort(C,C+N);

        temp=0;
        for (i=0;i<N;i++)
            temp=temp^C[i];
        printf("Case #%d: ",t);
        if (temp!=0) printf("NO\n");
        else
        {
            temp=0;
            for (i=1;i<N;i++)
                temp+=C[i];
            printf("%d\n",temp);
        }
    }
    
    fclose(stdin);
    fclose(stdout);
    return 0;
}
