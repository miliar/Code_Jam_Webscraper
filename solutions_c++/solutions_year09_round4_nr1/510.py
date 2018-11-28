#include <iostream> 
#include <sstream> 
#include <cstdlib> 
#include <cstdio> 
#include <cmath> 
#include <memory.h> 
#include <cstring> 
#include <string> 
#include <vector> 
#include <list> 
#include <stack> 
#include <queue> 
#include <map> 
#include <algorithm> 
#include <functional> 
using namespace std; 

template<class T> 
inline T MAX(const T& a, const T& b) {return (a>=b)?a:b;} 
template<class T> 
inline T MIN(const T& a, const T& b) {return (a<=b)?a:b;} 

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n;
		scanf("%d", &n);
		char buffer[100];
		int lasts[100] = {0};
		for (int i = 0; i < n; i++) {
			scanf("%s", buffer);
			lasts[i] = 0;
			for (int j = 0;j  < n; j++) if (buffer[j] == '1') lasts[i] = j;			
		}
		int order[100];
		for (int i = 0; i < n; i++) order[i] = -1;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (order[j] != -1) continue;
				if (lasts[j] <= i) {
					order[j] = i;
					break;
				}
			}
		}
		int res = 0;
		for (int i = 0; i < n; i++) {
			for (int j = i+1; j < n; j++) {
				if (order[j] < order[i]) res++;
			}
		}

		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
