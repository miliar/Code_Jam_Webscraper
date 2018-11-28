#include <stdio.h>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <vector>

#include <time.h>
#include <sys/time.h>

using namespace std;

bool solve(int n,int pd, int pg)
{
    struct timeval tv;
    gettimeofday(&tv, NULL);
    int i;

    int *kd = (int *)malloc(n * sizeof(int));
    int s = 0;
    for (i = 1; i <= n; ++i) {
	if (i * pd % 100 != 0) {
	    continue;
	}
	kd[s] = i;
	s++;
    }
    
    bool found = false;
    for (i = n; i < 1000*1000*10; ++i) {
	if (i * pg % 100 != 0) {
	    continue;
	}
	int j;
	int g = i;
	int wg = i * pg / 100;
	int lg = g - wg;
	for (j = 0; j < s; ++j) {
	    int d = kd[j];
	    int wd = kd[j] * pd / 100;
	    int ld = d - wd;
	    if (d > g || wd > wg || ld > lg) {
		continue;
	    }
	    printf("%4d %4d %4d d = (%4d, %4d, %4d) , g = (%4d, %4d, %4d)\n", n, pd, pg, 
		   d, wd, ld,
		   g, wg, lg);
	    found = true;
	    goto end;
	}
    }
 end:
    free(kd);
    return found;
}

int main(int argc, char *argv[])
{
    FILE *fpi, *fpo;
    char buff[80];
    strcpy(buff, argv[1]);
    strcat(buff, ".input");
    fpi = fopen(buff, "r");
    if (!fpi) {
	perror("input error");
	exit(1);
    }
    strcpy(buff, argv[1]);
    strcat(buff, ".output");
    fpo = fopen(buff, "w");
    if (!fpo) {
	perror("output error");
	exit(1);
    }
    int t;
    fscanf(fpi, "%d\n", &t);
    printf("t=%d\n", t);
    int i;
    for (i = 0; i < t; ++i) {
	int n, pd, pg;
	fscanf(fpi, "%d %d %d", &n, &pd, &pg);
	bool result = solve(n, pd, pg);
	fprintf(fpo, "Case #%d: %s\n", i+1, result ? "Possible" : "Broken");
	printf("Case #%d: %s\n", i+1, result ? "Possible" : "Broken");
    }
    fclose(fpi);
    fclose(fpo);
}
    
