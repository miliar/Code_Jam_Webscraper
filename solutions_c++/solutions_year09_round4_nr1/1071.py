#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
#define PI 3.14159265358979323846264338327950288


#define N 1000
#define INF 99999999999

int mt[100];

int  main()
{

//	freopen("in.txt", "r", stdin);
	int T;
	scanf("%d", &T);
	int count = 0;
	
	while(T-- > 0)
	{
		++count ;
		int n;
		scanf("%d", &n);
		for(int i=0;i<n;++i)
		{
			int c=0;
			for(int j=0;j<n;++j)
			{
				char t;
				do{
					scanf("%c", &t);
				}while(!(t=='0' || t=='1')); 
				if(t == '1')
					c = j+1;
			}
			mt[i+1] = c;
		}
		int sw=0;
		for(int i=1;i<=n;++i)
		{
			int j=0;
			if(mt[i] > i)
			{
				j = i;
				while(mt[j] > i) ++j;
				while(j>i)
				{
					int tmp;
					tmp = mt[j];
					mt[j] = mt[j-1];
					mt[j-1] = tmp;
					--j;
					++sw;
				}
			}
		}
		printf("Case #%d: %d\n", count, sw);
	}

	return 0;
}