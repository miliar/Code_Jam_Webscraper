# include<iostream>
# include<cstdio>
# include<vector>
using namespace std;

# define print(a,b) printf("Case #%d: %lld\n",a,b)
# define printno(i) printf("Case #%d: NO\n",i)

typedef long long int  LL;
typedef vector<LL > vi;


vi c;

int t,n;
LL ans = -1;
inline long long Max(LL a,LL b)
{
	if( a> b)return a;
	return b;
}

void rec(vi a,vi b, int left )
{
	if(left ==  0 && a.size() >0 && b.size() >0 )
	{
		LL or1 =a[0], or2=b[0],sum1=a[0],sum2=b[0];
		for(int i=1;i<a.size();i++)or1^=a[i],sum1+=a[i];
		for(int i=1;i<b.size();i++)or2^=b[i],sum2+=b[i];
		if(or1 == or2 )
		{
			ans = Max(ans,Max(sum1,sum2)); 
		} 
		return ;	
	}
	else if(left>0)
	{
		left-=1;
		a.push_back(c[left]);rec(a,b,left);
		a.pop_back();
                b.push_back(c[left]);rec(a,b,left);
	}
	else return ;
}

int  main()
{
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	//int t,n;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		fprintf(stderr,"%d\n",i);
		ans=-1;
		cin>>n;
		c.resize(n);
		for(int k=0;k<n;k+=1)cin>>c[k];
		n-=1;
		vi a,vi,b;
		a.push_back(c[n]);rec(a,b,n);
		a.pop_back();
		b.push_back(c[n]);rec(a,b,n);
		if(ans==-1)
		printno(i);
		else print(i,ans);
	}
	return 0;
}
