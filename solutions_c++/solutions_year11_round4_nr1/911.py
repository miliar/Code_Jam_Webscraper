#include<stdio.h>
#include<unordered_set>
#include<algorithm>
using namespace std;
struct acc
{
	int B;
	int W;
	int E;
};

bool cmp(acc a1,acc a2)
{
	return a1.W<a2.W || a1.W==a2.W && a1.B<a2.B;
}
vector<acc> acs;
int main()
{
	
	freopen("D:\\Gcj\\A\\input.txt","r",stdin);
	freopen("D:\\Gcj\\A\\output.txt","w",stdout);
    double X,R,S;
	int t;
	double T;
	int N;
	int B[1001],E[1001],W[1001];
    scanf("%d",&t);

	for(int i=0;i<t;i++)
	{
		acs.clear();
		scanf("%lf %lf %lf %lf %d",&X,&S,&R,&T,&N);
		double l;
		double remain=X;
		for(int j=0;j<N;j++)
		{
			scanf("%d %d %d",&B[j],&E[j],&W[j]);
			acc A;
			A.B=B[j];
			A.E=E[j];
			A.W=W[j];
			acs.push_back(A);

			remain-=E[j]-B[j];
		}
		acc A;
		A.B=-1;
		A.E=remain-1;
		A.W=0;
		acs.push_back(A);
		sort(acs.begin(),acs.end(),cmp);
		//work by foot
		double answ=0;
		for(int j=0;j<acs.size();j++)
		{
			double Storun=acs[j].E-acs[j].B;
			double speedWr=acs[j].W+R;
			double speedWf=acs[j].W+S;
			
				double need=Storun/speedWr;
				if(need <=T)
				{
					answ+=need;
					T-=need;
					
				}
				else
				{
					double remD=Storun-T*speedWr;
					double timetoadd=remD/speedWf;
					answ+=T+timetoadd;
					T=0;
					
				}
			
		}
		printf("Case #%d: %.10lf\n",i+1,answ);
		


		
	}
}