#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;
struct store{
	store(int aa, int bb): a(aa), b(bb){}
	int a,b;
};
bool sorter(store const& lhs, store const& rhs){
	return lhs.a<rhs.a;
}
int main(){
	int to;
	cin>>to;
	for(int nn = 1; nn<=to; nn++){
		long long t;
		int l,n,c;
		cin>>l>>t>>n>>c;
		vector<int> a;
		for(int i =0; i<c; i++){
			int x;
			cin>>x;
			a.push_back(x);
		}
		vector<int> dist;
		for(int i = 0; i<n; i++){
			dist.push_back(a[i%c]);
		}
		vector<int> vals;
		vector<store> toso;
		long long tt=t;
		for(int i = 0; i<n; i++){
///			cout<<tt<<endl;
			if(tt==0){
				vals.push_back(dist[i]*2);
			}
			else{
				long long tmp = tt-dist[i]*2;
				if(tmp>0){
					vals.push_back(0);
					tt=tt-dist[i]*2;
				}
				else{
					vals.push_back((-1)*(int)tmp);
					tt=0;
				}
		
			}
		}
		for(int i = 0; i<n; i++){
///			cout<<vals[i]<<" ";
			store todo(vals[i],dist[i]);
			toso.push_back(todo);
		}
///		cout<<endl;
///		cout<<endl;
		std::sort(toso.begin(),toso.end(), &sorter);
		int ll = l;
		long long res = 0;
		for (int i= n-1; i>=0; i--){
///			cout<<toso[i].a<<" "<<toso[i].b<<endl;
///			cout<<res<<endl;
			if(ll==0 || toso[i].a==0){
				res+=toso[i].b*2;
			}
			else{
				if(toso[i].a==toso[i].b*2){
					res=res+(long long)toso[i].b;
					ll--;
				}
				else{
					res=res+(long long)(toso[i].a/2+2*toso[i].b-toso[i].a);
					ll--;
				}
			}
		}
		cout<<"Case #"<<nn<<": "<<res<<endl;
	}
}
