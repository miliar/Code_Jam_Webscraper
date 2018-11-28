#include <cstdio>
#include <cstdlib>
#include <string>
#include <utility>
#include <set>

using namespace std;

int t, T, NA, NB;
int a, b, hour, minute;
multiset<pair<int, int> > A, B;
multiset<pair<int, int> >::iterator ptr;
int ans_a, ans_b;

int main()
{
	int i, j;
	
	freopen("B.output", "w", stdout);
	
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		A.clear();
		B.clear();
		
		scanf("%d", &T);
		scanf("%d %d", &NA, &NB);
		for (j = 0; j < NA; j++) {
			scanf("%d:%d", &hour, &minute);
			a = 60 * hour + minute;
			scanf("%d:%d", &hour, &minute);
			b = 60 * hour + minute;
			A.insert(make_pair(a, b));
		}
		for (j = 0; j < NB; j++) {
			scanf("%d:%d", &hour, &minute);
			a = 60 * hour + minute;
			scanf("%d:%d", &hour, &minute);
			b = 60 * hour + minute;
			B.insert(make_pair(a, b));
		}
		
		ans_a = ans_b = 0;
		
		while (1) {
			if (A.empty() || B.empty())
				break;
			if (* A.begin() < * B.begin()) {
				ans_a++;
				ptr = A.begin();
				while (1) {
					a = ptr -> second + T;
					b = 0;
					A.erase(ptr);
					ptr = B.lower_bound(make_pair(a, b));
					if (ptr == B.end())
						break;
					
					a = ptr -> second + T;
					b = 0;
					B.erase(ptr);
					ptr = A.lower_bound(make_pair(a, b));
					if (ptr == A.end())
						break;
				}
			} else {
				ans_b++;
				ptr = B.begin();
				while (1) {
					a = ptr -> second + T;
					b = 0;
					B.erase(ptr);
					ptr = A.lower_bound(make_pair(a, b));
					if (ptr == A.end())
						break;
					
					a = ptr -> second + T;
					b = 0;
					A.erase(ptr);
					ptr = B.lower_bound(make_pair(a, b));
					if (ptr == B.end())
						break;
				}
			}
		}
		
		ans_a += A.size();
		ans_b += B.size();
		
		printf("Case #%d: %d %d\n", i + 1, ans_a, ans_b);
	}
	
	return (0);
}
