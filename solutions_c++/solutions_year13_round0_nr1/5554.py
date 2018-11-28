#include <iostream>

using namespace std;

char temp[5][5];

void checkr(int &flag1, int &flag2, int &flag3, int &flag4, int now)
{
	int ju1, ju2, ju3, ju4;
	ju1 = ju2 = ju3 = ju4 = 1;
	for(int i = 0; i < 4; ++i)
	{
		if(temp[now][i] == '.')
		{
			ju1 = ju2 = 0;
		}
		else if(temp[now][i] == 'O')
			ju2 = ju4 = 0;
		else if(temp[now][i] == 'X')
			ju1 = ju3 = 0;
	}
	if(ju1)
		flag1 = 1;
	if(ju2)
		flag2 = 1;
	if(ju3)
		flag3 = 1;
	if(ju4)
		flag4 = 1;
}

void checkc(int &flag1, int &flag2, int &flag3, int &flag4, int now)
{
	int ju1, ju2, ju3, ju4;
	ju1 = ju2 = ju3 = ju4 = 1;
	for(int i = 0; i < 4; ++i)
	{
		if(temp[i][now] == '.')
		{
			ju1 = ju2 = 0;
		}
		else if(temp[i][now] == 'O')
			ju2 = ju4 = 0;
		else if(temp[i][now] == 'X')
			ju1 = ju3 = 0;
	}
	if(ju1)
		flag1 = 1;
	if(ju2)
		flag2 = 1;
	if(ju3)
		flag3 = 1;
	if(ju4)
		flag4 = 1;
}

void checkt(int &flag1, int &flag2, int &flag3, int &flag4)
{
	int ju1, ju2, ju3, ju4;
	ju1 = ju2 = ju3 = ju4 = 1;
	for(int i = 0; i < 4; ++i)
	{
		if(temp[i][i] == '.')
		{
			ju1 = ju2 = 0;
		}
		else if(temp[i][i] == 'O')
			ju2 = ju4 = 0;
		else if(temp[i][i] == 'X')
			ju1 = ju3 = 0;
	}
	if(ju1)
		flag1 = 1;
	if(ju2)
		flag2 = 1;
	if(ju3)
		flag3 = 1;
	if(ju4)
		flag4 = 1;
}

void checkft(int &flag1, int &flag2, int &flag3, int &flag4)
{
	int ju1, ju2, ju3, ju4;
	ju1 = ju2 = ju3 = ju4 = 1;
	for(int i = 0; i < 4; ++i)
	{
		if(temp[i][3 - i] == '.')
		{
			ju1 = ju2 = 0;
		}
		else if(temp[i][3 - i] == 'O')
			ju2 = ju4 = 0;
		else if(temp[i][3 - i] == 'X')
			ju1 = ju3 = 0;
	}
	if(ju1)
		flag1 = 1;
	if(ju2)
		flag2 = 1;
	if(ju3)
		flag3 = 1;
	if(ju4)
		flag4 = 1;
}

int main(void)
{
	int t;
	freopen("D:\A-small-attempt1.in", "r", stdin);
	freopen("D:\A-ans.out", "w", stdout);
	int ca = 0;
	scanf("%d", &t);
	while(t--)
	{
		for(int i = 0; i < 4; ++i)
		{
			scanf("%s", temp[i]);
		}
		int flag1, flag2, flag3, flag4;
		flag1 = flag2 = flag3 = flag4 = 0;
		for(int i = 0; i < 4; ++i)
		{
			checkr(flag1, flag2, flag3, flag4, i);
			checkc(flag1, flag2, flag3, flag4, i);
			if(i == 0)
			{
				checkt(flag1, flag2, flag3, flag4);
			}
			if(i == 3)
				checkft(flag1, flag2, flag3, flag4);
		}
		printf("Case #%d: ", ++ca);
		if(flag1 && flag2)
			printf("Draw");
		else if(flag1 && !flag2)
			printf("O won");
		else if(!flag1 && flag2)
			printf("X won");
		else if(flag3 || flag4)
			printf("Game has not completed");
		else
			printf("Draw");
		printf("\n");
	}
	return 0;
}