#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    
    int num_case;
    int n;
    scanf("%d", &num_case);
    
    for (int cas = 1; cas <= num_case; cas ++){
	scanf("%d", &n);
	vector<int> v1(n), v2(n), p(n);
	for (int i = 0; i < n; i ++){
	    scanf("%d", &v1[i]);
	    p[i] = i;
	}
	for (int i = 0; i < n; i ++){
	    scanf("%d", &v2[i]);
	}
	
	int Min = 2000000000;
	
	do{
	    int s = 0;
	    for (int i = 0; i < n; i ++){
		s += v1[p[i]] * v2[i];
	    }
	    Min = min(Min, s);
	}while (next_permutation(p.begin(), p.end()));

	printf("Case #%d: %d\n", cas, Min);
    }

    return 0;
}

