#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<string> permute(vector<string> str1, string str2, vector<string> knowns);
int caseResult(string strCase, int length, vector<string> knowns);

int main(int argc, char* argv[])
{
    ifstream infile(argv[1]);
    ofstream outfile(argv[2]);

    unsigned int L, D, N;
    infile >> L;
    infile >> D;
    infile >> N;

    vector<string> knownPatterns;
    for (unsigned int i = 0; i < D; ++i)
    {
        string currPattern;
        infile >> currPattern;
        knownPatterns.push_back(currPattern);
    }

    for (unsigned int i = 0; i < N; ++i)
    {
        string currCase;
        infile >> currCase;
        outfile << "Case #" << i+1 << ": " << caseResult(currCase, L, knownPatterns) << endl;
    }

    outfile.close();
    infile.close();
    return 0;
}

int caseResult(string strCase, int length, vector<string> knowns)
{
    vector<string> candidates;

    for (unsigned int j = 0; j < strCase.length(); ++j)
    {
        if (strCase.at(j) == '(')
        {
            string can;
            while (strCase.at(++j) != ')')
            {
                can.push_back(strCase.at(j));
            }
            candidates.push_back(can);
            continue;
        }
        string can;
        can.push_back(strCase.at(j));
        candidates.push_back(can);
    }

    vector<int> indices;
    for (int i = 0; i < candidates.size(); ++i)
    {
        indices.push_back(0);
    }

    int result = 0;

    vector<string> resultCandidates;
    for (int i = 0; i < candidates[0].length(); ++i)
    {
        string tmp;
        tmp.push_back(candidates[0].at(i));
        resultCandidates.push_back(tmp);
    }

    for (int i = 1; i < candidates.size(); ++i)
    {
        resultCandidates = permute(resultCandidates, candidates[i], knowns);
    }

    for (int i = 0; i < knowns.size(); ++i)
    {
        for (int j = 0; j < resultCandidates.size(); ++j)
        {
            if (knowns[i] == resultCandidates[j])
            {
                cout << resultCandidates[j] << endl;
                result++;
            }
        }
    }
    return result;
}

vector<string> permute(vector<string> str1, string str2, vector<string> knowns)
{
    vector<string> return_vector;
    for (int i = 0; i < str1.size(); ++i)
    {
        for (int j = 0; j < str2.length(); ++j)
        {
            string currStr;
            currStr.append(str1[i]);
            currStr.push_back(str2.at(j));

            for (int i = 0; i < knowns.size(); ++i)
            {
                int pos = knowns[i].find(currStr);
                if (pos == 0)
                {
                    return_vector.push_back(currStr);
                }
            }
        }
    }
    return return_vector;
}
