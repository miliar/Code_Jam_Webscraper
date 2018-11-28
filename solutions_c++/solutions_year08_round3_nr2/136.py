#include <cstdio>
#include <iostream>

using namespace std;

char s[100];
int N;
int res = 0;

long long pp[] = {2,3,5,7};

void calc(int pos, long long val)
{
	if (pos >= N-1)
	{
		for (int i=0; i<4; i++)
		{
			if ((val%pp[i]) == 0)
			{
				res++;
				return;
			}
		}
	}
	for (int i=pos+1; i<N; i++)
	{
		long long cval = 0;
		for (int j=pos+1; j<=i; j++)
		{
			cval *= 10;
			cval += (s[j]-'0');
		}
		calc(i,val+cval);
		calc(i,val-cval);
	}
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int tt=1; tt<=T; tt++)
	{
		cerr<<tt<<endl;
		scanf("%s", s);
		N = strlen(s);
		res = 0;
		
		for (int i=0; i<N; i++)
		{
			long long cval = 0;
			for (int j=0; j<=i; j++)
			{
				cval *= 10;
				cval += (s[j]-'0');
			}
			calc(i, cval);
		}
		printf("Case #%d: %d\n", tt, res);
	}
	return 0;
}