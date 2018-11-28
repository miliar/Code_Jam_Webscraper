#include<iostream>
#include<set>
#include<cmath>
using namespace std;

int n;
int gates[30];
int values[30];
int canchange[30];
int mat[30][1<<15];
int v;
int INF = 20000;

int put(int v , int i , int j){
	if(j==1){
		return v|(1<<i);
	}else{
		return v &(~(1<<i));
	}
}

int get(int ni , int vv){
	if(ni == 1 ){
		int d = (vv&(1<<0)) == 0? 0 : 1;
		if(d == v)
			return 0;
		else
			return INF;
	}
	if(mat[ni-1][vv]!=-1)
		return mat[ni-1][vv]; 
	int n1 = ni-1 ,  n2 = ni-2;
	int t1 , t2;
	if(n1>=(n-1)/2){
		t1 = values[n1];
	}else{
		t1 = (vv&(1<<n1)) == 0? 0 : 1;
	}
	if(n2>=(n-1)/2){
		t2 = values[n2];
	}else{
		t2 = (vv&(1<<n2)) == 0? 0 : 1;
	}
	int p = ni/2 -1 ;
	int res = INF;
	if(canchange[p]){
		res = min(res, (gates[p]==1? 0 : 1)+get(ni-2 , put(vv , p , (t1 && t2))));
		res = min(res, (gates[p]==0? 0 : 1)+get(ni-2 , put(vv , p , (t1 || t2))));
	}else if(gates[p]==1){
		res = min(res, get(ni-2 , put(vv , p , (t1 && t2))));
	}else{
		res = min(res, get(ni-2 , put(vv , p , (t1 || t2))));
	}
	return mat[ni-1][vv] = res;
}

int main(){
	freopen("A-small.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
	int t;
	cin>>t;
	for(int tt =1; tt<=t ; tt++){
		cout<<"Case #"<<tt<<": ";
		cin>>n>>v;
		memset(mat , -1 , sizeof mat);
		for(int i = 0 ; i<n ; i++){
			if(i<(n-1)/2){
				cin>>gates[i]>>canchange[i];
			}else{
				cin>>values[i];
			}
		}
		int res = get(n , 0);
		if(res>=INF)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<res<<endl;
	}
	return 0;
}
