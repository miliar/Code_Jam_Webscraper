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

char a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
	string in;	
	int t;
	ss1(t);
	getchar();
	loope(z,1,t)
	{
		string r;
		getline(cin,in);
		loop(i,0,sz(in))
		{
			if(in[i]>='a' && in[i]<='z')
				r+=a[in[i]-'a'];
			else
				r+=in[i];
		}
		printf("Case #%d: ",z);
		cout<<r<<"\n";
	}
	return 0;
}

