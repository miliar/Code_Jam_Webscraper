#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdlib>
#include <utility>
#include <cassert>
#include <cctype>
#include <climits>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
using namespace std;
typedef unsigned int 		uint;
typedef long long			ll;
typedef unsigned long long	ull;
const double	pi			= acos(-1.0);
const double	epsilon		= 1e-9;
const int		large_int	= 2000000000;
const uint 		large_uint	= 4000000000u;
const ll		large_ll	= 9000000000000000000ll;
const ull		large_ull	= 18000000000000000000ull;
const int large = large_int;

FILE *in = fopen("A.in", "r");
FILE *out = fopen("A.out", "w");

int gcd(int a, int b) { 
    return (b ? gcd(b, a%b) : a);
}

int main()
{
    int test_cases;
    fscanf(in, "%d", &test_cases);
    for (int test_id = 1; test_id <= test_cases; test_id++)
    {
        bool possible = true;
        int n, pd, pg, foo;
        fscanf(in, "%d%d%d", &n, &pd, &pg);
        
        foo = gcd(100, pd);
        printf("%d\n", foo);
        
        if (pd == 0 || pd == 100)  possible = true;
        else if ((100 % foo) == 0) possible = (n >= (100 / foo));
        else                       possible = (n >= 100);
        
        if ((pg == 0 && pd != 0) ||
            (pg == 100 && pd != 100))
        {
            possible = false;
        }
        
        fprintf(out, "Case #%d: ", test_id);
        fprintf(out, "%s", (possible ? "Possible" : "Broken"));
        fprintf(out, "\n");
    }
    fclose(in);
    fclose(out);
	return 0;
}
