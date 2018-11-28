#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int MAX = 50;

int n;
int val[MAX];

int go()
{
	int i, j, k;
	int res = 0;
	for(i = 0; i < n; i++){
		if(val[i] <= i)  continue;
		for(j = i + 1; j < n; j++){
			if(val[j] <= i){
				res += (j - i);
				for(k = j; k >= i + 1; k--){
					swap(val[k], val[k - 1]);
				}
				break;
			}
		}
	}
	return res;
}



int main()
{
	int T;
	int cnt = 0;
	freopen("f://A-large.in", "r", stdin);
	freopen("f://A-large.out", "w", stdout);
	scanf("%d", &T);
	while(T--){
		int i, j;
		cnt++;
		scanf("%d", &n);
		for(i = 0; i < n; i++){
			char t[MAX];
			scanf("%s", t);
			for(j = n - 1; j >= 0; j--){
				if(t[j] == '1'){
					val[i] = j;
					break;
				}
			}
			if(j < 0)  val[i] = -1;
		}
		printf("Case #%d: %d\n", cnt, go());
	}
}