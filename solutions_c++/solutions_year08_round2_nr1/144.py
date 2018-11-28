#include<iostream>
#include<vector>



using namespace std;

typedef unsigned long UL;
typedef signed long SL;
typedef unsigned short US;
typedef signed short SS;

typedef unsigned long long ULL;

typedef pair<ULL, ULL> point;

const UL max_n=100000;

ULL Q[max_n+1][4][3][3];

int main()
{
	UL tests;
	cin>>tests;
	for(UL tt=1; tt<=tests; ++tt)
	{
		UL n;
		ULL A, B, C, D, x0, y0, M;
		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		vector<point> p;
		ULL X=x0, Y=y0;
		p.push_back(point(X, Y));
		for(UL i=0; i<n-1; ++i)
		{
			X=(A*X + B)%M;
			Y=(C*Y + D)%M;
			p.push_back(point(X,Y));
		}
		for(UL m1=0; m1<3; ++m1)
			for(UL m2=0; m2<3; ++m2)
		{
				for(UL sz=0; sz<=3; ++sz)
					Q[0][sz][m1][m2]=(sz==0 && m1==0 && m2==0);
				for(UL i=1; i<=n; ++i)
					Q[i][0][m1][m2]=(m1==0 && m2==0);
		}
		for(UL i=1; i<=n; ++i)
			for(UL sz=1; sz<=3; ++sz)
				for(UL m1=0; m1<3; ++m1)
					for(UL m2=0; m2<3; ++m2)
					{
						const ULL x=p[i-1].first, y=p[i-1].second;
//						Q[i][sz][m1][m2]=Q[i-1][sz][m1][m2] + Q[i-1][sz-1][((m1+3*(x/3)) - x)%3][((m2+3*(y/3)) - y)%3];
						Q[i][sz][m1][m2]=Q[i-1][sz][m1][m2] + Q[i-1][sz-1][(m1+(3-(x%3)))%3][(m2+(3-(y%3)))%3];
					}
		cout<<"Case #"<<tt<<": "<<Q[n][3][0][0]<<'\n';
	}
}
