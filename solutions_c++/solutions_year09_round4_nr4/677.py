#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;
int x[1000], y[1000], r[1000];

double dist(int k){
    int s, t;
    if (k == 0)
	s = 1, t =2;
    else if (k == 1)
	s = 0, t = 2;
    else
	s = 0, t = 1;

    return 0.5 * sqrt(pow((double)(x[s]-x[t]), 2) + pow((double)(y[s]-y[t]), 2)) + 0.5 * (r[s] + r[t]);
}

int main(){

    int numcases;

    scanf("%d", &numcases);



    for (int casno = 1; casno <= numcases; casno ++){
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i ++){
	    scanf("%d %d %d", &x[i], &y[i], &r[i]);
	}

	printf("Case #%d: ", casno);
	if (n == 1){
	    printf("%lf", (double)r[0]);
	}
	else if (n == 2){
	    printf("%lf", (double)max(r[0], r[1]));
	}
	else{
	    double d[1000];
	    for (int i = 0; i < n; i ++)
		d[i] = max(dist(i), (double)r[i]);
	    printf("%lf", *min_element(d, d+n));
	}
	printf("\n");
    }
}

