#include<iostream>
using namespace std;

int M;
int tree[10001];
int changable[10001];
int dp[10001][2];

int recur(int node, int value){
	if(dp[node][value] != -2){
		return dp[node][value];
	}
	if(node > M/2){
		/*-- leaf node --*/
		if(value == tree[node]) return 0;
		else return -1;
	}
	else{
		int min_step = INT_MAX;
		int leftans;
		int rightans;
		/*-- case and --*/
		if(tree[node] == 1){
			if(value == 1){
				/*-- case both 1 --*/
				leftans = recur(node*2, 1);
				rightans = recur(node*2 + 1, 1);
				if(rightans != -1 && leftans != -1){
					if(min_step >= rightans + leftans){
						min_step = rightans + leftans;
					}
				}
				/*-- case change to or --*/
				if(changable[node] == 1){
					/*-- case 1 and 0 --*/
					leftans = recur(node*2, 1);
					rightans = recur(node*2 + 1, 0);
					if(rightans != -1 && leftans != -1){
						if(min_step >= leftans + rightans + 1){
							min_step = rightans + leftans + 1;
						}
					}
					/*-- case 0 and 1 --*/
					leftans = recur(node*2, 0);
					rightans = recur(node*2 + 1, 1);
					if(rightans != -1 && leftans != -1){
						if(min_step >= leftans + rightans + 1){
							min_step = rightans + leftans + 1;
						}
					}
				}
			}
			if(value == 0){
				/*-- case both 0 --*/
				leftans = recur(node*2, 0);
				rightans = recur(node*2 + 1, 0);
				if(rightans != -1 && leftans != -1){
					if(min_step >= rightans + leftans){
						min_step = rightans + leftans;
					}
				}
				/*-- case 1 and 0--*/
				leftans = recur(node*2, 1);
				rightans = recur(node*2 + 1, 0);
				if(rightans != -1 && leftans != -1){
					if(min_step >= rightans + leftans){
						min_step = rightans + leftans;
					}
				}
				/*-- case 0 and 1 --*/
				leftans = recur(node*2, 0);
				rightans = recur(node*2 + 1, 1);
				if(rightans != -1 && leftans != -1){
					if(min_step >= rightans + leftans){
						min_step = rightans + leftans;
					}
				}
			}
		}
		/*-- case or --*/
		else if(tree[node] == 0){
			if(value == 0){
				/*-- case both 0 --*/
				leftans = recur(node*2, 0);
				rightans = recur(node*2 + 1, 0);
				if(rightans != -1 && leftans != -1){
					if(min_step >= rightans + leftans){
						min_step = rightans + leftans;
					}
				}
				/*-- case change to and --*/
				if(changable[node] == 1){
					/*-- case 1 and 0 --*/
					leftans = recur(node*2, 1);
					rightans = recur(node*2 + 1, 0);
					if(rightans != -1 && leftans != -1){
						if(min_step >= leftans + rightans + 1){
							min_step = rightans + leftans + 1;
						}
					}
					/*-- case 0 and 1 --*/
					leftans = recur(node*2, 0);
					rightans = recur(node*2 + 1, 1);
					if(rightans != -1 && leftans != -1){
						if(min_step >= leftans + rightans + 1){
							min_step = rightans + leftans + 1;
						}
					}
				}
			}
			if(value == 1){
				/*-- case both 1 --*/
				leftans = recur(node*2, 1);
				rightans = recur(node*2 + 1, 1);
				if(rightans != -1 && leftans != -1){
					if(min_step >= rightans + leftans){
						min_step = rightans + leftans;
					}
				}
				/*-- case 1 and 0--*/
				leftans = recur(node*2, 1);
				rightans = recur(node*2 + 1, 0);
				if(rightans != -1 && leftans != -1){
					if(min_step >= rightans + leftans){
						min_step = rightans + leftans;
					}
				}
				/*-- case 0 and 1 --*/
				leftans = recur(node*2, 0);
				rightans = recur(node*2 + 1, 1);
				if(rightans != -1 && leftans != -1){
					if(min_step >= rightans + leftans){
						min_step = rightans + leftans;
					}
				}
			}
		}
		if(min_step == INT_MAX){
			return dp[node][value] = -1;
		}
		else{
			return dp[node][value] = min_step;
		}
	}
}

int main(){
	int N;
	cin >> N;
	for(int times = 1; times <= N; times++){
		int V;
		cin >> M >> V;
		for(int i = 0; i < 10001; i++){
			tree[i] = 0;
			changable[i] = 0;
			dp[i][0] = -2;
			dp[i][1] = -2;
		}
		for(int i = 1; i <= M/2; i++){
			cin >> tree[i] >> changable[i];
		}
		for(int i = M/2 + 1; i <= M; i++){
			cin >> tree[i];
		}
		cout << "Case #" << times << ": ";
		int ans = recur(1, V);
		if(ans == -1) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
	return 0;
}
