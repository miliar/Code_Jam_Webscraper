#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int nt;
int p,k,l;
int let[1024];

void read()
{
	scanf("%d %d %d",&p,&k,&l);
	
	memset(let,0,sizeof(let));
	
	for(int i=0;i<l;i++)
		scanf("%d",&let[i]);
	sort(let,let+l);
}

void solve(int ind)
{
	unsigned long long ans=0;
	if(k*p<l) {printf("Case #%d: Impossible\n",ind);return ;}
	int indx=l-1;
	for(int j=1;j<=p;j++)
	{
		if(indx<0) break;
		for(int i=1;i<=k;i++)
		{
			if(indx<0) break;
			ans+=j*let[indx];
			indx--;
		}
	}
	cout<<"Case #"<<ind<<": "<<ans<<endl;
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
