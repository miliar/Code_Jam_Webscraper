#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
//vector<long long> vp1  , vn1 , vp2 , vn2;
vector<long long> v1  ,  v2;
int n;
int main(){
	freopen("4.in" , "rt",stdin);
	freopen("1.out" , "wt",stdout);
	int t;
	cin>>t;
	for(int tt=0 ; tt<t; tt++ ){
		v1.clear(); 
		v2.clear(); 
		cin>>n;
		long long x;
		for(int i = 0 ; i< n ; i++){
			cin>>x;
			
				v1.push_back(x);
			
		}
		for(int i = 0 ; i< n ; i++){	
			cin>>x;
			
				v2.push_back(x);
			
		}
		cout<<"Case #"<<(tt+1)<<": ";
		sort(v1.begin() , v1.end());
		sort(v2.begin() , v2.end());
		long long y = 0;
		
		for(int i = 0 , j = v1.size()-1 ; i<v2.size() ; i++ , j--){
			y+=(v1[j]*v2[i]);
		}
		cout<<y<<endl;
	}
	return 0;
}

/*int main(){
	freopen("1.in" , "rt",stdin);
	freopen("2.out" , "wt",stdout);
	int t;
	cin>>t;
	for(int tt=0 ; tt<t; tt++ ){
		vp1.clear(); vn1.clear();
		vp2.clear(); vn2.clear();
		cin>>n;
		long long x;
		for(int i = 0 ; i< n ; i++){
			cin>>x;
			if(x>0)
				vp1.push_back(x);
			else
				vn1.push_back(x);
		}
		for(int i = 0 ; i< n ; i++){	
			cin>>x;
			if(x>0)
				vp2.push_back(x);
			else
				vn2.push_back(x);
		}
		cout<<"Case #"<<(tt+1)<<": ";
		sort(vp1.begin() , vp1.end());
		sort(vp2.begin() , vp2.end());
		sort(vn2.begin() , vn2.end());
		sort(vn1.begin() , vn1.end());
		long long y = 0;
		int v1ns = vn1.size() , v1ps = vp1.size() , v2ns = vn2.size() , v2ps = vp2.size();
		if(v1ns == v2ps){
			for(int i = 0 ; i<v1ns ; i++){
				y+= (vn1[i]*vp2[i]);
			}
			for(int i = 0 ; i<v2ns ; i++){
				y+= (vn2[i]*vp1[i]);
			}
		}else if(v1ns > v2ps){
			int i,j , k , l;
			for(i = v2ps-1 , l = 0 ; i>=0 ; i--,l++){
				y+= (vn1[l]*vp2[i]);
			}
			for(i = v1ps-1 , k= 0 ; i>=0 ; k++ , i-- ){
				y+= (vp1[i]*vn2[k]);
			}
			for(i = l , j = v2ns-1 ; i<v1ns ; i++ , j--){
				y+= (vn1[i]*vn2[j]);
			}
		}else{
			int i,j , k , l;
			for(i = v1ps-1 , j = 0 ; j<v2ns ; i--,j++){
				y+= (vn2[j]*vp1[i]);
			}
			for(j = v2ps-1 , k=0 ; k<v1ns ; k++ , j-- ){
				y+= (vp2[j]*vn1[k]);
			}
			for(l = i , k = 0 ; l>=0 ; l-- , k++){
				y+= (vp1[l]*vp2[k]);
			}
		}
		cout<<y<<endl;
	}
	return 0;
}*/
