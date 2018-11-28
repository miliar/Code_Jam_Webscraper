#include <iostream>
#include <string.h>
#include <cstdio>
#include <cstdlib>

using namespace std;

int FuHao[45];
char str[45];
int l;


__int64 Calculate()
{
	__int64 result = 0;
	__int64 QianMian = 0;
	int QianMianFuHao = 1;	
	int i;
	QianMian = str[0] - '0';
	for(i = 1; i < l; i++)
	{
		if(FuHao[i - 1] == 0)
		{
			QianMian = QianMian * 10 + str[i] - '0';
		}
		else
		{
			if(QianMianFuHao == 1)
				result = result + QianMian;
			else
				result = result - QianMian;
			QianMianFuHao = FuHao[i - 1];
			QianMian = str[i] - '0';
		}
	}
	if(QianMianFuHao == 1)
		result = result + QianMian;
	else
		result = result - QianMian;
	return result;
}

int main()
{
	int numCase;
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i, j, k;

	__int64 sum;

	scanf("%d", &numCase);
	gets(str);
	for(int cases = 0; cases < numCase; cases++)
	{
		gets(str);
		l = strlen(str);
		sum = 0;
		memset(FuHao, 0, sizeof(FuHao));
		
		while(1)
		{

			__int64 result;
			if(l == 1)
				result = str[0] - '0';
			else
				result = Calculate();
			if(result & 1 == 0 || result % 3 == 0 || result % 5 == 0 || result % 7 == 0)
				sum++;
			i = l - 2;
			while(i >= 0)
			{
				FuHao[i]++;
				if(FuHao[i] <= 2)
					break;
				FuHao[i] = 0;
				i--;
			}
			if(i < 0)
				break;
		}

		cout << "Case #" << cases + 1 << ": " << sum << endl;
	}

	return 0;
}