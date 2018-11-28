#include <vector>
#include <iostream>

using namespace std;

int f(int i1, int i2, int i3, int n)
{
	if (i1+i2+i3!=n)
		return 2;
	if (abs(i1-i2)>2 || abs(i1-i3)>2 || abs(i2-i3)>2)
		return 2;
	if (abs(i1-i2)<2 && abs(i1-i3)<2 && abs(i2-i3)<2)
		return 0;
	return 1;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	for (int t=1; t<=T; ++t)
	{
		int n,s,p,ans=0;
		cin >> n >> s >> p;
		vector<int> a(n);
		for (int i=0; i<n; ++i)
			cin >> a[i];
		for (int i=0; i<n; ++i)
		{
			int mx=a[i]/3+10,
				mn=max(0,a[i]/2-10),
				h=2;
			for (int i1=p; i1<mx; ++i1)
				for (int i2=mn; i2<mx; ++i2)
					for (int i3=mn; i3<mx; ++i3)
						h=min(h,f(i1,i2,i3,a[i]));
			if (h==0)
			{
				++ans;
			}else if (h==1 && s>0)
			{
				++ans;
				--s;
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}