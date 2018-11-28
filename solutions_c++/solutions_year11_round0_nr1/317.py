#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <iterator>
#include <bitset>
#include <sstream>
#include <cmath>
#include <cstring>

using namespace std;
int n;
void work(){
	cin >> n ;
	int OP=1,BP=1,t=0,OT=0,BT=0;
	for (int i=0;i<n;i++){
		char c;
		int pos;
		cin >> c >> pos;
		if (c=='O'){
			int dist=abs(pos-OP);
			int tmp=max(0,dist-OT)+1;
			//cout << tmp <<endl;
			OP=pos;
			t+=tmp;
			BT+=tmp;
			OT=0;
		}else {
			int dist=abs(pos-BP);
			int tmp=max(0,dist-BT)+1;
			//cout << tmp <<endl;
			BP=pos;
			t+=tmp;
			OT+=tmp;
			BT=0;
		}
	}
	cout  << t <<endl;
}


int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;cin >> t;
	for (int i=1;i<=t;i++){
		cout << "Case #"<< i << ": ";
		work();
	}
	//system("pause");
	return 0;
}
