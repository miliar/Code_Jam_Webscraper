#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <math.h>

#define ERROR 1E-6

using namespace std;
FILE* in = fopen("A-small-attempt0.in","r");

int processTestCase()
{
    int n;
    fscanf(in,"%d",&n);

    //cout << "n: " << n << endl;;

    vector<int> x, y;

    int i, j;

    int tmp;
    for(i = 0; i <n; i++)
    {
        fscanf(in,"%d",&tmp);
        x.push_back(tmp);
    }

    for(i = 0; i <n; i++)
    {
        fscanf(in,"%d",&tmp);
        y.push_back(tmp);
    }

    sort(x.begin(),x.end());
    sort(y.begin(),y.end());

    int scalar = 0;
    for(i=0; i<n; i++)
    {
        scalar += (x[i]*y[n-i-1]);
    }

    return scalar;
}

int main()
{

    FILE* outfile = fopen("output.dat","w");

    // test cases number
    int T;
    fscanf(in, "%d", &T);

    //cout << "T: " << T << endl;

    int t;
    // para cada test case
    for(t = 1; t <= T; t++)
    {

        //printf("Case #%d: %d\n",t,processTestCase());
        fprintf(outfile, "Case #%d: %d\n",t,processTestCase());
        //getchar();
    }

    return 0;
}
