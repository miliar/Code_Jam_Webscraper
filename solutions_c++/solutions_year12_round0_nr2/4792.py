#include<cstdio>
#include<algorithm>
#include<functional>

using namespace std;

int main()
{
    int T;
    scanf("%d\n",&T);
    for(int ii =1; ii<= T; ++ii)
    {
        int N, S, p, C[105];
        scanf("%d %d %d",&N,&S,&p);
        for(int i = 0;i < N; ++i) scanf(" %d",C+i);
        sort(C,C+N);

        int mp  = 0;
        for(int i = N-1; i >= 0; --i)
        {
            if(C[i] >= 29) mp++;
            else if(C[i] == 1 && p <= 1) mp++;
            else if(C[i] == 0 && p == 0) mp++;
            else if(C[i] >= 2 && C[i] <= 28) {
                if((C[i] % 3 == 0) && (C[i] >= 3*p)) mp++;
                else if((C[i] % 3 == 1) && ((C[i]-1)/3 + 1 >= p)) mp++;
                else if((C[i] % 3 == 2) && ((C[i]-2)/3 + 1 >= p)) mp++;
                else if(S > 0){
                    if     ((C[i] % 3 == 0) && ((C[i]/3) + 1 >= p)) {mp++;S--;}
                    else if((C[i] % 3 == 1) && ((C[i]/3) + 1 >= p)) {mp++;S--;}
                    else if((C[i] % 3 == 2) && ((C[i]/3) + 2 >= p)) {mp++;S--;}
                }
            }
        }
        printf("Case #%d: %d\n",ii,mp);
    }
    return 0;
}
