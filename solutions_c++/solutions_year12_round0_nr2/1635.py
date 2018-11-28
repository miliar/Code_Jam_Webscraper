#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>

using namespace std;

#define MAXN 110
int main(int argc, char *argv[])
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T, N, S, P, score_sum[MAXN];
    int min[MAXN], max[MAXN];

    scanf("%d", &T);
    for(int i=0;i<T;i++)
    {
        scanf("%d %d %d", &N, &S, &P);

        for(int j=0;j<N;j++)
        {
            scanf("%d", &score_sum[j]);

            if(score_sum[j]%3 == 0){    //3x
                if(score_sum[j] == 0 || score_sum[j] == 30)
                    min[j] = max[j] = score_sum[j]/3;
                else
                    min[j] = score_sum[j]/3, max[j] = score_sum[j]/3+1;
            }else if(score_sum[j]%3 == 1)   //3x+1
                    min[j] = max[j] = score_sum[j]/3+1;
            else{  // 3x+2
                if(score_sum[j] == 29)
                    min[j] = max[j] = 10;
                else
                    min[j] = score_sum[j]/3+1, max[j] = score_sum[j]/3+2;
            }
        }

        unsigned counter = 0;

        for(int j=0;j<N;j++)
        {
            if(min[j] >= P)
                counter++;
            else if(max[j] == P && S > 0)
                counter++, S--;
        }

        printf("Case #%d: %d\n", i+1, counter);
    }
	return 0;
}
