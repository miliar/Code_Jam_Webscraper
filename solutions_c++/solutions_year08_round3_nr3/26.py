#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

unsigned long long n,m,X,Y,Z,nt;

unsigned long long ma[(1<<19)];
struct g{
	int p;
	unsigned long long val;
}gm[(1<<19)];
long long tree[1<<20];
int mas[1<<19];

bool operator<(const g &x,const g &y)
{
	if(x.val<y.val) return 1;
	return 0;
}

void read()
{
	memset(ma,0,sizeof(ma));
	memset(gm,0,sizeof(gm));
	memset(tree,0,sizeof(tree));
	cin>>n>>m>>X>>Y>>Z;
	for(int i=0;i<m;i++)
	{
		scanf("%d",&ma[i]);
	}
	for(int i=0;i<n;i++)
	{
		gm[i].val = ma[i%m];
		gm[i].p=i;
		
		ma[i%m]=(X*ma[i%m]+Y*(i+1))%Z;
	}
}

void push(int p, int v)
{
	while (p <= (1<<19)) {
		tree[p]+=v;
		tree[p]%=1000000007;
		p += (p&(-p));
		}
}

long long pop(int p)
{
	unsigned long long res=0;
	while (p>0) {
		res+=tree[p];
		res%=1000000007;
		p -= (p&(-p));
		}
	return res;
}

void solve(int ind)
{
	unsigned long long br=0;
	sort(gm,gm+n);
	int s=1;
	mas[gm[0].p]=s;
	for(int j=1;j<n;j++)
	{
		if(gm[j-1].val==gm[j].val)
			mas[gm[j].p]=s;
		else mas[gm[j].p]=++s;
	}
	for(int i=0;i<n;i++)
	{
		unsigned long long qr;
		qr=pop(mas[i]);
		qr%=1000000007;
		push(mas[i]+1,qr+1);
		br+=qr+1;
		br%=1000000007;
	}
	cout<<"Case #"<<ind<<": "<<br<<endl;
}

int main()
{
	scanf("%d",&nt);
	for(int i=0;i<nt;i++)
	{
		read();
		solve(i+1);
	}

    return 0;
}
