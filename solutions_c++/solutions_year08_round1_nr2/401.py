#include<iostream>
#include<vector>
using namespace std;

int mat[11][1025];
int n , m;
vector<pair<int , int> > v[101]; 
int count(int t){
	int res = 0;
	while(t>0){
		res+=t%2;
		t/=2;
	}
	return res;
}
int get(int i , int j ){
	if(i >= n){
		for(int l = 0 ; l<m ; l++){
			int k;
			for(k = 0 ; k<v[l].size() ; k++){
				int t = ((j & (1<<v[l][k].first))==0? 0 :1); 
				if(t==v[l][k].second)
					break;
			}
			if(k == v[l].size()) return 1000000;
		}
		return j;
	}
	if(mat[i][j]!=-1) return mat[i][j];
	int r1 = get(i+1 , j|(1<<i)) , r2 = get(i+1 , j );
	int r1t = count(r1) , r2t = count(r2);
	if(r1 >= 1000000){
		if(r2<1000000)
			return r2;
		return 1000000;
	}
	if(r2 >= 1000000){
		if(r1<1000000)
			return r1;
		return 1000000;
	}	
	if(r1t<r2t)
		return mat[i][j] = r1;
	return mat[i][j] = r2;
}

int main(){
	freopen("1.in","rt",stdin);
	freopen("1.out","wt",stdout);
	int t;
	cin>>t;
	for(int tt = 0 ; tt<t ; tt++){
		cin>>n;
		cin>>m;
		for(int i = 0 ; i< m ; i++){
			v[i].clear();
			int d , x ,y;
			cin>>d;
			for(int j= 0 ; j< d ; j++){
				cin>>x>>y;
				x--;
				v[i].push_back(make_pair(x,y));
			}
		}
		cout<<"Case #"<<(tt+1)<<": ";
		memset(mat,-1 , sizeof mat);
		int res = get(0,0);
		if(res>=1000000)
			cout<<"IMPOSSIBLE"<<endl;
		else{
			for(int i = 0 ; i<n ; i++){
				int t = ((res & (1<<i))==0? 0 :1);
				if(i>0) cout<<" ";
				cout<<t;
			}
			cout<<endl;
		}
	}
	return 0;
}
