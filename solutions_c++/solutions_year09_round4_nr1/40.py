#include<iostream>
#include<vector>
using namespace std;

bool check(const vector<int>&a,int b){
	for(int i=b+1;i<a.size();i++)
		if(a[i])return 0;
	return 1;
}

main(){
	int t;
	cin>>t;
	for(int kase=1;kase<=t;kase++){
		int n;
		scanf("%d\n",&n);
		vector<vector<int> >a(n,n);
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				char c;
				scanf("%c",&c);
				a[i][j]=c-'0';
			}
			scanf("\n");
		}
		int ans=0;
		for(int i=0;i<n;i++){
			int j;
			for(j=0;j<a.size();j++)
				if(check(a[j],i))break;
			ans+=j;
			a.erase(a.begin()+j);
		}
		cout<<"Case #"<<kase<<": "<<ans<<endl;
	}

}
