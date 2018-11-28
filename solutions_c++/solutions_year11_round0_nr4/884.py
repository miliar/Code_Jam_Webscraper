#include <fstream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

ifstream in;



float solve(){
	int n;
	in>>n;

	vector<int> arr (n);
	for( int i = 0; i < n; i++)
		in>>arr[i];

	vector<int> sorted (n);
	vector<int> must (n);
	vector<bool> was (n,false);

	sorted = arr;
	sort( sorted.begin(), sorted.end() );

	for( int i = 0; i < n; i++){
		int val = arr[i];

		int j;
		if( sorted[i]!=val )
			for( j = 0; sorted[j]!=val || was[j] || sorted[j]==arr[j]; j++);
		else 
			j = i;
		must[i] = j;
		was[j] = true;
	}

	was.assign(n,false);

	int res = 0;
	for( int i=0;i<n;i++){
		if( was[i] ) continue;
		int cnt=0;
		int k = i;
		while( must[k]!=i ){
			was[k]=true;
			k = must[k];
			cnt++;
		}
		was[k] = true;
		if( cnt!=0 )
			res+=cnt+1;
	}
	return res;
}

int main(){
	//freopen("D-small.in", "r", stdin);
	freopen("D-small.out", "w", stdout);
	in = ifstream("D-small.in");
	//ofstream out ("D-small.out");*/
	int T;
	in >> T;

	for( int i = 1; i <= T; i++){
		printf("Case #%d: %.6f\n", i, solve() );
		//out.width(5);
		
	}
	//out.close();
	in.close();
}
