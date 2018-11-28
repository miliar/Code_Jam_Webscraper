#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
using namespace std;

double p[100009];

inline void Init()
{
	freopen("A-small-attempt4.in","r",stdin);
	freopen("A-small.out","w",stdout);
}

int main(void)
{
	Init();
	int i,j;
	int T,cases;
	int A,B;
	scanf("%d",&cases);
	for(T=1;T<=cases;T++)
	{
		scanf("%d %d",&A,&B);
		for(i=1;i<=A;i++)
		{
			scanf("%lf",&p[i]);
		}
		double ans;
		set<double> s;
		if(A==1)
		{
			ans = p[1]*(B-A+1) + (1-p[1])*(B-A+1 + B+1);
			s.insert(ans);
			s.insert(1+B+1);
			s.insert(2+B+1);
			s.insert(1+B+1);
		}
		else if(A==2)
		{
			ans = p[1]*p[2]*(B-A+1) + (1-p[1]*p[2])*(B-A+1+B+1);
			s.insert(ans);
			ans = p[1]*(1+B-(A-1)+1) + (1-p[1])*(1+B-(A-1)+1+B+1);
			s.insert(ans);
			s.insert(2+B+1);
			s.insert(1+B+1);
		}
		else
		{
			double t1=1.0;
			s.insert(1+B+1);

			for(i=1;i<=A-2;i++)
			{
				t1 *= p[i];
			}
			ans = t1*(2+B-(A-2)+1) + (1-t1)*(2+B-(A-2)+1 + B+1);
			s.insert(ans);

			t1 *= p[A-1];
			ans = t1*(1+B-(A-1)+1) + (1-t1)*(1+B-(A-1)+1 + B+1);
			s.insert(ans);

			t1 *= p[A];
			ans = t1*(B-A+1) + (1-t1)*(B-A+1+B+1);
			s.insert(ans);
		}
		printf("Case #%d: ",T);
		set<double>::iterator it = s.begin();
		printf("%.6lf\n",*it);
	}
	return 0;
}