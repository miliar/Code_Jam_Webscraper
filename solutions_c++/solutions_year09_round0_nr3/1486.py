#include <cstdio>
#include <iostream>
#include <memory>
#include <string>

using namespace std;

string s = "welcome to code jam";

char buf[10000];

int mas[1000][1000];

int run(string mes)
{
	memset(mas,0,sizeof(mas));
	for (int i=0; i<mes.size(); i++)
	{
		mas[0][i] = 1;
	}
	for (int i=0; i<s.size(); i++)
	{
		for (int j=0; j<mes.size(); j++)
		{
			mas[i+1][j+1] = mas[i+1][j];
			if (s[i] == mes[j])
			{
				mas[i+1][j+1] = mas[i][j]+mas[i+1][j];
			}
			mas[i+1][j+1] %= 10000;
		}
	}
	return mas[s.size()][mes.size()];
}

int main()
{
	//s = "ab";
	int N;
	scanf("%d", &N);
	cin.getline(buf, 10000);
	for (int n=0; n<N; n++)
	{
		cin.getline(buf, 10000);
		int res = run(buf);
		printf("Case #%d: %04d\n", n+1, res);
	}

	return 0;
}