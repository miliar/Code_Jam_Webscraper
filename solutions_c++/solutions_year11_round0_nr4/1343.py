#include<iostream>
using namespace std;
int main()
{
    int T, cs = 0;
    int i, N;
    freopen("D_L.in", "r", stdin);
    freopen("D_L.out", "w", stdout); 
    scanf("%d", &T);
    while(T--)
    {
        scanf("%d", &N);
        int a, j = 0;
        for(i = 1; i <= N; ++i)
        {
           scanf("%d", &a);
           if(a == i) ++j;
        }
        printf("Case #%d: %.6lf\n", ++cs, (N-j)*1.0);
    }
}
