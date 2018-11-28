#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<cstring>
#include<numeric>

using namespace std;

#define ll long long int 
#define ss1(a) scanf("%d",&a)
#define ss2(a,b) scanf("%d %d",&a,&b)
#define ss3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define loop(i,a,b) for(int i=a;i<b;i++)
#define loope(i,a,b) for(int i=a;i<=b;i++)
#define loopd(i,a,b) for(int i=a;i>=b;i--)

typedef vector<int> vi; 
typedef vector< vi > vvi; 
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define mp(a,b) make_pair(a,b)
#define F first
#define S second

ll powr(int s,int p)
{
	if(p==0)
		return 1;	

	if(p%2==1)
	{
		ll q=powr(s,p/2);
		ll a=q;
		q=(a*a);
		q=(q*s);	
		return ( q );
	}

	else
	{
		ll q=powr(s,p/2);
		ll a=q;
		q=(a*a);	
		return (q);
	}
}

/*******************************MAIN CODE STARTS*******************************/

#define mx 2000000;
int a[2000010];
int m,n;


void init()
{
	loope(i,m,n)
		a[i]=0;
}

int get(int x)
{
	int ret=1;
	int p=x;
	int t,w;
	a[x]=1;
	
	int d=floor(log10(x)+1);

	//printf("%d ",x);
	int i=0;

	while(i<d)
	{
		w=1;
		t=p/10 + ( (p%10)*powr(10,d-1) );
		while(floor(log10(t)+1)!=d)
		{
			w++;
			i++;
			t=p/powr(10,w) + ((p%powr(10,w))*powr(10,d-w));
		}

		p=t;
		if(p>=m && p<=n && a[p]==0 && floor(log10(p)+1)==d)
		{
			//printf("%d ",p);
			ret++;
			a[p]=1;
		}
		i++;
		
		//p=p/10 + ( (p%powr(10,d-1))*10 );
	}

	//printf("\n");
	return ((ret*(ret-1))/2);
}

int main()
{

	int t;
	ss1(t);

	loope(z,1,t)
	{
		ll ret=0;
		ss2(m,n);
		init();
	
		loope(i,m,n)
		{
			if(a[i]==0)
			{
				ret+=get(i);	
				//getchar();
			}
		}
		printf("Case #%d: ",z);
		cout<<ret<<'\n';
	}
	return 0;
}
