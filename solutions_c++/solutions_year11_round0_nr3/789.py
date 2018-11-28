#include<vector>
#include<algorithm>
#include<stdio.h>
#include<map>
using namespace std;

int a[1100];
int main()
    {
        freopen("C-large.in","r",stdin);
        freopen("CCC.txt","w",stdout);
        int T;
        scanf("%d",&T);

        for(int ii = 1 ;ii<=T;ii++)
            {
                int n ;
                scanf("%d",&n);
                for(int i = 0 ; i < n ;i++)
                    scanf("%d",&a[i]);
                sort(a , a+ n );
                int xo = 0 , sum = -a[0];
                for(int i =  0; i < n ;i++)
                    {xo^=a[i];sum+=a[i];}
                printf("Case #%d: ",ii);
                if(xo)
                    {
                        printf("NO\n");
                        continue;
                    }
                printf("%d\n",sum);

            }
        return 0;
    }
