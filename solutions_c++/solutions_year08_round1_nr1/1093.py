#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<iostream>

using namespace std;

int main(int argc, char *argv[])
{
    FILE *in = fopen(argv[1], "r");
    FILE *out = fopen(argv[2], "w");
	int ci, cc;

	fscanf(in, "%d\n", &cc);
	for(ci = 0; ci < cc; ci++){
        vector<int> x, y;
        int n, t;
	    fscanf(in, "%d\n", &n);
        for(int i = 0; i < n; i++) {
            fscanf(in, "%d", &t);
            x.push_back(t);
        }
        for(int i = 0; i < n; i++) {
            fscanf(in, "%d", &t);
            y.push_back(t);
        }
        sort(x.begin(), x.end());
        sort(y.begin(), y.end());
        int msp = 0;
        for(int i = 0; i < n; i++) {
            msp += x[i] * y[n-i-1];
        }
        fprintf(out, "Case #%d: %d\n", ci + 1, msp);
	}
    return 0;
}
