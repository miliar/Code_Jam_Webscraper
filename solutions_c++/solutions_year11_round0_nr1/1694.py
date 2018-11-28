#include<iostream>
using namespace std;
int main() {
	int t;
	freopen("A-large.in","r",stdin);
	freopen("A-large.OUT","w",stdout);
	cin >> t;
	
	for(int cas = 1; cas <= t;cas ++) {
		int n;
		cin >> n;
		int ans =0;
		int ox = 1;
		int ot = 0;
		int bx = 1;
		int bt = 0;
		for(int i = 0;i < n ; i ++) {
			char ch ;
			int x ;
			cin >> ch >> x;
			if (ch == 'O') {
				ot += abs(x-ox);
				if (ot < ans) ot = ans;
				else ans = ot;
				ans ++;
				ot ++;
				ox = x;
			} else  {
				bt +=abs(x-bx);
				if(bt<ans) bt= ans;
				else ans = bt;
				ans ++;
				bt ++;
				bx = x;
			}
			
		}
		cout <<"Case #"<<cas<<": "<< ans << endl;
		
	}
	return 0;
}
