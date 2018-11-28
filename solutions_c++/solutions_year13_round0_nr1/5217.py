#include <stdio.h>
#include <string.h>
#include <stdlib.h>

using namespace std;

int d[10][10];
const int INF=10000;

int init()
{
	int have_point=0;
	char ch;
	memset(d,0,sizeof(d));
	while (getchar()!='\n');
	for (int i=1;i<=4;i++)
	{
		for (int j=1;j<=4;j++)
		{
			ch = getchar();
			if (ch=='.') {
				have_point=1;
				d[i][j]=INF;
			} else if (ch=='X') {
				d[i][j]=-1;
			} else if (ch=='O') {
				d[i][j]=1;
			} else if (ch=='T') {
				d[i][j]=0;
			}
		}
		while (getchar()!='\n');
	}
	//while (getchar()!='\n');
	return have_point;
}

int check_row(int x)
{
	int tot=0;
	for (int i=1;i<=4;i++)
		tot += d[x][i];
	if (tot > INF / 2) return 0;
	if (abs(tot) >=3) return 1;
	return 0;
}

int check_col(int x)
{
	int tot=0;
	for (int i=1;i<=4;i++)
		tot += d[i][x];
	if (tot > INF / 2)  return 0;
	if (abs(tot) >= 3)	return 1;
	return 0;
}

int check_left_right()
{
	int tot=0;
	for (int i=1;i<=4;i++)
		tot += d[i][i];
	if (tot > INF / 2) return 0;
	if (abs(tot) >= 3) return 1;
	return 0;
}

int check_right_left()
{
	int tot=0;
	for (int i=1;i<=4;i++)
		tot += d[5-i][i];
	if (tot > INF / 2) return 0;
	if (abs(tot) >= 3) return 1;
	return 0;
}

int calc()
{
	for (int i=1;i<=4;i++)
	{
		if (check_row(i)==1) return i;
		if (check_col(i)==1) return i+4;
	}

	if (check_left_right()) return 9;
	else if (check_right_left()) return 10;

	return 0;
}

int judge(int status)
{
	if (status <= 4)
		if (d[status][1]==-1 || d[status][2]==-1)
			return 0;
		else
			return 1;
	else if (status <= 8)
		if (d[1][(status-1)%4+1]==-1 || d[2][(status-1)%4+1]==-1)
			return 0;
		else
			return 1;
	else if (status == 9)
		if (d[1][1]==-1 || d[2][2]==-1)
			return 0;
		else
			return 1;
	else
		if (d[4][1]==-1 || d[3][2]==-1)
			return 0;
		else
			return 1;
}

int main()
{
    freopen("/Users/zpl/Documents/Codes/gcj_pre1/A-small-attempt0.in","r",stdin);
    freopen("/Users/zpl/Documents/Codes/gcj_pre1/output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		int have_point,status;
		have_point=init();
		status=calc();
		printf("Case #%d: ",i);
		if (status > 0) {
			if (judge(status)==0)
				printf("X won\n");
			else
				printf("O won\n");
		} else if (have_point)
			printf("Game has not completed\n");
		else printf("Draw\n");
	}
	return 0;
}
