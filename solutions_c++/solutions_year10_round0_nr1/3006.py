#include <iostream>
#include <fstream>

using namespace std;

int on[31];

int main()
{
    ofstream fout ("out.txt");
    ifstream fin ("A-large.in");
    int T, t = 1;
    for(int i = 1, j = 1; i < 31; i++)
    {
        if(i > 1)
            j = j * 2;
        on[i] = on[i - 1] + j;
    }
    fin >> T;
    while(T--)
    {
        long long N, K;
        fin >> N >> K;
        if(K == 0)
            fout << "Case #" << t++ << ": OFF" << endl;
        else if(K % (on[N]+1) == on[N])
            fout << "Case #" << t++ << ": ON" << endl;
        else
            fout << "Case #" << t++ << ": OFF" << endl;
    }
    return 0;
}
