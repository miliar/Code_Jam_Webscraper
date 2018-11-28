#include<cstdio>
#include<cstring>

void swap(int &a , int &b)
{
	int temp = a;
	a = b;
	b = temp;
}

bool judge(int x , int y)
{
	if(x > y) swap(x , y);
	int num = 0;
	while(x != 0 && y / x == 1)
	{
		num ++;
		y = y % x;
		swap(x , y);
	}
	if(num % 2 == 0) return true;
	else return false;
}

int main()
{
//	freopen("C-small-attempt0.in.txt" , "r" , stdin);
//	freopen("1.txt" , "w" , stdout);
	int t;
	scanf("%d" , &t);
	int p;
	for(p = 1;p <= t;p++)
	{
		int num = 0;
		int a1 , a2 , b1 , b2;
		scanf("%d%d%d%d" , &a1 , &a2 , &b1 , &b2);
		int i , j;
		for(i = a1;i <= a2;i++)
			for(j = b1;j <= b2;j++)
				if(judge(i , j)) num++;
		printf("Case #%d: %d\n" , p , num);
	}
	return 0;
}
