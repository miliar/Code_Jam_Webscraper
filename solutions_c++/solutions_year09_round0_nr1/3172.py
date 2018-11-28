#include <vector>
#include <string>
#include <fstream>
#include <iostream>
using namespace std;

class AlienToken
{
public:
    AlienToken(char   t) : token(1,t) { }
    AlienToken(string t) : token(t)   { }

    bool match(char l)
    {
        return (token.find(l) != string::npos);
    }

    string token;
};

int main(int argc, char** argv)
{
    if(argc != 2)
    {
        cerr << "Missing input data file." << endl;
        return 0;
    }

    ifstream input(argv[1]);
    if(!input.is_open())
    {
        cerr << "Failed to open input data file (" << argv[1] << ")" << endl;
        return 0;
    }

    ofstream output("out.txt");

    int L,D,N;
    input >> L >> D >> N;

    vector<string> dic;
    for(int d = 0; d < D; d++)
    {
        string tmp;
        input >> tmp;
        dic.push_back(tmp);
    }

    for(int n = 1; n <= N; n++)
    {
        string pattern;

        input >> pattern;

        vector<AlienToken> tokens;

        for(unsigned int c = 0; c < pattern.length(); c++)
        {
            if(pattern[c] != '(')
            {
                tokens.push_back(pattern[c]);
            }
            else
            {
                unsigned int closing = pattern.find(')',c);
                tokens.push_back(pattern.substr(c+1,closing-c-1));
                c = closing;
            }
        }

        int caseTotal = 0;
        for(unsigned int iDic = 0; iDic < dic.size(); iDic++)
        {
            int l;
            for(l = 0; l < L; l++)
            {
                if(!tokens[l].match(dic[iDic][l]))
                    break;
            }
            if(l == L)
                caseTotal++;
        }

        output << "Case #" << n << ": " << caseTotal << endl;
    }

    input.close();
    output.close();

    return 0;
}
