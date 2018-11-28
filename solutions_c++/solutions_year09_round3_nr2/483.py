#include<iostream>
#include<cmath>
#include<cstring>
#include<fstream>
#define MAX 1000
using namespace std;
ifstream in("data.in");
ofstream out("data.out");
FILE *write1;
class contest
{
	double x[1000];	
	double y[1000];
	double z[1000];
	double xv[1000];	
	double yv[1000];
	double zv[1000];
	int N;
	double x0,x1;
	double y0, y1;
	double z0, z1;
	double ans;
	double A,B,C;
public:
	contest();
	void process();
};
contest::contest()
{
	in>>N;
	for(int i = 1;i <= N;i++)
	{
		in>>x[i]>>y[i]>>z[i]>>xv[i]>>yv[i]>>zv[i];
	}
	double sumx;
	double sumy;
	double sumz;
	sumx = 0;
	sumy = 0;
	sumz = 0;
	for(int i = 1;i <= N;i++)	
	{
		sumx += x[i];
		sumy += y[i];
		sumz += z[i];
	}
	x0 = sumx/(double)N;
	y0 = sumy/(double)N;
	z0 = sumz/(double)N;
	sumx = 0;
	sumy = 0;
	sumz = 0;
	for(int i = 1;i <= N;i++)	
	{
		sumx += xv[i];
		sumy += yv[i];
		sumz += zv[i];
	}
	x1 = sumx/(double)N;
	y1 = sumy/(double)N;
	z1 = sumz/(double)N;
	 A = x1 * x1 + y1 * y1 + z1 * z1;
	 B = x0 * x1 + y0 * y1 + z0 * z1;
	C = x0 * x0 + y0 * y0 + z0 * z0;
	if(A == 0)
	{
		printf("%.9f %.9f\n", sqrt(abs(C)), 0.0);
		fprintf(write1, "%.9f %.9f\n", sqrt(abs(C)), 0.0);
	}
	else
	{
	if(B >= 0)
	{
		printf("%.9f %.9f\n", sqrt(abs(C)), 0.0);
		fprintf(write1, "%.9f %.9f\n", sqrt(abs(C)), 0.0);
	}
	else
	{
		printf("%.9f %.9f\n",sqrt(abs(C - B * B /A)), -B/A);
		fprintf(write1, "%.9f %.9f\n",sqrt(abs(C - B * B /A)), -B/A);
	}
	}	
	
}
void contest::process()
{
}
void solve()
{
	class contest myobj;
	myobj.process();
}
int main()
{
	write1 = fopen("data.out","w");
	int t;
	int i = 1;
	in>>t;
	while(i <= t)
	{
		printf("Case #");
		fprintf(write1, "Case #");
		printf("%d: ", i);
		fprintf(write1, "%d: ", i);
		
		//out<<"Case #"<<i<<": ";
		solve();
		i++;
	}
		
	return 0;
}
