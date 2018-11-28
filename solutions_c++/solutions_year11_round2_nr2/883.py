#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>

using namespace std;

const int MaxV = 1000005;

double D , eps = 1e-8;
vector<double> V;

bool canbe(double T)
{
	double pre_loc ;
	for(int i=0;i<V.size();i++)
	{
		if(i==0)
			pre_loc = V[i] - T;
		else{

			// 需要的位置在V[i]後面
			if( pre_loc + D <= V[i] ){
				pre_loc = max( pre_loc+D , V[i]-T );
			// 需要的位置在V[i]前面
			}else{
				if( V[i] + T < pre_loc+D )
					return false;
				else
					pre_loc = pre_loc+D;
			}
		}
	}
	return true;
}

double FindMin()
{
	double beg = 0.0 , end = 1e9, mid , best = 1e9;
	do{
		mid = (beg + end) / 2.0;
		if( canbe(mid) ){
			best = min( best , mid);
			end = mid;
		}else
			beg = mid + eps;

	}while(beg + eps < end );

	return best;
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);

	int cs,point;
	scanf("%d",&cs);

	for(int c=1;c<=cs;c++)
	{
		scanf("%d%lf", &point , &D);

		double P; int Vnum;
		for(int i=0;i<point;i++)
		{
			scanf("%lf%d", &P , &Vnum);
			for(int j=0;j<Vnum;j++)
				V.push_back(P);
		}
		sort( V.begin() , V.end() );
		/*for(int i=0;i<V.size();i++)
			printf("%.2lf ",V[i]);
		putchar('\n');*/

		printf("Case #%d: %.8lf\n",c, FindMin() );
		V.clear();
	}
	return 0;
}
