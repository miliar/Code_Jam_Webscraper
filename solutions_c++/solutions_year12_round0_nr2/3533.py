#include <iostream>
#include <algorithm>

using namespace std;

// Google Code Jame 2012 Qualification Round

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, N, S, P;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		scanf("%d %d %d", &N, &S, &P);
		int cnt=0;
		for(int n=0; n<N; n++)
		{
			int total;
			scanf("%d", &total);
			int a, b, c; //The scores given by the judges. Let a always be the largest one.
			a = total/3 + total%3;
			b = c = total/3;
			if(a>P || a==P && a-b!=2 || (a==P && a-b==2 || a==b && a==P-1 && a>0) && --S>=0)
				cnt++;
		}
		printf("Case #%d: %d\n", t, cnt);
	}
	return 0;
}