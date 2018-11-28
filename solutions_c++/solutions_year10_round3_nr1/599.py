#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>

using namespace std;

struct point
{
       int x, y;
};

int main()
{
ifstream in("A-small.in");
ofstream out("A-small.out");
long long T, N;
in >> T;
    for (long long Q=1; Q <= T; Q++)
    {
        in >> N;
        point VALUES[N];
        long long count=0;
        for (long long i=0; i < N; i++)
        {
            in >> VALUES[i].x >> VALUES[i].y;
        }
        
        for (long long i=0; i < N; i++)
        {
            for (long long j=i; j < N; j++)
            {
                if (i!=j)
                {
                    if ( (VALUES[i].x > VALUES[j].x) && (VALUES[i].y < VALUES[j].y) )
                       count++;
                    else if ( (VALUES[i].x < VALUES[j].x) && (VALUES[i].y > VALUES[j].y) )   
                         count++;
                }
            }
        }
        out << "Case #" << Q << ": " << count << endl;
    }
//8    system("pause");
    return 0;
}

