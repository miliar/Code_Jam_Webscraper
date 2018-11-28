


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
#include <fstream>
using namespace std; 
template<class T> T gcd(T a,T b){return a==0?b:gcd(b%a,a);}
template<class T> string tostring(T a){ostringstream os;os<<a;return os.str();}
int toint(string a){istringstream is(a);int p;is>>p;return p;}
long long toll(string a){istringstream is(a);long long p;is>>p;return p;}

void sm(const vector<vector<long long> > &mass,vector<vector<long long> > &sum)
{
	sum[0][0]=mass[0][0];
	for(int j=1;j<sum[0].size();j++)
	{
		sum[0][j]=sum[0][j-1]+mass[0][j];
	}
	long long sum2;
	for(int i=1;i<mass.size();i++)
	{
		sum2=0;
		for(int j=0;j<sum[0].size();j++)
		{
			sum2+=mass[i][j];
			sum[i][j]=sum2+sum[i-1][j];
		}
	}
}

long long get(const vector<vector<long long> > &sum,const vector<vector<long long> > &mass,int x1,int y1,int x2,int y2)
{
	long long res;
	res=sum[x2][y2];
	if(x1!=0)res-=sum[x1-1][y2];
	if(y1!=0)res-=sum[x2][y1-1];
	if(x1!=0&&y1!=0)res+=sum[x1-1][y1-1];
	res-=mass[x1][y1]+mass[x2][y1]+mass[x1][y2]+mass[x2][y2];
	return res;
}

void _main()
{
	int R,C,D;
	cin>>R>>C>>D;
	vector<string> vs(R);
	for(int i=0;i<R;i++)
	{
		cin>>vs[i];
	}
	vector<vector<long long> > sum(R,vector<long long>(C)) ,mass(R,vector<long long>(C)),
		rsum(R,vector<long long>(C)) ,rmass(R,vector<long long>(C)),
		csum(R,vector<long long>(C)) ,cmass(R,vector<long long>(C));
	for(int i=0;i<R;i++)
	{
		for(int j=0;j<C;j++)
		{
			mass[i][j]=vs[i][j]-'0';
			rmass[i][j]=mass[i][j]*i;
			cmass[i][j]=mass[i][j]*j;
		}
	}
	sm(mass,sum);
	sm(rmass,rsum);
	sm(cmass,csum);
	int t=min(R,C);
	for(;t>=3;t--)
	{
		for(int i=0;i+t<=R;i++)for(int j=0;j+t<=C;j++)
		{
			long long sumx=get(sum,mass,i,j,i+t-1,j+t-1);
			long long rsumx=get(rsum,rmass,i,j,i+t-1,j+t-1);
			long long csumx=get(csum,cmass,i,j,i+t-1,j+t-1);
			if(sumx*(i+i+t-1)==rsumx*2&&sumx*(j+j+t-1)==csumx*2)
			{
				cout<<t<<endl;
				return;
			}
		}
	}
	cout<<"IMPOSSIBLE"<<endl;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cout<<"Case #"<<i<<": ";
		_main();
	}
}