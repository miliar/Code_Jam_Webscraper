#include <iostream>
#include <vector>
using namespace std;
int N, K, n, c[5000], d[100];
int main()
{
    cin >> N;
    for (int t=0; t<N; ++t) {
	cin >> K >> n;
	for (int i=0; i<n; ++i) cin >> d[i];
	fill(c, c+K, 0);
	vector<int> empties(K);
	for (int i=0; i<K; ++i) empties[i] = i;
	int cur=0;
	for (int i=1; i<=K; ++i) {
	    cur = (cur + (i-1)) % empties.size();
	    c[empties[cur]] = i;
	    empties.erase(empties.begin()+cur);
	}
	printf("Case #%d:", t+1);
	for (int i=0; i<n; ++i) 
	    printf(" %d", c[d[i]-1]);
	printf("\n");
    }
}
