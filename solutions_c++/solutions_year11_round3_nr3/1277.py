#include<iostream>
#include<string>
#include<cstdio>
#include<vector>
using namespace std;
int n,l,h;
long long a[1000];
inline void fact(long long x,vector< pair<long long,int> >& v)
{
        int d=1;
        long long i;
        for(i=2; (x/i) && (i*i<=x) ;i+=d,d=2)
                if(x%i==0)
                        for(v.push_back(make_pair(i,0));x%i == 0;x/=i)
                                ++v.back().second;

        if(x!=1)
                v.push_back( make_pair(x,1) );

}

long long gcd(long long a,long long b)
{
	if(b == 0) return a;
	return gcd(b,a%b);
}
long long lcm(long long a,long long b)
{
	return a*b/gcd(a,b);
}
long long solve()
{
	int i,j;
	/*	long long x = a[0];
	for(i=1;i<n;i++)
	x = lcm(x,a[i]);
	*/
	long long x = -1;
	while(l<=h)
	{

		for(i=0;i<n;i++)
			if(l%a[i]==0 ||a[i]%l==0) continue;
			else break;
			if(i==n) return l;

			l++;
	}

	//vector<long long> v;
	//for(i=0;i<n;i++)
	//{
	//	vector<pair<long long,int> > t;
	//	fact(a[i],t);
	//	for(j=0;j<t.size();j++)
	//		v.push_back(t[j].first);
	//}
	//long long x = v[0];
	//for(i=1;i<v.size();i++)
	//	x = lcm(x,v[i]);
	/*if (l/x < h/x) return x*((l/x)+1);
	if(l%x==0) return l;
	if(h%x==0) return h;*/
	//while(l<=h)
	//{
	//	if(l%x ==0 ) return l;
	//	l++;
	//}
	//if(x>=l && x<=h) return x;
	return -1;
}
int main()
{
	freopen("in.txt","rt",stdin);
	freopen("C.out","wt",stdout);
	int TC,i;
	long long ans;
	scanf("%d",&TC);
	for(int tc = 1;tc<=TC;tc++)
	{
		scanf("%d %d %d",&n,&l,&h);
		for(i=0;i<n;i++)
			scanf("%I64d",&a[i]);
		printf("Case #%d: ",tc);

		ans = solve();
		if(ans != -1)
			printf("%I64d\n",ans);
		else printf("NO\n");
	}
	return 0;
}