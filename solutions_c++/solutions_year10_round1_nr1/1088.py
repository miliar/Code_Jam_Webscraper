#include <cstdio>

int main() {
  freopen("in.in", "r", stdin);
  freopen("output.out", "w", stdout);

  int caseCount;
  scanf("%d", &caseCount);
  int n, k;
  char g[51][51];
  for (int caseNum = 1; caseNum <= caseCount; caseNum++) {
    int res = 0;
    int rb = 0; int rr = 0;
  	scanf("%d%d", &n, &k);
  	for (int i = 0; i < n; i++)
	  scanf("%s", g[i]);
    for (int i = 0; i < n; i++) {
      int c = n-1;
      for (int j = n-1; j >= 0; j--)
        if (g[i][j] != '.') {
        	char tmp = g[i][j];
        	g[i][j] = '.';
        	g[i][c] = tmp;
        	c--;
        }
    }
    int b, r;
    for (int i = 0; i < n; i++) {
    	b = 0; r = 0;
	    for (int j = 0; j < n; j++) {
    		if (g[i][j] == '.') {
		    	b = 0; r = 0;
		    } else if (g[i][j] == 'R') {
    			r++; b = 0;
    		} else {
		    	b++; r = 0;
		    }
		    if (b == k)
		    	rb = 1;
	    	if (r == k)
    	 		rr = 2;
    	}
    }
    for (int j = 0; j < n; j++) {
    	b = 0; r = 0;
	    for (int i = 0; i < n; i++) {
    		if (g[i][j] == '.') {
		    	b = 0; r = 0;
		    } else if (g[i][j] == 'R') {
    			r++; b = 0;
    		} else {
		    	b++; r = 0;
		    }
		    if (b == k)
		    	rb = 1;
	    	if (r == k)
    	 		rr = 2;
    	}
    }
    // diag from here
    for (int p = 0; p < 2*n; p++) {
    	b = 0; r = 0;
    	int i, j;
	    for (i = p, j = 0; i >= 0 && j < n; i--, j++) {
	    	if (i >= n)
	    		continue;
    		if (g[i][j] == '.') {
		    	b = 0; r = 0;
		    } else if (g[i][j] == 'R') {
    			r++; b = 0;
    		} else {
		    	b++; r = 0;
		    }
		    if (b == k)
		    	rb = 1;
	    	if (r == k)
    	 		rr = 2;
    	}
    }
    for (int p = -n; p < n; p++) {
    	b = 0; r = 0;
    	int i, j;
	    for (i = 0, j = p; i < n && j < n; j++, i++) {
	    	if (j < 0)
	    		continue;
    		if (g[i][j] == '.') {
		    	b = 0; r = 0;
		    } else if (g[i][j] == 'R') {
    			r++; b = 0;
    		} else {
		    	b++; r = 0;
		    }
		    if (b == k)
		    	rb = 1;
	    	if (r == k)
    	 		rr = 2;
    	}
    }
  	printf("Case #%d:", caseNum);
  	res = rb + rr;
  	switch(res) {
	  	case 0:
	  	printf(" Neither\n");
	  	break;
	  	case 1:
	  	printf(" Blue\n");
	  	break;
	  	case 2:
	  	printf(" Red\n");
	  	break;
	  	case 3:
	  	printf(" Both\n");
	  	break;
	  }
  }

  fclose(stdin);
  fclose(stdout);
}
