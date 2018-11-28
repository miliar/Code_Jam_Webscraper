#include <iostream>
using namespace std;
char key[100][100];
char tp[100][100];
int m,n;
void rote() {
	int i,j;
	memset(tp, 0, sizeof(tp));
	for (i=0;i<m;++i) {
		for (j =0;j<m;++j) {
			tp[i][j] = key[m - j - 1][i];
		}
		tp[i][m] = '\0';
	}
	memcpy(key, tp, sizeof(key));
}

void gravit() {
	int i, j, len;
	memset(tp, '.', sizeof(tp));
	for (i = 0; i < m; ++i) {
		len = m - 1;
		for (j = m-1; j>=0; --j) {
			if (key[j][i] != '.') {
				tp[len--][i] = key[j][i];
			}
		}
	}
	for (i =0 ;i < m ;++i) {
		tp[i][m] = '\0';
	}
	memcpy(key, tp, sizeof(key));
}

bool check(char x) {
	int i,j,k;
	for (i = 0; i < m ; ++i) {
		for (j = 0; j < m ; ++j) {
			if (key[i][j] == x) {
				int ct = 1;
				for (k=j +1 ;k < m; ++k) {
					if (key[i][k] == x) {
						++ct;
					} else {
						break;
					}
				}
				for (k=j -1 ;k >= 0; --k) {
					if (key[i][k] == x) {
						++ct;
					} else {
						break;
					}
				}
				if (ct >= n) {
					return true;
				}

				ct = 1;
				for (k=i+1 ;k < m; ++k) {
					if (key[k][j] == x) {
						++ct;
					} else {
						break;
					}
				}
				for (k=i-1 ;k >= 0; --k) {
					if (key[k][j] == x) {
						++ct;
					} else {
						break;
					}
				}
				if (ct >= n) {
					return true;
				}

				ct = 1;
				int l;
				for (k=i+1,l=j+1;k < m && l< m; ++k, ++l) {
					if (key[k][l] == x) {
						++ct;
					} else {
						break;
					}
				}
				for (k=i-1,l=j-1;k>=0 && l>=0; --k, --l) {
					if (key[k][l] == x) {
						++ct;
					} else {
						break;
					}
				}
				if (ct >= n) {
					return true;
				}

				ct = 1;
				for (k=i+1,l=j-1;k < m && l>=0; ++k, --l) {
					if (key[k][l] == x) {
						++ct;
					} else {
						break;
					}
				}
				for (k=i-1,l=j+1;k>=0 && l<m; --k, ++l) {
					if (key[k][l] == x) {
						++ct;
					} else {
						break;
					}
				}
				if (ct >= n) {
					return true;
				}
			}
		}
	}
	return false;
}

int main() {
	int T;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	int b;
	for (b = 1; b <= T; ++b) {
		scanf("%d%d",&m,&n);
		gets(key[0]);
		int i;
		for (i=0;i<m;++i) {
			gets(key[i]);
		}
		rote();

		gravit();

		bool red = check('R');
		bool blue = check('B');

		printf("Case #%d: ",b);
		if (red && blue) {
			puts("Both");
		} else if (red) {
			puts("Red");
		} else if (blue) {
			puts("Blue");
		} else {
			puts("Neither");
		}

	}
	return 0;
}