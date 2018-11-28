#include <iostream>
using namespace std;
typedef long long ll;
ll a,b,ans;
bool check(int x,int y)
{
	int a[10],siz=0;
	while(x)
	{
		a[siz++]=x%10;
		x/=10;
	}
	int si=0,b[10];
	while(y)
	{
		b[si++]=y%10;
		y/=10;
	}
	if(si!=siz)
		return false;
	for(int i=0;i<siz;i++)
	{
		bool flag=true;
		for(int j=0;j<si;j++)
			if(a[(i+j)%siz]!=b[j])
				flag=false;
		if(flag)
			return true;
	}
	return false;
}
int main()
{
	int tsts;
	cin >> tsts;
	for(int kk=0;kk<tsts;kk++)
	{
		ans=0;
		cin >> a >> b;
		for(int i=a;i<=b;i++)
			for(int j=i+1;j<=b;j++)
				if(check(i,j))
					ans++;
		cout << "Case #" << kk+1 << ": " << ans << endl;
	}
	return 0;
}
