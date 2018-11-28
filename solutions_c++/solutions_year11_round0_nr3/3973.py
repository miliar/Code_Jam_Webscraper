#include <iostream>

using namespace std;
int bags[1002];
int memo[1002];
int len;
int rec(int indx,int s,int p,unsigned long long mx){
	if( indx >= len ){
		if( s == p && s) return mx;
		return 0;
	}
	return max( rec( indx + 1, s ^ bags[indx],p, mx ),rec( indx + 1, s ,p ^ bags[indx], mx + bags[indx]));
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;

	for( int i = 1 ; i <= t; i++ ){
		cin >> len;
		for( int j = 0; j < len; j++ )cin >> bags[j];
		int ret = rec( 0,0,0,0) ;;
		cout<<"Case #"<<i<<": ";
		if( ret )cout<< ret;
		else cout<< "NO";
		cout <<endl;
	}

}