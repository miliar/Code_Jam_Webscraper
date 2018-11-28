#include <cstdio>
#include <vector>
#define fi first
#define se second
#define pb push_back
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pi;
int t[1000003];
int nwd(int a, int b)
{
	if (b>a) return nwd(b,a);
	if (b==0) return a;
	return nwd(b,a%b);
}
bool isPrime(int a)
{
	for (int i=2; i*i<=a; i++)
		if (a%i==0) return false;
	return true;
}
bool common(int a, int b, int p)
{
	int c=nwd(a,b);
	for (int i=p; i<=c; i++)
		if (isPrime(i)&&c%i==0) return true;
	return false;
}
int par(int a)
{
	if (t[a]==a) return a;
	int k=par(t[a]);
	t[a]=k;
	return k;
}
void merge(int a, int b)
{
	int p=par(a);
	int q=par(b);
	t[p]=q;
}
int main()
{
	int N;
	scanf("%d",&N);
	for (int u=1; u<=N; u++)
	{
		int a,b,p;
		scanf("%d %d %d",&a,&b,&p);
		for (int i=0; i<=b-a; i++)
			t[i]=i;
		for (int i=a; i<=b; i++)
			for (int j=i+1; j<=b; j++)
				if (common(i,j,p)) merge(i-a,j-a);
		int w=0;
		for (int i=0; i<=b-a; i++)
			if (t[i]==i) w++;
		printf("Case #%d: %d\n",u,w);
	}
}
