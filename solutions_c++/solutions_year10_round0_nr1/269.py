#include<iostream>
using namespace std;

int n,k;
int pow2[31];
int check[31];

void setlist()
{
	int i;
	pow2[0]=1;
	check[0]=0;
	for(i=1;i<=30;++i)
	{
		pow2[i]=pow2[i-1]*2;
		check[i]=pow2[i]-1;
	}
}

bool ison()
{
	if(k%pow2[n]==check[n]) return true;
	return false;
}

int main()
{
	int ti,t;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	setlist();
	for(ti=1;ti<=t;++ti)
	{
		scanf("%d%d",&n,&k);
		if(ison()){
			printf("Case #%d: ON\n",ti);
		}else{
			printf("Case #%d: OFF\n",ti);
		}
	}
	//system("pause");
	return 0;
}