#include <fstream>

using namespace std;

short getNormalJudgingMax(short score)
{
    switch (score % 3)
    {
        case 0:
            return score / 3;
        case 1:
            return score / 3 + 1;
        case 2:
            return score / 3 + 1;
    }
}

short getSurprizingJudgingMax(short score)
{
    switch (score % 3)
    {
        case 0:
            if (score > 0)
                return score / 3 + 1;
            return 0;
        case 1:
            if (score > 1)
                return score / 3 + 1;
            return 1;
        case 2:
            return score / 3 + 2;
    }
}

short getMaxGooglers(short N, short S, short p, short t[])
{
    short count = 0;
    for (short i = 0; i < N; i++)
    {
        if (getNormalJudgingMax(t[i]) >= p)
        {
            count++;
        }
        else if ((S > 0) && (getSurprizingJudgingMax(t[i]) >= p))
        {
            count++;
            S--;
        }
    }
    return count;
}

int main()
{
    short T;
    short N, S, p;
    short t[100];
    
    ifstream fin ("B_large_input.txt");
    ofstream fout ("B_large_output.txt");
    
    fin >> T;
    
    for (short i = 1; i <= T; i++)
    {
        fin >> N >> S >> p;
        for (short j = 0 ; j < N; j++)
        {
            fin >> t[j];
        }
        fout << "Case #" << i << ": " << getMaxGooglers(N, S, p, t) << "\n";
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
