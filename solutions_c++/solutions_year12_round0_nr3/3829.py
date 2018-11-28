#include <cstdio>
using namespace std;
int T;
long long a,b;
long long bas(int t)
{
	if(!t) return 1;
	return bas(t/10)*10;
}
int isRecycled(int x)
{
	long long k=bas(x),t=(x%(k/10))*10+(x*10)/k;
	int s=0;
	while(t!=x)
	{
		if(t>x && t<=b) s++;
		t=(t%(k/10))*10+(t*10)/k;
	}
	return s;
}
int main()
{
	int i,k;
	int res;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf(" %d",&T);
	for(k=1;k<=T;k++)
	{
		res=0;
		scanf(" %lld %lld",&a,&b);
		for(i=a;i<=b;i++)
			res+=isRecycled(i);
		printf("Case #%d: %d\n",k,res);
	}
	return 0;
}
