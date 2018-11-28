#include <iostream>

using namespace std;

const int MAXN = 110;
const int MAXM = 1000100;

int n, k, d[MAXN];
int s[MAXM], f[MAXM], a[MAXM], b[MAXM];

void init()
{
	int i;
	
	scanf("%d", &k);
	scanf("%d", &n);
	for (i=1; i<=n; i++)
		scanf("%d", &d[i]);	
}

int low(int x)
{
	return (((x-1)^x)&x);
}

int count(int x)
{
	int t=0, xx=x;
	while (x>0){
		t+=s[x];
		x-=low(x);
	}
	return xx-t;
}

int find(int x)
{
	int l, r, mid;
	
	l=1; r=k; 
	while (l<r){
		mid=(l+r)/2;
		if (count(mid)>=x)
			r=mid;
		else
			l=mid+1;	
	}
	return l;	
}

void add(int x)
{
	while (x<=k){
		s[x]++;
		x=x+low(x);
	}	
}

void work()
{
	int i, p, t;
	
	memset(f, 0, sizeof(f));
	f[k]=1;
	t=0;
	for (i=k-1; i>=1; i--){
		p=k-i;
		t=((t-i)%p+p)%p;
		f[i]=t+1;
	}	
	memset(s, 0, sizeof(s));
	for (i=1; i<=k; i++){
		a[i]=find(f[i]);
		add(a[i]);
	}
	for (i=1; i<=k; i++)
		if (a[i]>=a[1]){
			b[a[i]-a[1]+1]=i;
			
		}
		else
		{
			b[k-a[1]+1+a[i]]=i;
		}
	for (i=1; i<=n; i++)
		printf("%d ", b[d[i]]);	
	printf("\n");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
	int cas=0, t;
	scanf("%d", &t);
	while (t--){
		cas++;
		printf("Case #%d: ", cas);
		init();
		work();
	}
	
	return 0;
}
