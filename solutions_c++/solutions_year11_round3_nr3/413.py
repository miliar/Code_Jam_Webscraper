#include <iostream>
using namespace std;

int a[110];
int n,l,h,i,ans,t,ca;
bool flg;

void work()
{
	int d;
	for (i=0;i<n;i++)
	{
		int a1,b,c;
		a1=ans; b=a[i];
		if (a1<b)
		{
			c=a1; a1=b; b=c;
		}
		if (a1%b!=0)
		{
		flg=0;
		return;
		}
	}
}

int main()
{
	freopen("in.in","r",stdin);
	freopen("ou.ou","w",stdout);
	cin>>t;
	while (t--)
	{
		ca++;
		cout<<"Case #"<<ca<<": ";
		cin>>n>>l>>h;
		for (i=0;i<n;i++) cin>>a[i];
		for (ans=l;ans<=h;ans++)
		{
			flg=1;
			work();
			if (flg) 
			{
				cout<<ans<<endl;
				break;
			}
		}
		if (!flg) cout<<"NO"<<endl;
	}
}

