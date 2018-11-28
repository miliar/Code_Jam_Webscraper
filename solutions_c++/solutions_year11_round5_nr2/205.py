#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;


int TRIALS;
int cards[10001];
int scount[1000];

void trial(int T)
{
	printf("Case #%d: ", T);
        int N;
        int s1 = 0; int s2 = 0;
        scanf("%d", &N);
        if (N == 0){printf("0\n"); return;}
        memset(cards, 0, sizeof(cards));
        memset(scount, 0, sizeof(scount));
        for (int i = 0; i < N; i++)
        {
            int card;
            scanf("%d", &card);
            cards[card-1]++;
        }
        int sc = 0;
        int ans = 1000000;
        for (int i = 0; i < 10001; i++)
        {
            while (sc > cards[i])
            {
                int len = i - scount[s1++];
                if (ans > len) ans = len;
                sc--;
            }
            while (sc < cards[i])
            {
                scount[s2++] = i;
                sc++;
            }
        }
        printf("%d\n", ans);
	
}

int main(int argc, char* argv[])
{
	scanf("%d", &TRIALS);
	for (int T = 1; T <= TRIALS; T++)
	{
		trial(T);
	}
	
	return 0;
}