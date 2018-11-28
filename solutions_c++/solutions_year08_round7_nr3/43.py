#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>


#define for0(n,t) for(int n=0;n<t;++n)
#define forV(n,t) for(int n=0;n<t.size();++n)
#define Vall(t) t.begin(),t.end()


using namespace std;
#define DPP long long
DPP memo[500][500];
DPP dp(int at,int left)
{
	if(at == 0){return 0;}
	DPP &ret = memo[at][left];
	if(ret != -1){return ret;}
	ret = 0;
	//blah
	//
	return ret;
}

double z[55][4];

int MA;
vector<double> vd;
void dfs(int at,double d)
{
	if(at == MA){vd.push_back(d);return;}
	for(int i=0;i<4;++i)
	{dfs(at+1,d*z[at][i]);}

}

int main(void)
{
	int CASES;
	cin >> CASES;
	for(int CN=1;CN<=CASES;++CN)
	{
		int M,Q;
		cin >> M >> Q;
		for(int i=0;i<Q;++i)
		{
			for(int j=0;j<4;++j)
			{
				cin >> z[i][j];
			}
		}
		MA = Q;
		vd.clear();
		dfs(0,1.0);
		sort(vd.begin(),vd.end());
		reverse(vd.begin(),vd.end());
		double d = 0.0;
		M<?= (1 << (2*Q));
		cerr << "HI" << endl;
		for(int i=0;i<M;++i)
		{d += vd[i];}


		fprintf(stdout,"Case #%d: %.12lf\n",CN,d);
		fprintf(stderr,"Case #%d: %.12lf\n",CN,d);
	}
}
