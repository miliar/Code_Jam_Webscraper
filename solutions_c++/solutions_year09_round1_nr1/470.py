#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;

int used[20000], G;

bool test(int num, int base)
{
	int i, tmp = 0, d;
	//printf("%d %d\n", num, base);
	while( true )
	{
		tmp = 0;
		while( num )
		{
			d = num % base;
			num /= base;
			tmp += d*d;
		}
		//printf("%d\n", tmp);
		//system("pause");
		if(tmp == 1)return true;
		if(used[tmp] == G)break;
		used[tmp] = G;
		num = tmp;
	}
	return false;
}

int main()
{
	int cas, T;
	int i, j, n, x[100];
	char line[2000];
	
	scanf("%d", &T);
	
	for(cas = 1; cas <= T; cas ++)
	{
		scanf("\n");
		gets(line);
		bool flag = false;
		n = 0;

		for(i = 0; line[i] != '\0'; i ++)
		{
			if(!flag){
				if(line[i] >= '0' && line[i] <= '9')
				{
					flag = true;
					x[n] = line[i] - '0';
				}
			}
			else {
				if(line[i] >= '0' && line[i] <= '9')
				{
					x[n] = x[n]*10 + line[i] - '0';
				}
				else {
					flag = false;
					n ++;
				}
			}
		}
		if(flag)n ++;
		//for(i = 0; i < n; i ++)printf("x[%d] = %d\n", i, x[i]);
		for(i = 2; ; i ++)
		{
			for(j = 0; j < n; j ++)
			{
				G ++;
				if(!test(i, x[j]))break;
			}
			if(j == n)break;
		}
		printf("Case #%d: %d\n", cas, i);
	}
	return 0;
}
