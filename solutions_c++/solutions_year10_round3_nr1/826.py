#include <iostream>
#include <queue>
#include <deque>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
//33507885
//
int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int t;
	cin>>t;
	int n;
	pair <int, int> a[1013];
	for(int ii=0; ii<t; ii++){
		cin>>n;
		for(int i=0; i<n; i++){
			cin>>a[i].first>>a[i].second;
		}
		sort(a,a+n);
		int cnt=0;
		for(int i=0; i<n; i++){
			for(int j=i+1; j<n; j++){
				if(a[i].second>a[j].second){
					cnt++;
				}
			}
		}
		cout<<"Case #"<<ii+1<<": "<<cnt<<endl;
	}
	return 0;
}