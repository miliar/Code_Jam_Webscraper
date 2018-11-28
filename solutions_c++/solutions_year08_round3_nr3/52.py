#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
const int MOD=1000000007;
class FenTree
{
private:
	const int static MAXN=500000+10;
	int a[MAXN];
public:
	FenTree()
	{
		int i;
		for(i=0;i<MAXN;i++)
			a[i]=0;
	}
	void update(int x,int d)
	{
		while(x<MAXN)
		{
			a[x]=(a[x]+d)%MOD;
			x|=x+1;
		}
	}
	int rsq(int x)
	{
		int res=0;
		while(x>-1)
		{
			res=(res+a[x])%MOD;
			x&=x+1;
			x--;
		}
		return res;
	}
	int rsq(int x,int y)
	{
		return x>y ? 0 : ((rsq(y)-rsq(x-1))%MOD+MOD)%MOD;
	}
};
const int MAXN=500000+10;
int a[MAXN];
int c[MAXN];
vector<int> b;
map<int,int> num;
void solution(int nn)
{
	int m,x,y,z,n;
	scanf("%d %d %d %d %d",&n,&m,&x,&y,&z);
	int i;
	for(i=0;i<m;i++)
		scanf("%d",&a[i]);
	b.clear();
	for(i=0;i<n;i++)
	{
		b.push_back(a[i%m]);
		c[i]=a[i%m];
		a[i%m]=(((long long)x)*a[i%m]+((long long)y)*(i+1))%z;
	}
	sort(b.begin(),b.end());
	int cc=0;
	num.clear();
	num[b[0]]=0;
	for(i=1;i<n;i++)
	{
		if(b[i]!=b[i-1]) cc++;
		num[b[i]]=cc;
	}
	FenTree t;
	int e;
	for(i=0;i<n;i++)
	{
		
		e=(t.rsq(0,num[c[i]]-1)+1)%MOD;
		t.update(num[c[i]],e);
	}
	printf("Case #%d: %d\n",nn,t.rsq(0,cc));
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	scanf("%d",&n);
	int i;
	for(i=0;i<n;i++)
		solution(i+1);
}
