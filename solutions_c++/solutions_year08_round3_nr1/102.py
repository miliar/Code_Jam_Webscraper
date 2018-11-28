

#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>
using namespace std;


int main()
{
	int n,t=0;
	cin>>n;
	while(n--)
	{
		int p,k,l;
		cin>>p>>k>>l;
		vector<int> vc(p,k);
		long long ans = 0;
		vector<int> vp(l);
		for(int i=0;i<l;++i)
			cin>>vp[i];
		sort(vp.begin(),vp.end(),greater<int>());
		//~
		for(int i=0;i<l;++i){
			int j;
			for(j=0;j<p;++j){
				if(vc[j]>0){
					vc[j]--;
					break;
				}
			}
			ans += (__int64(j+1)) * vp[i];
		}
		++t;
		cout<<"Case #"<<t<<": ";
		cout<<ans<<endl;
	}
}