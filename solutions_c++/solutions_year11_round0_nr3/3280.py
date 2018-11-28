#include <cstdio>
#include <vector>

using namespace std;

vector<int> v;
int x1 = 0, x2 = 0, s=0, n, max_s = -1, x1c=0, x2c=0;

void rek(int i)
{
	if(i == n)
	{
		if(x1 > 0 && x2 > 0 && x1 == x2 && s > max_s)
			max_s = s;
		//printf("i == %d, x1 == %d, x2 == %d, s == %d, max_s = %d\n", i, x1, x2, s, max_s);
	}
	else
	{
		//printf("i == %d; ", i);
		//v[i] -> xor
		
		x1 = x1^v[i];
		x1c++;
		//printf("x1 = %d\n", x1);
		rek(i+1);
		x1 = x1^v[i];
		x1c--;
		
		x2 = x2^v[i];
		x2c++;
		//printf("x2 = %d\n", x2);
		s += v[i];
		rek(i+1);
		s -= v[i];
		x2 = x2^v[i];
		x2c--;
		//printf("koniec i == %d\n", i);
	
	}
}

int main()
{
	int t, c;

	scanf("%d", &t);

	for(int i=1;i<=t;i++)
	{
		scanf("%d", &n);
		//v.clear();
		v.resize(n);
		max_s = -1;
		x1 = 0;
		x2 = 0;
		s = 0;
		x1c = 0;
		x2c = 0;

		for(int j=0;j<n;j++)
		{
			scanf("%d", &v[j]);
		}

		rek(0);

		if(max_s == -1)
			printf("Case #%d: NO\n", i);
		else
			printf("Case #%d: %d\n", i, max_s);
	}
}
