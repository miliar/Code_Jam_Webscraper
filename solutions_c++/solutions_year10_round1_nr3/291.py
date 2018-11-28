#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <queue> 
#include <cstring> 
using namespace std;

int main(){
	int T, ca=0;
	scanf("%d", &T);
	while (T--){
		printf("Case #%d: ", ++ca);
		int A1, A2, B1, B2, res=0;
		scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
		for (int i = A1; i <= A2; ++i)
			for (int j = B1; j <= B2; ++j){
				vector<int> layout;
				int a = max(i, j), b = min(i, j), c;
				while(b){
					layout.push_back(a/b);
					c = a%b;
					a = b;
					b = c;
				}
				int N = layout.size();
				if (layout.back() == 1){
					N--;
					layout.pop_back();
					vector<bool> fW(N+1);
					for (int k = N-1; k >= 0 ; --k)
						layout[k] == 1 ?fW[k] = !fW[k+1]: fW[k] = true;
					if (fW[0]) res++;
				}else{
					vector<bool> fW(N+1);
					for (int k = N-1; k >= 0 ; --k)
						layout[k] == 1 ?fW[k] = !fW[k+1]: fW[k] = true;
					if (fW[0]) res++;
				}
			}
			printf("%d\n", res);
	}
	return 0;
}
