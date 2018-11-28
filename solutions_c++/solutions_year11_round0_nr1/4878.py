#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <map>
using namespace std;

int n, t, x, l = 1, res, tmp;
char z;
pair <char, int> T[110];
map <char, int> M;

int main(){
	scanf ("%d", &t);
	while (t--){
		M['O'] = M['B'] = 1;
		scanf ("%d", &n);
		for (int i = 1; i <= n; i++){
			scanf (" %c %d", &z, &x);
			T[i] = make_pair (z, x); 
		}
		tmp = res = T[1].second;
		M[T[1].first] = T[1].second;
			//printf ("| %d %d |\n", res, tmp);
		for (int i = 2; i <= n; i++){
			//printf ("| %d %d |\n", res, tmp);
			if (T[i].first == T[i-1].first){
				res += abs (T[i].second - T[i-1].second) + 1;
				tmp += abs (T[i].second - T[i-1].second) + 1;
			}
			else{
				res += max (0, abs (T[i].second - M[(T[i].first == 'O') ? 'O' : 'B']) - tmp) + 1;
				tmp = max (0, abs (T[i].second - M[(T[i].first == 'O') ? 'O' : 'B']) - tmp) + 1;
			}
			M[T[i].first] = T[i].second;
		}
		printf ("Case #%d: %d\n", l, res);
		l++;
		res = tmp = 0;
		M.clear();
	}
}
