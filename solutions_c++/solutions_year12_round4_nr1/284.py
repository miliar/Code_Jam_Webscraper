#pragma comment(linker,"/STACK:256000000")
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <time.h>
using namespace std;
int main(){
	//double ti=clock();
	//freopen("A-small-attempt0.in","r",stdin); 
	//freopen("outputA_Small.txt","w",stdout);
	freopen("A-large.in","r",stdin); freopen("outputA_Large.txt","w",stdout);
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		int n;
		cin>>n;
		vector<int> d(n),l(n);
		d[0]=0;
		for(int i=0;i<n;i++)
			cin>>d[i]>>l[i];
		int D;
		cin>>D;
		printf("Case #%d: ",t+1);
		vector<int> a(n);
		a[0]=d[0];
		for(int i=0;i<n;i++)
			for(int j=i+1;j<n;j++)
				if(d[j]-d[i]<=a[i])
					a[j]=max(a[j],min(d[j]-d[i],l[j]));
		int yes=0;
		for(int i=0;i<n;i++)
			if(D-d[i]<=a[i]) yes=1;
		if(yes) cout<<"YES\n";
		else cout<<"NO\n";

	}
	//printf("%lf\n",(clock()-ti)/CLOCKS_PER_SEC);
}