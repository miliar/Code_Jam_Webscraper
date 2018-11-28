#include<fstream>
#include<iostream>
#include<vector>
#include<math.h>

using namespace std;

ifstream in("A-large.in");
ofstream out("output.txt");

int T;

int main()
{
    in >> T;
    for(int test = 0; test < T; test++)
    {
        long long N;
        int Pd, Pg;
        in >> N >> Pd >> Pg;
        bool possible = false;
        if((Pg == 100 && Pd == 100) || Pg < 100)
        if((Pg > 0) || (Pd  == 0))
        {
            if(Pd == 0)
                possible = true;
            else
            {
                long long top = Pd, bottom = 100;
                for(int i = 2; i <= 100; i++)
                    while(top % i == 0 && bottom % i == 0)
                    {
                        top /= i;
                        bottom /= i;
                    }
                if(bottom <= N)
                    possible = true;
            }
/*                for(int i = 1; i <= N; i++)
                    if((i*Pd) % 100 == 0)
                    {
                        possible = true;
                        break;
                    }*/
        }
        out << "Case #" << test + 1 << ": " << (possible ? "Possible" : "Broken") << endl;
    }
    return 0;
}
