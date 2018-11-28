#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
int vv = 0;
int n;
int sum =0;
int a[1010];
void back(int idx,int bitsumleft,int bitsumright ,int value,int cnt){

	if(bitsumleft == bitsumright && cnt > 0 && cnt != n)
		vv >?= value;
	if(idx == n)
		return ;

	back(idx+1, bitsumleft^a[idx], bitsumright^a[idx], value+ a[idx],cnt+1);
	back(idx+1, bitsumleft, bitsumright, value,cnt);
}
int main()
{
	int kase = 1;
	int t,i;
	cin >> t;

	while(t--){
		vv = -1;
		cin >> n;

		int value =0;
		sum = 0;
		for(i=0;i<n;i++){
			cin >> a[i];
			sum ^= a[i];
		}
		back(0,sum,0,0,0);
		cout <<"Case #"<<kase++<<": ";
		if(vv<0)
			cout <<"NO"<<endl;
		else cout << vv <<endl;
	}
	return 0;
}
