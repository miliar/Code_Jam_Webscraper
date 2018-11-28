#include <iostream>
#include <stack>
#include <vector>
using namespace std;

vector <int> V[30];
stack <int> S;
int map[30][30];
int hash[30];
char s[150];
int ans[150];

bool checkOpposed(int now)
{
	int size = V[now].size();
	int temp;

	for (int i=0 ; i<size ; i++) {
		temp = V[now][i];
		if (hash[temp] > 0)
			return true;
	}
	return false;
}

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	
	int t;
	int C , D , N;
	int cas = 0;
	int pre , now ;
	int temp;
	int len;

	scanf("%d" , &t);
	while (t--) {
		cas++;

		scanf("%d" , &C);
		memset(map , -1 , sizeof(map));
		for (int i=0 ; i<C ; i++) {
			scanf("%s" , s);
			map[s[0] - 'A'][s[1] - 'A'] = s[2] - 'A';
			map[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
		}	

		scanf("%d" , &D);
		for (int i=0 ; i<30 ; i++) {
			V[i].clear();
		}
		for (int i=0 ; i<D ; i++) {
			scanf("%s" , s);
			V[s[0] - 'A'].push_back(s[1] - 'A');
			V[s[1] - 'A'].push_back(s[0] - 'A');
		}

		scanf("%d" , &N);
		scanf("%s" , s);
		memset(hash , 0 , sizeof(hash));
		while (!S.empty()) {
			S.pop();
		}

		for (int i=0 ; i<N ; i++) {
			
			now = s[i] - 'A';
			if (!S.empty()) {
				pre = S.top();
				S.pop();
				if (map[pre][now] != -1) {
					temp = map[pre][now];
					S.push(temp);
					hash[pre]--;
					continue;
				}
				else {
					S.push(pre);
				}
			}
			
			if (checkOpposed(s[i] - 'A')) {
				memset(hash , 0 , sizeof(hash));
				while (!S.empty()) {
					S.pop();
				}
				continue;
			}
			S.push(now);
			hash[now]++;
		}

		len = 0;
		while (!S.empty()) {
			ans[len++] = S.top();
			S.pop();
		}

		printf("Case #%d: " , cas);
		printf("[");
		for (int i=len - 1 ; i>=0 ; i--) {
			if (i == len - 1) {
				printf("%c" , ans[i] + 'A');
			}
			else {
				printf(", %c" , ans[i] + 'A');
			}
		}
		printf("]");
		printf("\n");
	}

	return 0;
}
