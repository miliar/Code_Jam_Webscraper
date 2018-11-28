#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>

#define INF 100000000
#define MAX 1048576
#define nc (((qc % 2) == 0) ? 1 : 2)

using namespace std;

int a, b, c, d, score = -1, spz, miss, skip, missct;
char dict[10005][15], order[40];
int has[10005][26], len[10005];
int q[10005][3], qs[4], qc;

int main() {
    scanf("%d", &a);
    
    for (int t=0; t<a; t++) {
	scanf("%d%d", &b, &c);
	qc = 0;
	for (int k=0; k<10005; k++) {
	    for (int j=0; j<26; j++) 
		has[k][j] = 0;
	}
	
	    
	for (int i=0; i<b; i++) {
	    q[qs[qc]++][qc] = i;
	    scanf("%s", dict[i]);
	    len[i] = strlen(dict[i]);
	    for (int j=0; j<strlen(dict[i]); j++)
		has[i][dict[i][j] - 'a'] += 50*(j+1)*(j+1)*(j+1)*(j+1);
	}
	printf("Case #%d: ", t+1);
	for (int i=0; i<c; i++) {
	    //alphabets
	    score = -1;
	    scanf("%s", order);
	    for (int j=0; j<b; j++) {
		missct = miss = qc = 0;
		//cout << endl << endl;
		//potential word
		for (int k=0; k<26; k++) {
		    qs[nc] = skip = miss = 0;
		    int trg = order[k] - 'a';
		   // cout << qs[qc] << "!" << endl;
		   if (has[j][trg] <= 15) miss = true;
		    for (int m=0; m<qs[qc]; m++) {
			int index = q[m][qc];
			if (has[index][trg] > 15) skip = 1;
			if (has[j][trg] == has[index][trg] && len[j] == len[index]) {
			    q[qs[nc]++][nc] = index;
			}
		    }
		    if (miss && skip) ++missct;
		    if (skip) qc = nc;
		}
		if (missct > score)
		    score = missct, spz = j;
	    }
	    printf("%s%c", dict[spz], (i == c-1 ? '\n' : ' '));
	}
    }
   
    return 0;
}