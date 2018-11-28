#include <stdio.h>

#define MAX_N	1000
#define min(a,b)	((a)<(b)?(a):(b))

typedef struct {
	int min;	//
	int max;	// apply surprise
} point_t;

int score[MAX_N];
point_t ptarr[MAX_N];

void getScore(int num, point_t *p)
{
	if (num == 0) {
		p->min = p->max = 0;
		return ;
	}

	int min, max;
	int r = num%3;

	switch(r)
	{
	case 0:
		min = num/3;
		max = min+1;
		break;
	case 1:
		min = max = (num/3)+1;
		break;
	case 2:
		min = num/3+1;
		max = min+1;
		break;
	default:
		break;
	}

	p->min = min;
	p->max = max;
}

int main()
{
	int t;

	scanf("%d", &t);
	
	for(int a=0; a<t; a++)
	{
		int ans = 0, N, basep, surp;

		scanf("%d %d %d", &N, &surp, &basep);

		for(int i=0; i<N; i++) 
		{
			scanf("%d", &score[i]);
			getScore(score[i], &ptarr[i]);
		}

		for(int i=0; i<N; i++)
		{
			if (ptarr[i].min >= basep) {
				ans++;
			} else if (ptarr[i].max >= basep) {
				if (surp > 0) {
					ans++; surp--;
				}
			}
		}

		printf("Case #%d: %d\n", a+1, ans);
	}
}
