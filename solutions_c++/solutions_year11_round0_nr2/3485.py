#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int tests(0);
    fin >> tests;
    string abc = "QWERASDF";
    for (int test = 1; test <= tests; test++)
    {
        char combine[9][9];
        string destroy[9];
        memset(combine, 0, sizeof(combine));
        int c(0), d(0), n(0);
        fin >> c;
        for (int i = 0; i < c; i++)
        {
            string three;
            fin >> three;
            int i1 = (int)(find(abc.begin(), abc.end(), three[0]) - abc.begin());
            int i2 = (int)(find(abc.begin(), abc.end(), three[1]) - abc.begin());
            combine[i1][i2] = three[2];
            combine[i2][i1] = three[2];
        }
        fin >> d;
        for (int i = 0; i < d; i++)
        {
            string couple;
            fin >> couple;
            int i1 = (int)(find(abc.begin(), abc.end(), couple[0]) - abc.begin());
            int i2 = (int)(find(abc.begin(), abc.end(), couple[1]) - abc.begin());
            destroy[i1] += couple[1];
            destroy[i2] += couple[0];
        }
        string letters;
        fin >> n >> letters;
        string answer;
        for (int i = 0; i < (int)letters.size(); i++)
        {
            if (answer.size() > 0)
            {
                char last = answer[(int)answer.size() - 1];
                int i1 = (int)(find(abc.begin(), abc.end(), last) - abc.begin());
                int i2 = (int)(find(abc.begin(), abc.end(), letters[i]) - abc.begin());
                if (combine[i1][i2] != 0)
                {
                    answer[(int)answer.size() - 1] = combine[i1][i2];
                }
                else
                {
                    bool erase = false;
                    for (int j = 0; j < (int)destroy[i2].size(); j++)
                    {
                        if (find(answer.begin(), answer.end(), destroy[i2][j]) != answer.end())
                        {
                            erase = true;
                            break;
                        }
                    }
                    if (erase)
                    {
                        answer = "";
                    }
                    else
                    {
                        answer += letters[i];
                    }
                }
            }
            else
            {
                answer += letters[i];
            }
        }
        string result;
        for (int i = 0; i < (int)answer.size(); i++)
        {
            if (result.size() > 0)
            {
                result += ", ";
            }
            result += answer[i];
        }
        result = "[" + result + "]";
        fout << "Case #" << test << ": " << result << endl;
    }
    return 0;
}