# include <iostream>
# include <cmath>

using namespace std;

double max(double a, double b)
{return a>b?a:b;}

double min(double a, double b, double c)
{
	double min1 = (a<b?a:b);
	return (min1<c?min1:c);
}

double dis (double x1, double y1, double x2, double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

int main ()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);


	double r[3], x[3], y[3];
	int t, i, j, n;
	cin>>t;
	for (i=0; i<t; ++i)
	{
		cin>>n;
		for (j=0; j<n; ++j)
		{
			cin>>x[j]>>y[j]>>r[j];
		}
		if (n==1)
			cout<<"Case #"<<i+1<<": "<<r[0]<<endl;
		else if (n==2)
		{
			double max = r[0]>r[1]?r[0]:r[1];
			cout<<"Case #"<<i+1<<": "<<max<<endl;
		}
		else
		{
			double d1 = dis(x[0],y[0],x[1],y[1]);
			double d2 = dis(x[0],y[0],x[2],y[2]);
			double d3 = dis(x[1],y[1],x[2],y[2]);
			double min1 = max((d1+r[0]+r[1])/2, r[2]);
			double min2 = max((d2+r[0]+r[2])/2, r[3]);
			double min3 = max((d3+r[1]+r[2])/2, r[0]);
			double ans = min(min1, min2, min3);
			printf("Case #%d: %.6lf\n",i+1,ans);
		}
	}
	return 0;
}



/*

2
3
20 10 2
20 20 2
40 10 3
3
20 10 3
30 10 3
40 10 3


# include <iostream>
using namespace std;

int main()
{
//	freopen("D-large.in","r",stdin);
//	freopen("output.txt","w",stdout);
	int i,j,k,p,ans;
	return 0;
}*/