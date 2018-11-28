#include <iostream>
#include <algorithm>
using namespace std;


int f(int n,int *a,int s,int p){
	int *sup = new int[n];
	int i;
	int count = 0;
	for(i=0;i<n;i++){
		if(p!=1){
			if(a[i] >= 3*p - 4) break;
		}
		else{
			if(a[i] > 0) break;
		}
	}
	//cout<<"i = "<<i<<endl;
	int t = s;
	for(int j = n-1 ; j>=i ; j--){
		if(a[j] >= 3*p - 2) count++;
		else if(t!=0){
			//cout <<"da"<<endl;
			t--;
			count++;
		}
	}
	/*for(int i=0;i<s;i++) {
		if(a[i]!=0){
			sup[i] = a[i]/3 + 1 + (a[i]%3 == 2);
		}
		else{
			sup[i] = 0;
		}
	}	
	for(int i=s;i<n;i++) {
		if(a[i]!=0){
			sup[i] = a[i]/3 + (a[i]%3 != 0);
		}	
		else{
			sup[i] = 0;
		}
	}
	
	int count = 0;
	for(int i=0;i<n;i++){
		if(sup[i] >= p) count++;
	}*/
	return count;
}

int main(){
	int t;
	cin>>t;
	int n;
	int s;
	int p;
	for(int k=1;k<=t;k++){
		cin>>n>>s>>p;
		int *a = new int[n];
		for(int i = 0;i<n;i++){
			cin>>a[i];
		}
		sort(a,a+n);
		cout<<"Case #"<<k<<": "<<f(n,a,s,p)<<endl;
	}
	return 0;
}