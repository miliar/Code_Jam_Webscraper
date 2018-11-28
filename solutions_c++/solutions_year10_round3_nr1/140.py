#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<list>
using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int tt;
	cin>>tt;
	for(int t=1;t<=tt;++t){
		
		int n;
		cin>>n;
		vector<pair<int,int> >a(n);
		for(int i=0;i<n;++i)
			cin>>a[i].first>>a[i].second;

		int kil=0;
		for(int i=0;i<n;++i){
			for(int i1=i+1;i1<n;++i1){
				if((a[i].first-a[i1].first)*(a[i].second-a[i1].second)<0)
					kil++;
			}
		}
		cout<<"Case #"<<t<<": ";
		cout<<kil;
		cout<<endl;
	}
	return 0;
}