#include<iostream>
using namespace std;

int t,n,now;
int lp[2],lt[2];

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("A-small-attempt0.in","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for(int ca=1;ca<=t;++ca)
	{
		cin>>n;
		lp[0]=lp[1]=1;
		lt[0]=lt[1]=0;
		now=0;
		while(n--)
		{
			char who;
			int pos;
			bool flag;
			cin>>who>>pos;
			
			flag=who=='O';
			lt[flag]=max(now+1,lt[flag]+abs(pos-lp[flag])+1);
			lp[flag]=pos;
			now=max(now,lt[flag]);
		}
		printf("Case #%d: %d\n",ca,now);
	}
	return 0;
}
