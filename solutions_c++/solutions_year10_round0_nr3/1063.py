#include<stdio.h>

int T, C;
int Times, Capacity;
int n;
int a[1000];
int Next[1000];
int Size[1000];
int Check[1000];
int m;
int starter;
long long ret;
long long loc_money;

int Go(int l1, int flag)
{
	if(Check[l1] == flag) return l1;
	if(Times > 0)
	{
		Times--;
		ret += Size[l1];
	}
	Check[l1] = flag;
	return Go(Next[l1], flag);
}

int main(void)
{
	int l1, l2;

	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);

	scanf("%d",&T);
	for(C=1;C<=T;C++)
	{
		scanf("%d %d %d",&Times,&Capacity,&n);
		for(l1=0;l1<n;l1++) scanf("%d",&a[l1]);

		for(l1=0;l1<n;l1++) Check[l1] = 0;

		for(l1=0;l1<n;l1++)
		{
			int curr = 0;
			for(l2=0;l2<n;l2++)
			{
				curr += a[(l1 + l2) % n];
				if(curr <= Capacity)
				{
					Next[l1] = (l1 + l2 + 1) % n;
					Size[l1] = curr;
				}
			}
		}

		ret = 0;

		Go(starter = Go(0, 1), 2);
		m = 0;
		loc_money = 0;
		for(l1=0;l1<n;l1++)
		{
			if(Check[l1] == 2)
			{
				m++;
				loc_money += Size[l1];
			}
		}

		int factor = Times / m;
		Times %= m;
		ret += (long long)factor * loc_money;
		Go(starter, 3);

		printf("Case #%d: %Ld\n",C,ret);
	}
	return 0;
}