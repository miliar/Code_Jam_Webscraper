#include <string.h>
#include <stdio.h>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <stack>
#include <algorithm>
#include <iostream>
#include <string>
#include <bitset>
#include <cstring>
#include <queue>
#include <cmath>
#include <map>
#include <iterator>
#define EPS 1e-9
#pragma comment(linker, "/STACK:256000000")

using namespace std;

void solve(){
	int c,d,n;
	cin>>c;
	char cc[113][3];
	char dd[113][2];
	for (int i=0;i<c;i++){
		cin>>cc[i][0]>>cc[i][1]>>cc[i][2];
	}
	cin>>d;
	for (int i=0;i<d;i++){
		cin>>dd[i][0]>>dd[i][1];
	}
	cin>>n;
	char ch[213];
	int cnt=-1;
	for (int i=0;i<n;i++){
		cnt++;
		cin>>ch[cnt];
		bool pp=0;
		if (cnt>0){
			for (int k=0;k<c;k++){
				if ((ch[cnt]==cc[k][0] && ch[cnt-1]==cc[k][1]) || (ch[cnt]==cc[k][1] && ch[cnt-1]==cc[k][0])){
					cnt--;
					ch[cnt]=cc[k][2];
					pp=1;
					break;
				}
			}
		}
		int left=cnt+1;
		for (int j=0;j<cnt;j++){
			for (int k=0;k<d;k++){
				if ((ch[cnt]==dd[k][0] && ch[j]==dd[k][1]) || (ch[cnt]==dd[k][1] && ch[j]==dd[k][0])){
					left=min(left,j);
				}
			}
		}
		if (left<=cnt){
			cnt=-1;
		}
	}
	cout<<'[';
	if (cnt>=0){
		cout<<ch[0];
		for (int i=1;i<=cnt;i++){
			cout<<", "<<ch[i];
		}
	}
	cout<<']';
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	ios::sync_with_stdio(0);
	int t;
	cin>>t;
	for (int z=1;z<=t;z++){
		cout<<"Case #"<<z<<": ";
		solve();
		cout<<endl;
	}
	return 0;
	//cout.setf(ios::fixed);cout.precision(20);
	}