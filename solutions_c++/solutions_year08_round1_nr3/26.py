#include <stdio.h>
#include <math.h>
#include <utility>
using namespace std;
int N;
typedef pair<pair<int,int>,pair<int,int> > Mdat;
Mdat mp(Mdat a,Mdat b)
{
	return make_pair(
		make_pair((a.first.first*b.first.first+a.first.second*b.second.first)%10000,(a.first.first*b.first.second+a.first.second*b.second.second)%10000),
		make_pair((a.second.first*b.first.first+a.second.second*b.second.first)%10000,(a.second.first*b.first.second+a.second.second*b.second.second)%10000));
}
Mdat times(Mdat in,int time)
{
	Mdat t1,t2;
	t1=make_pair(make_pair(1,0),make_pair(0,1));
	t2=in;
	while (time>0)
	{
		if (time&1)
			t1=mp(t2,t1);
		t2=mp(t2,t2);
		time>>=1;
	}
	return t1;
}
int main()
{
	freopen("C:\\test.in","r",stdin);
	freopen("C:\\test.out","w",stdout);
	int T,nT;
	scanf("%d",&T);
	nT=T;
	while (T--)
	{
		scanf("%d",&N);
		//N=T+2;
		Mdat dat=make_pair(make_pair(6,-4),make_pair(1,0));
		dat=times(dat,N-1);
		int ans=dat.first.first*6+dat.first.second*2-1;
		ans%=1000;
		if (ans<0) ans+=1000;
		printf("Case #%d: %03d\n",nT-T,ans%1000);
	}
	fclose(stdin);
	fclose(stdout);
}