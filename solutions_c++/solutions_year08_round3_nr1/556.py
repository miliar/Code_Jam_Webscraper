#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<list>
#include<set>
using namespace std;
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;
	cin>>t;
	int iii;
	for(iii=1;iii<=t;iii++){
		int p,k,l;
		cin>>p>>k>>l;
		if(k*p<l){
			cout<<"Impossible"<<endl;
			continue;
		}
		vector<int>a(l);
		int i;
		for(i=0;i<l;i++)
			cin>>a[i];
		sort(a.begin(),a.end());
		int kil=0;
		int ko=0;
		int index=l-1;
		for(i=0;i<l;i++){
			//cout<<a[index]<<' ';
			if((i%k)==0)
				ko++;
			kil+=a[index]*ko;
			index--;
		}

		cout<<"Case #"<<iii<<": "<<kil;
		cout<<endl;
	}
	return 0;
}