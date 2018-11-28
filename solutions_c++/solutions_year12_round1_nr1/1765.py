#include<stdio.h>
#include<vector>

using namespace std;

int T;
int A,B;
vector<double> prob;
double prob_cal[100000];

int main()
{
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		prob.clear();
		scanf("%d %d",&A,&B);
		for(int i=0;i<A;i++)
		{
			double temp;
			scanf("%lf",&temp);
			prob.push_back(temp);
		}
		// calc prob
		double sum = 1.0;
		for(int i=0;i<A;i++)
		{
			sum *= prob[i];
		}
		prob_cal[0] = sum;
		for(int i=0;i<A;i++)
		{
			sum /= prob[A-1-i];
			sum *= (1.0-prob[A-1-i]);
			prob_cal[i+1] = sum;
		}
		//try type
		double ans = prob_cal[0] * (B-A+1) + (1.0-prob_cal[0]) *(B+1+B-A+1);
		//printf("%lf",ans);
		// back space
		double _sum = prob_cal[0];
		for(int i=1;i<=A;i++)
		{
			double temp = 0.0;
			_sum += prob_cal[i];
			temp += (_sum) * (B-A+1+2*i);
			temp += (1.0-_sum) * (B-A+1+2*i+B+1);
			if(ans - temp > 0.000001)
				ans =temp;
		//printf("%lf",ans);
		}	
		if(ans - (B+2)*1.0 > 0.000001)
			ans = (B+2)*1.0;
		//printf("%lf",ans);

		//printf("%lf",ans);
		
		printf("Case #%d: %lf\n",t,ans);
	}
	return 0;
}
