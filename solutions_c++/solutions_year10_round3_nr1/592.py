#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<math.h>
#include<conio.h>

using namespace std;

struct point
{
       int x, y;
};

int main()
{
    ifstream in("A-large.in");
    ofstream out("A-large.out");
    long long t, n;
    in >> t;
    for (long long a=1; a <= t; a++)
    {
        in >> n;
        point val[n];
        long long counter=0;
        for (long long i=0; i < n; i++)
        {
            in >> val[i].x >> val[i].y;
        }
        
        for (long long i=0; i < n; i++)
        {
            for (long long j=i; j < n; j++)
            {
                if (i!=j)
                {
                    if ( (val[i].x > val[j].x) && (val[i].y < val[j].y) )
                       counter++;
                    else if ( (val[i].x < val[j].x) && (val[i].y > val[j].y) )   
                         counter++;
                }
            }
        }
        out << "Case #" << a << ": " << counter << endl;
    }
    system("pause");
    return 0;
}
