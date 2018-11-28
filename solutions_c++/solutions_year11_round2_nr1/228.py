#include <iostream>
using namespace std;
#define M 110

double ans[M];
double WP[M],OWP[M],OOWP[M];
char data[M][M];
int n;

void read_data()
{
	cin >> n;
	int i,j;
	for (i=1;i<=n;i++)
		for (j=1;j<=n;j++) cin >> data[i][j];
}

double calcWP(int s)
{
	double a = 0,b = 0;
	int i;
	for (i=1;i<=n;i++)
	{
		if (data[s][i] != '.') a++;
		if (data[s][i] == '1') b++;
	}
	return b / a;
}

double calcOWP(int s)
{
	char __data[M][M];
	memcpy(__data,data,sizeof(data));
	int i;
	for (i=1;i<=n;i++) data[s][i] = data[i][s] = '.';

	int cnt = 0;
	double sum = 0;
	for (i=1;i<=n;i++) if (__data[s][i] != '.')
	{
		cnt++;
		sum += calcWP(i);
	}
	memcpy(data,__data,sizeof(data));
	return sum / cnt;
}

double calcOOWP(int s)
{
	int cnt = 0;
	double sum = 0;
	int i;
	for (i=1;i<=n;i++) if (data[s][i] != '.')
	{
		cnt++;
		sum += OWP[i];
	}
	return sum / cnt;
}

void work_ans()
{
	int i;
	for (i=1;i<=n;i++) WP[i] = calcWP(i);
	for (i=1;i<=n;i++) OWP[i] = calcOWP(i);
	for (i=1;i<=n;i++) OOWP[i] = calcOOWP(i);
	for (i=1;i<=n;i++) ans[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
}

void show_ans()
{
	int i;
	for (i=1;i<=n;i++) printf("%.10lf\n",ans[i]);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,i;
	cin >> t;
	for (i=1;i<=t;i++)
	{
		printf("Case #%d:\n",i);
		read_data();
		work_ans();
		show_ans();
	}
	return 0;
}
