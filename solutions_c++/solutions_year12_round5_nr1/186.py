#include<iostream>
#include<cstdio>
using namespace std;
typedef long long ll;
struct af{
	int id;
	int l,p;
	bool operator<(const af cp)const{
		if(p!=cp.p)
			return p>cp.p;
		return id<cp.id;
	}
};
int main(){
	int t;
	cin>>t;
	af as[1009];
	int n;
	//scanf("%d",&t);
	for(int z=1;z<=t;z++){
		cin>>n;
		for(int i=0;i<n;i++){
			cin>>as[i].l;
			as[i].id=i;
		}
		for(int i=0;i<n;i++){
			cin>>as[i].p;
		}
		sort(as,as+n);
		cout<<"Case #"<<z<<":";
		for(int i=0;i<n;i++){
			cout<<" "<<as[i].id;
		}
		//printf("Case #%d: ",z);
		cout<<endl;
		//printf("\n");
	}
	return 0;
}
