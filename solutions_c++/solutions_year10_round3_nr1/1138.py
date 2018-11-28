/*
 * Rope Intranet
 */
#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

const int maxn = 1000+5;
int A[maxn],B[maxn];
int idx[maxn];
int N;

void Input(){
	cin >> N;

	for(int i = 0;i<N;i++){
		idx[i] = i;
		cin >> A[i] >> B[i];
	}
}

bool cmp(int a,int b){
	return A[a]<A[b];
}

int Solve(){
	Input();

	sort(idx,idx+N,cmp);

	/*
	for(int i = 0;i<N;i++){
		cout << idx[i] << " " ;
	}
	cout << endl;
	*/

	int ans = 0;

	for(int i = 0;i<N;i++){
		for(int j = i-1;j>=0;j--){
			if(B[idx[j]]>B[idx[i]]){
				ans++;
				//cout << idx[i] << " " << idx[j] << endl;
			}
		}
	}

	return ans;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int n;
	cin >> n;

	for(int i = 1;i<=n;i++){
		cout << "Case #" << i << ": " << Solve() << endl;
	}

	return 0;
}
