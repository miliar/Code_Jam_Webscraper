#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <iterator>

#include <map>
#include <cmath>
#include <sstream>
#include <set>
#include <string>
#include <vector>

using namespace std;

#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))


typedef long long ll;//NOTES:int64
typedef unsigned long long ull;//NOTES:uint64




// get line
string gl()
{
    char chGl [1024*1024];
    gets (chGl);
    string gl = chGl;
    return gl;
}
// get line as integer
int gli()
{
    string gli = gl();
    return atoi(gli.c_str());
}








int digit(int x, double d, int base)
{
    int a =floor(x/pow(base, d-1));
    return a % base;
}


int nlength(double x, int base)
{
    return 1+floor(log(x)/log(base));
}

int sum_square_digits (int x, int n, int base)
{
    int total = 0;
    for (int i=1; i<=n; i++)
    {
        int d = digit (x, i, base);
        total += d*d;
    }
    return total;
}


bool happy(int x, int base)
{

set <int> s;
//printf ("%d ", s.count(x));
    int n = nlength(x, base);
    while (s.find(x) == s.end())
    {
//printf ("asdf%d ", x);
s.insert(x);
        n = nlength(x, base);
        x = sum_square_digits(x, n, base);
    }
    return (x==1);
}



int main()
{
    int i, N;
//printf ("%d", (100 == 1));
//printf ("%d", happy(82, 10));
//printf ("%d", nlength(1, 10));
//return 0;
//printf("%d", digit(1000, 2, 10));


    // input output streams
    freopen ("A-small-attempt0.in", "r", stdin);
    freopen ("output.txt", "w", stdout);

    // number of cases
    N=gli();
    if (N < 1)
        printf ("Error: input file not found\n");

//printf ("%d", happy(5, 7));

    // for each case
    for (int caseId=1; caseId<=N; caseId++)
    {

    string line = "";
    ::getline(std::cin,line,'\n');

    std::stringstream lineStream(line);

    int i;
    std::vector<int> values;

    while (lineStream >> i)
        values.push_back(i);

int j=2;
        while(true)
        {
            int sw = 0;
for (int i=0; i<values.size(); i++)
{

    //printf ("%d %d\n", j, values[i]);
    if (!happy(j, values[i])) sw=1;
}

if (sw==0) break;

j++;
        }
        printf ("Case #%d: %d\n", caseId, j);
    }

//printf ("%d", happy(2, 3));


    return 0;
}
