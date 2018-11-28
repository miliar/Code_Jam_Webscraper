#include <iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)(n);++i)

int main()
{
    int n,T;
    scanf("%d",&T);

    REP(cc,T) {
         vector<int> a;
        scanf("%d",&n);
        int b;
        REP(i,n) {
            b=0;
             char p[100];
             scanf("%s",p);
             REP(j,n) if(p[j]=='1') b=j;
             a.push_back(b);
      }

        int ws=0;
//REP(i,n) printf("%d\n",a[i]);

        int i=0;
        while(i<n) {
           // printf("*\n");
           // REP(i,n) printf("%d\n",a[i]);
           if(a[i]<=i) {++i;continue;}
                    int j=i+1;
                    while(j<n && a[j]>i )j++;
                    while(j>i){
                        ws++;swap(a[j],a[j-1]);--j;
                       // printf("-------\n");
                       // REP(x,n) printf("%d\n",a[x]);

                        }
    }
    printf("Case #%d: %d\n",cc+1,ws);
    }

    return 0;
}
