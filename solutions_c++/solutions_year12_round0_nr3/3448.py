#include<cstdio>

using namespace std;

int len(int num)
{
	int ret = 0;
	while(num > 0)
	{
		num /= 10;
		ret++;
	}
	return ret;
}
int pow(int l){
	int ret = 1;
	for(int i = 0;i < l;i++)
	{
		ret *= 10;
	}
	return ret;
}
int brother(int low, int high,int num)
{
	int ret = 0;
	int leng = len(num);
	int temp = num;
	for(int i = 1;i < leng; i++)
	{
		int part1 = num % 10;
		int part2 = num / 10;
		num = part1 * pow(leng-1) + part2;
		if(num >= low && num <= high && num != temp)
		{
			if(leng % 2 == 1)
				ret++;
			else if(num % 101 != 0 && num % 10101 != 0 && num % 1001 != 0)
				ret++;
		}
	}
	if(leng % 2 == 0)
	{
		if(temp % 101 == 0 || temp % 10101 == 0)
		{
			int part1 = temp % 10;
			int part2 = temp / 10;
			num = part1 * pow(leng-1) + part2;
			if(num >= low && num <= high && num != temp) 
			ret++;
		}
		else if(temp % 1001 == 0){
			int part1 = temp % 10;
			int part2 = temp / 10;
			num = part1 * pow(leng-1) + part2;
			if(num >= low && num <= high && num != temp) 
			ret++;
			part1 = num % 10;
			part2 = num / 10;
			num = part1 * pow(leng-1) + part2;
			if(num >= low && num <= high && num != temp) 
			ret++;
		}
	}
	return ret;
}
int main()
{
//	freopen("c.txt", "r", stdin);
//	freopen("c.out", "w", stdout);
	int n;
	int l,r;
	scanf("%d\n", &n);
	for(int i = 1;i <= n;i++)
	{
		int ansi = 0;
		scanf("%d %d\n", &l, &r);
		for(int j = l; j <= r; j++)
		{
			ansi += brother(l,r,j);
		//	if(brother(l,r,j) > 0)
		//		printf("%d %d\n", j, brother(l,r,j));
		}
		ansi /= 2;
		printf("Case #%d: %d\n", i, ansi);
	}
	return 0;
}
