#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
#define MAX 105
using namespace std;

int N;
char grid[MAX][MAX];
double WP,OWP,OOWP;

double calcWP(int p)
{
	double num=0.0,den=0.0;
	for(int i=0;i<N;i++)
	{
		num+=(grid[p][i]=='1');
		den+=(grid[p][i]!='.');
	}
	return num/den;
}

double calcOWP(int p)
{
	double sum=0.0,cnt=0.0;
	for(int i=0;i<N;i++)
	{
		if(grid[p][i]=='.') continue;
		char tmp=grid[i][p];
		grid[i][p]='.';
		sum+=calcWP(i);
		cnt++;
		grid[i][p]=tmp;
	}
	return sum/cnt;
}

double calcOOWP(int p)
{
	double sum=0.0,cnt=0.0;
	for(int i=0;i<N;i++)
	{
		if(grid[p][i]=='.') continue;
		sum+=calcOWP(i);
		cnt++;
	}
	return sum/cnt;
}
		
int main()
{
	int cases;
	
	scanf("%d",&cases);
	
	for(int iD=1;iD<=cases;iD++)
	{
		printf("Case #%d:\n",iD);
		scanf("%d",&N);

		for(int i=0;i<N;i++) scanf("%s",grid[i]);
		for(int i=0;i<N;i++)
			printf("%.12lf\n",0.25*calcWP(i)+0.50*calcOWP(i)+0.25*calcOOWP(i));
	}

	return 0;
}


