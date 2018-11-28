#include <iostream>
#include <map>
#include <string>
#include <fstream>
#include <cstdlib>
#include <sstream>

using namespace std;

int main()
{
    int T, N, S, p, t, m;
    string buffer;
    
    ifstream fin("B-small-attempt0.in");
    getline(fin, buffer);
    ofstream os;
    os.open("out.txt");
    
    T = atoi(buffer.c_str());
    for (int i = 0; i < T; i++)
    {
        fin>>N>>S>>p;
        m = 0;
        for (int j = 0; j < N; j++)
        {
            fin>>t;
            if (t == 0)
            {
                  if (p == 0)
                     m++;
                  continue;
            }
            if (t == 1)
            {
                  if (p <= 1)
                     m++; 
                  continue;
            }
            if (t == 2)
            {
                  if (p <= 1)
                     m++;
                  continue;
            }
            if (t >= 28)
            {
                  m++;
                  continue;
            }
            if (t % 3 == 0)
            {
                  if (p <= t / 3)
                  {
                        m++;
                        continue;
                  }
                  if (p <= t / 3 + 1 && S > 0)
                  {
                        S--;
                        m++;
                        continue;
                  }
            }
            if (t % 3 == 1)
            {
                  if (p <= t / 3 + 1)
                  {
                        m++;
                        continue;
                  }
            }
            if (t % 3 == 2)
            {
                  if (p <= t / 3 + 1)
                  {
                        m++;
                        continue;
                  }
                  if (p == t / 3 + 2 && S > 0)
                  {
                        m++;
                        S--;
                        continue;
                  }
            }
        }
        os<<"Case #"<<i+1<<": "<<m;
        if (i < T - 1) os<<endl;
    }
    os.close();
    
    return 0;
}
