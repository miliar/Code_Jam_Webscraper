#include  <cstdio> 
#include  <cstdlib> 
#include  <cstring> 
#include  <string> 
#include  <vector> 
#include  <cmath> 
#include  <algorithm> 
#include  <cassert> 
#include  <set> 
#include  <map> 
#include  <queue> 
#include  <iostream> 
#include <fstream> 
using namespace std; 
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )  

typedef long long LL; 
typedef pair<int,int> pii; 

int x[3][3];

int main()
{
	int cases;
	scanf("%d", &cases);
	REP(caseIndex, cases)
	{
		double res = 1e100;
		int N;cin>>N;
		REP(i,N)
			REP(j,3)
				cin>>x[i][j];
		//cout<<N<<endl;
		if (N == 1)
			res = x[0][2];
		else
			if (N == 2)
				res = max(x[0][2], x[1][2]);
			else
			{
				REP(j,3)
				{
					double tmp = x[j][2];
					REP(t1, 3)
						REP(t2, t1)
							if (t1!=j && t2!=j)
								tmp = max(tmp, (x[t1][2]+x[t2][2]+sqrt(pow(x[t1][0]-x[t2][0]+0.0,2.0) + pow(x[t1][1]-x[t2][1]+0.0,2.0)))/2);
					res = min(res, tmp);
				}
				
			}
		printf("Case #%d: %.6lf\n", caseIndex + 1,res);
	}
}
