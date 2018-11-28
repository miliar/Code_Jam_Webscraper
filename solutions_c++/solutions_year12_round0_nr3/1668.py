#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<algorithm>

#define MAXN 2001000

using namespace std;

bool visited[MAXN];
unsigned power_ten[8] = {0, 1, 10, 100, 1000, 10000, 100000, 1000000};

int move_time(int num)
{ return log10((double)num);}

int move(int num, int digit_cnt)
{ return num/10 + ( num%10 * power_ten[digit_cnt] ); }

int main(int argc, char *argv[])
{
    //freopen("C-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);

    int T, A, B;

    scanf("%d", &T);

    for(int i=0;i<T;i++)
    {
        scanf("%d %d", &A, &B);

        memset(visited, false, sizeof(visited));

        int counter = 0;
        int move_t = move_time(A);

        vector< pair<int, int> > V;

        for(int j=A;j<=B;j++)
        {
            if(visited[j] == false)
            {
                int tmp_cnt = 1;
                int tmp_value = j;

                visited[j] = true;

                for(int k=0;k<move_t;k++)
                {
                    int d = tmp_value%10;
                    tmp_value = move(tmp_value, move_t+1);

                    // invalid number
                    if( d == 0 || tmp_value > B || tmp_value < A || tmp_value <= j)
                        continue;

                    // unvisitted number
                    if(!visited[tmp_value])
                        tmp_cnt++, visited[tmp_value] = true;
                }
                counter += tmp_cnt * (tmp_cnt-1) / 2;
            }
        }
        printf("Case #%d: %d\n", i+1, counter);
    }
	return 0;
}
