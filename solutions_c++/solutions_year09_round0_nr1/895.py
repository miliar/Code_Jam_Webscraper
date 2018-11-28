#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>
#include <cassert>
#include <string>
#include <set>

using namespace std;

const int dmax = 5001;
const int lmax = 16;

char w[dmax][lmax];
set < char > u[lmax];
int L, n, D;
string s;


int main()
{
	scanf("%d%d%d\n", &L, &D, &n);
	for (int i = 0; i < D; ++i)
	{
		for (int j = 0; j < L; ++j)
			w[i][j] = fgetc(stdin);
		scanf("\n");
	}
    for (int k = 0; k < n; ++k)
    {
    	cin >> s;
      	int q = 0;
       	for (int p = 0; p < L; ++p, ++q)
        {
        	u[p].clear();
			if (s[q] == '(')
            {
            	while (s[++q] != ')') u[p].insert(s[q]);
            }
            else
            	u[p].insert(s[q]);
        }

        int ret = 0;
        for (int i = 0; i < D; ++i)
        {
        	bool good = true;
        	for (int j = 0; j < L; ++j)
        		if (u[j].count(w[i][j]) == 0)
        		{
        			good = false;
        			break;
        		}
           if (good) ret++;
        }

        printf("Case #%d: %d\n", k + 1, ret);
    }

	return 0;
}
