#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
#define M 5100

int n,D,L;
string data[M];

bool table[50][30];

void read_data()
{
	cin >> L >> n >> D;
	int i;
	for (i=1;i<=n;i++) cin >> data[i];
}
string buf;

void make_comp()
{
	int i,pnt = 0;
	for (i=0;i<L;i++)
	{
		if (buf[pnt] == '(')
		{
			pnt++;
			while (buf[pnt] != ')') {table[i][buf[pnt] - 'a'] = true;pnt++;}
			pnt++;
		}
		else
		{
			table[i][buf[pnt] - 'a'] = true; pnt++;
		}
	}
}

void show_ans()
{
	int i,j,cnt = 0;
	bool flag;
	for (i=1;i<=n;i++)
	{
		flag = true;
		for (j=0;j<L;j++) if (!table[j][data[i][j] - 'a'])
		{
			flag = false;
			break;
		}
		if (flag) cnt++;
	}
	printf("%d\n",cnt);
}

void work_ans()
{
	int i;
	for (i=1;i<=D;i++)
	{
		memset(table,false,sizeof(table));
		cin >> buf;
		make_comp();
		printf("Case #%d: ",i);
		show_ans();
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A_large.out","w",stdout);
	read_data();
	work_ans();
	return 0;
}
