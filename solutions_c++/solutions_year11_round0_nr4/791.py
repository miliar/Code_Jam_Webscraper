#include <iostream>
#include <cmath>
using namespace std;

int a[1050];
bool hash[1050];



int getNext(int index)
{
	int ret = 0;
	int next;
	next = index;
	while (!hash[next]){
		ret++;
		hash[next] = true;
		next = a[next];
	}

	return ret;
}

int main()
{

	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);

	int t;
	int n;
	int cnt;
	double result;
	bool find;
	int cas = 0;
	
	scanf("%d" , &t);
	while (t--) {
		cas++;
		scanf("%d" , &n);
		for (int i=1 ; i<=n ; i++) {
			scanf("%d" , &a[i]);
		}

		memset(hash , 0 , sizeof(hash));
		result = 0;
		find = true;
		while (find) {
			find = false;
			for (int i=1 ; i<=n ; i++) {
				if (!hash[i]) {
					cnt = getNext(i);
					if (cnt >= 2) {
						result += cnt;
					}
					find = true;
				}
			}
		}

		printf("Case #%d: %.6lf\n" , cas , result);
	}

	return 0;
}
