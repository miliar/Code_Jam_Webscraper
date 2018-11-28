#include<iostream>
#include<algorithm>
#include<string>
#include<cstdio>
#include<vector>
#define REP(j,n) for(int j=0;j<(n);j++)

using namespace std;
int main(){
	int l,n,c;
	long long t;
	int temp;
	int cases,i=0;
	cin >> cases;
	while( i++<cases ){
		cin >> l >> t >> n >> c;
	//	cout << l << t << n << c;
		vector<int> a;
		REP(j,c){
			cin>>temp;
			a.push_back(temp);
		}
		cout << "Case #"<<i<<": ";
		
		vector<int> x;
		REP(i,n){
			x.push_back(a[i%c]);
		}
		vector<long long> p;
		int flag=0;
		long long total=0;
		REP(i,n){
			total+=x[i];
			if(total*2>t){
				if(flag==0){
					p.push_back(total-t/2);
					flag=1;
				}
				else{
					p.push_back(x[i]);
				}
			}
		}
		sort(p.begin(),p.end());
		reverse(p.begin(),p.end());
		double r=0.0;
		int psize=p.size();
		REP(i,min(l,psize)){
			r+=p[i];
		}
		cout << (long long)(2*total-r)<<endl;
	}
	return 0;
}


