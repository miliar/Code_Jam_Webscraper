#include<cstdio>
#include<cstring>
#include<iostream>

using namespace std;

#define IN "C-large.in"
#define OUT "C-large.out"

#define LL long long

#define MAX_N 1000

LL R,k;
int N;
LL g[MAX_N+1];

LL d[MAX_N+1];
int hash[MAX_N+1];

LL calc(const int &l,const int &r)
{
	LL total=0;
	if(r==-1)
	{
		for(int i=0;i<R;i++) total+=d[i];
		return total;
	}
	for(int i=0;i<l;i++) total+=d[i];
	R-=l;

	LL sum=0;
	for(int i=l;i<=r;i++) sum+=d[i];

	total+=sum*(R/(r-l+1));

	R%=(r-l+1);

	if(R!=0) for(int i=l;i<l+R;i++) total+=d[i];

	return total;

}

LL solve()
{
	memset(hash,0xFF,sizeof(hash));
	int head=0;
	int l=-1,r=-1;
	for(int i=0;i<R;i++)
	{
		if(hash[head]!=-1)
		{
			l=hash[head];
			r=i-1;
			break;
		}

		hash[head]=i;

		LL cnt=0;
		for(int j=0;j<N;j++)
		{
			if(cnt+g[(head+j)%N]>k)
			{
				head=(head+j)%N;
				break;
			}
			cnt+=g[(head+j)%N];
		}

		d[i]=cnt;
	}

	return calc(l,r);
}

int main()
{
	freopen(IN,"r",stdin);
	freopen(OUT,"w",stdout);

	int T;
	cin>>T;
	for(int caseID=1;caseID<=T;caseID++)
	{
		cin>>R>>k>>N;
		for(int i=0;i<N;i++) cin>>g[i];
		cout<<"Case #"<<caseID<<": "<<solve()<<endl;
	}
	return 0;
}
