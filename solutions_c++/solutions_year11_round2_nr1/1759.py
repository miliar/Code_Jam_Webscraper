#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define clr(x) memset((x), 0, sizeof(x))

int T,N;
char a[101][101];
int main()
{
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
//	freopen("test.txt","r",stdin);freopen("test.out","w",stdout);

//  for(i = 0; i < N; i++)
	int i,j;
	cin>>T;
	for(int caseID = 1; caseID <= T; caseID++)
	{	
		double wp[101],owp[101],oowp[101];
		int winNum[101],total[101];
		cout<<"Case #"<<caseID<<": "<<endl;
		cin>>N;
		for(i = 0; i < N; i++)
		{
			for(j = 0; j < N; j++)
			{
				cin>>a[i][j];
			}
		}
		//wp
		for(i = 0; i < N; i++)
		{
			winNum[i] = 0;
			total[i] = 0;
			for(j = 0; j < N; j++)
			{
				if(a[i][j] != '.' && i != j)
				{
					total[i]++;
					if(a[i][j] == '1')
						winNum[i]++;
				}
			}
			wp[i] = (double)(winNum[i])/total[i];
		}
		//owp
		for(i = 0; i < N; i++)
		{
			double owtmp = 0;
			int opnum = 0;
			for(j = 0; j < N; j++)
			{
				if(j != i)
				{
					if(a[i][j] == '1')
					{
						opnum++;
						if(winNum[j] > 0 && total[j]-1 != 0)
							owtmp += (double)(winNum[j])/(total[j]-1);
					}
					else if(a[i][j] == '0')
					{
						opnum++;
						if(winNum[j] - 1> 0 && total[j]-1 != 0)
							owtmp += (double)(winNum[j] - 1)/(total[j]-1);
					}
				}
			}
			owp[i] = owtmp/opnum;
		}
		for(i = 0; i < N; i++)
		{
			double oowptmp = 0;
			int ntmp = 0;
			for(j = 0; j < N; j++)
			{
				if(j != i && a[i][j] != '.')
				{
					ntmp++;
					oowptmp += owp[j];
				}
			}
			oowp[i] = oowptmp/ntmp;
		}
		double ans;
		for(i = 0; i < N; i++)
		{
			ans = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
			cout<<ans<<endl;
		}
//		cout<<endl;
	}
	return 0;
}