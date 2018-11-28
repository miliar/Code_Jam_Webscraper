
#include <iostream>
using namespace std;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("tt.out","w",stdout);
	int T,n,l,h,ret,cases=1,f;
	int p[101];
	cin >>T;
	while (T--)
	{
		f=1;
		cin >>n>>l>>h;
		for(int i=0;i<n;i++)
			cin >>p[i];
		cout <<"Case #"<<cases++<<": ";
		for(int i=l;i<=h;i++)
		{
			ret=1;
			for(int j=0;j<n;j++)
				if(i%p[j]!=0 && p[j]%i!=0){
					ret=0;
					break;
				}
			if(ret){
				cout <<i<<endl;
				f=0;
				break;
			}
		}
		if(f) cout <<"NO"<<endl;
	}
	return 0;
}