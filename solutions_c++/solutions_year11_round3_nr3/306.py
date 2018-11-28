#include<iostream>
#include<algorithm>
#include<string>
#include<cstdio>
#include<vector>
#define REP(j,n) for(int j=0;j<(n);j++)

using namespace std;
int main(){
	int h,l,n;
	long long t;
	int temp;
	int cases,i=0;
	cin >> cases;
	while( i++<cases ){
		cin >> n >> l >> h ;
		vector<int> a;
		REP(j,n){
			cin>>temp;
			a.push_back(temp);
		}
		int flag=0;
		int res;
		for( int f=l;f<=h;f++){
			flag=0;
			REP(k,a.size()){
				if(! ( a[k]%f==0 or f%a[k]==0) )	
					flag=1;
			}
			if(flag==0){
				res=f;
				f=h+1;
				flag=2;
			}
		}
		cout << "Case #"<<i<<": ";
		if(flag==2)
			cout << res << endl;
		else
			cout << "NO" << endl;
		
	}
	return 0;
}


