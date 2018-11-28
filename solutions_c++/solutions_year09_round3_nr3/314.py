#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstdio>


using namespace std;

FILE *fp;
int t;
int p,q;

int d[10];

bool flag[104];

int get()
{
	int sum = 0;
	for(int i = 0;i < q;i ++)
	{
		flag[d[i]] = true;
		int pos = d[i] - 1;
		while(pos >= 0 && flag[pos] == false)
			pos --;
		sum += (d[i] - 1) - pos;
		pos = d[i] + 1;
		while(pos < p && flag[pos] == false)
			pos ++;
		sum += pos - (d[i] + 1);
	}
	return sum;
}






int main()
{
	fp = fopen("out.txt","w");
	cin >> t;
	int r = 1;
	while(--t >= 0)
	{
		cin >> p >> q;
		for(int i= 0;i < q;i ++)
		{
			cin >> d[i];
			d[i] --;
		}
		memset(flag,false,sizeof(flag));

		int ans = 1000000000;
		sort(d,d + q);
		do
		{
			memset(flag,false,sizeof(flag));
			int sum = get();
			if(sum < ans)
				ans = sum;
		}while(next_permutation(d,d + q));
		fprintf(fp,"Case #%d: %d\n",r,ans);
		r ++;
	}
		

	return 0;
}