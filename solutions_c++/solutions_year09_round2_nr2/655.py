#include <iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#define REP(i,n) for(int i=0;i<(int)(n);++i)
using namespace std;

int main()
{
    int N;
    scanf("%d",&N);
    REP(cc,N){
    char p[1000];
        scanf("%s",p);
        int ok=1;
        for(int i=1;p[i];++i) if(p[i-1]<p[i]) ok=0;
        int n=strlen(p);
        if (!ok){
            next_permutation(p,p+n);
            printf("Case #%d: %s\n",cc+1,p);
        } else {
            int c[10];
            REP(i,10) c[i]=0;
            REP(i,n) c[((int)p[i])-(int)'0' ]++;
            int sm=1;
            REP(i,10) if (i && c[i]){sm=i;break;}
            c[0]++;
            printf("Case #%d: ",cc+1);
            c[sm]--;
            printf("%c",sm+'0');
            REP(i,10) REP(j,c[i]) printf("%c",i+'0');
            printf("\n");
        }
    }

    return 0;
}
