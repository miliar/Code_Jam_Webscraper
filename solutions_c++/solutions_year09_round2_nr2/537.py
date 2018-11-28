#include <cstdio>
#include <cstring>
#include <algorithm>
#include <functional>

using namespace std;

int main(){

    int t, p, tmp, i;
    char n[1000];
    int casno;
    int d[1000], len;

    scanf("%d", &t);
    for (casno = 1; casno <= t; casno ++){
	scanf("%s", n);
	len = strlen(n);
	
	memset(d, 0, sizeof(d));
	for (i = 0; i < len; i ++){
	    d[i] = n[len - 1 -i] - '0';
	}
	
	p = 1;
	while (p < len && d[p] >= d[p-1])
	    p ++;
	if (p == len){
	    len ++;
	    d[p] = 0;
	}

	tmp = d[p];
	for (i = 0; i < p; i ++){
	    if (d[p] == tmp){
		if (d[i] > d[p])
		    swap(d[i], d[p]);
	    }
	    else{
		if (d[i] < d[p] && d[i] > tmp)
		    swap(d[i], d[p]);
	    }
	}
	sort(d, d + p, greater<int>());
	
	printf("Case #%d: ", casno);
	for (i = len - 1; i >= 0; i --){
	    printf("%d", d[i]);
	}
	printf("\n");
    }
    return 0;
}

		
	
	
	
