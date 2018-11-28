#include<iostream>
using namespace std;

int N, D;
int pos[5000];

int main(){

	//freopen("1.in", "rt", stdin);
	freopen("C-small.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);
	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);
	
	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		
		cin >> N;
		memset(pos, -1, sizeof pos);
		int i, j = -1;
		for(i = 1 ; i <= N ; i++){
			for(int k = 0 ; k < i ; k++){
				j = (j+1)%N;
				if(pos[j] != -1)k--;
			}
			pos[j] = i;
		}
		cin >> D;
		cout << "Case #" << t+1 << ":";
		for(i = 0 ; i < D ; i++){
			int d; cin >> d;
			cout << " " << pos[d-1];
		}
		cout << endl;
	}

	return 0;	
}
