#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int main()
{
    int N, x, m[1002][2], i, j, s1, s2, S1, S2, MAX, T, CASE;


fin >> T;
for (CASE=1; CASE <= T; CASE++)
{

    fin >> N;
    for (i=1; i<=N; i++)
    {
        fin >> m[i][0];
        m[i][1]=0;
    }
    m[N+1][1]=0;

    m[1][1]=1; MAX=0;
    while (m[N+1][1]!=1)
    {
        s1=-1; s2=-1; S1=0; S2=0;

        for (j=1; j<=N; j++)
        {
            if (m[j][1]==1)
            {
                if (s1==-1)
                    s1=m[j][0];
                else
                    s1^=m[j][0];
                S1+=m[j][0];
            }
            else
            {
                if (s2==-1)
                    s2=m[j][0];
                else
                    s2^=m[j][0];
                S2+=m[j][0];
            }
        }
        if (s1==s2)
        {
            if ((MAX<=S1)||(MAX<=S2))
                if (S1>S2)
                    MAX=S1;
                else
                    MAX=S2;
        }


        m[1][1]++;
        for (j=1; j<=N; j++)
            if (m[j][1]==2)
            {
                m[j][1]=0;
                m[j+1][1]++;
            }
    }

    fout << "Case #" << CASE << ": ";

    if (MAX>0)
        fout << MAX;
    else
        fout << "NO";

    fout << endl;

}

//x=1^2; cout << x;

    return 0;
}
