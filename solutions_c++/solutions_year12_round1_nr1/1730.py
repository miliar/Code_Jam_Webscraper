#include <cstdlib>  
#include <cctype>  
#include <cstring>  
#include <cstdio>  
#include <cmath>  
#include <algorithm>  
#include <vector>  
#include <string>  
#include <iostream>  
#include <sstream>  
#include <map>  
#include <set>  
#include <queue>  
#include <stack>  
#include <fstream>  
#include <numeric>  
#include <iomanip>  
#include <bitset>  
#include <list>  
#include <stdexcept>  
#include <functional>  
#include <utility>  
#include <ctime>  
using namespace std;  

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, cases, a, b;
	float cor[10];
	float ps[10];
	int   h[10];

	scanf("%d", &T);
	cases = 0;
	while(cases++ < T){
		scanf("%d%d", &a, &b);

		ps[0] = 1.0;
		for(int i=1; i<=a; i++){
			scanf("%f", &cor[i]);
			ps[i]= ps[i-1] * cor[i];
		}

		float tmp;
		float ans = 2 + b;
		for(int i=0; i<=a; ++i){
			tmp = i + i + b - a + 1 + (1.0 - ps[a-i]) * (b + 1);
			if(tmp < ans)
				ans = tmp;
		}

		printf("Case #%d: %f\n", cases, ans);
	}
}

