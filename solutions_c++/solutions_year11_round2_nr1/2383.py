#include<ctime>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
typedef istringstream iss; typedef ostringstream oss; typedef long long lli;
const double TOLL=1e-9;

char arr[110][110]; int n;
double WP[110], OWP[110], OOWP[110], RPI[110];

int main()
{
    int t; cin>>t; int cn=0;
    while(t--)
    {
	cin>>n;
	for(int i=0;i<n;i++) scanf("%s",arr[i]);

	for(int i=0;i<n;i++)
	{
	    double cnt=0; double win=0;
	    for(int j=0;j<n;j++) if(arr[i][j]!='.')
	    {
		cnt++;
		if(arr[i][j]=='1') win++;
	    }
	    WP[i]=0;
	    if(cnt>TOLL) WP[i]=win/cnt;
//	    cerr<<WP[i]<<endl; //OK
	}

	for(int i=0;i<n;i++) //OWP
	{
	    double cnt=0; double winp=0;
	    for(int j=0;j<n;j++) if(arr[i][j]!='.')
	    {
		cnt++; //CONFUSION
		double tc=0, tw=0;
		for(int k=0;k<n;k++) if(k!=i && arr[j][k]!='.')
		{
		    tc++;
		    if(arr[j][k]=='1') tw++;
		}
		if(tc) winp+=tw/tc;
	    }
	    OWP[i]=0;
	    if(cnt) OWP[i]=winp/cnt;
//	    cerr<<OWP[i]<<endl;
	    
	}

	for(int i=0;i<n;i++)
	{
	    double cnt=0, sum=0;
	    for(int j=0;j<n;j++) if(arr[i][j]!='.')
	    {
		cnt++; sum+=OWP[j];
	    }
	    OOWP[i]=0;
	    if(cnt) OOWP[i]=sum/cnt;
	 //   cerr<<OOWP[i]<<endl;
	}

	//RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
	for(int i=0;i<n;i++)
	{
	    RPI[i]=0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
	}
	printf("Case #%d:\n",++cn);
	for(int i=0;i<n;i++)
	{
	    printf("%.12lf\n",RPI[i]);
	}

    }

}
