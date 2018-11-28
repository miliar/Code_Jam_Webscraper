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
#include <ctime> 

using namespace std;

char a[200][200];
double wp[200];
double twp[200];
int on[200];
double owp[200];
double oowp[200];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,l,t,tmp1,n,cnt;
	scanf("%d",&t);
	for (l=0;l<t;l++)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)
			scanf("%s",a[i]);
		memset(on,0,sizeof(on));
		for (i=0;i<n;i++)
		{
			wp[i]=0;
			for (j=0;j<n;j++)
				if (a[i][j]!='.')
				{
					on[i]++;
					if (a[i][j]=='1') 
						wp[i]+=1;
				}
			wp[i]/=on[i];
		}
		for (i=0;i<n;i++)
		{
			owp[i]=0;
			for (j=0;j<n;j++)
				if (a[i][j]!='.')
				{
					twp[j]=wp[j]*on[j];
					tmp1=on[j]-1;
					if (a[j][i]=='1')
						twp[j]-=1;
					twp[j]/=tmp1;
					owp[i]+=twp[j];
				}
			owp[i]/=on[i];
		}
		for (i=0;i<n;i++)
		{
			oowp[i]=0;
			cnt=0;
			for (j=0;j<n;j++)
				if (a[i][j]!='.')
				{
					oowp[i]+=owp[j];
					cnt++;
				}
			oowp[i]/=cnt;
		}
		printf("Case #%d:\n",l+1);
		for (i=0;i<n;i++)
			printf("%.12lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}
	return 0;
}

