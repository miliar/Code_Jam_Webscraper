#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <utility>
#define X first
#define Y second
using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin >> test;
	for(int t=0;t<test;++t){
		int n;
		cin >> n;
		vector < pair<int,int> > m(n);
		for(int i=0;i<n;++i){
			int a,b;
			cin >> a >> b;	
			m[i]=make_pair(a,b);
		}
		sort(m.begin(),m.end());
		int count =0;
		for(int i=0;i<n;++i){
			for(int j=i+1;j<n;++j){
				if((m[i].X - m[j].X) * (m[i].Y - m[j].Y) < 0) ++count;
			}
		}
		cout <<"Case #"<<t+1<<": "<< count <<endl;
	}
	return 0;
}