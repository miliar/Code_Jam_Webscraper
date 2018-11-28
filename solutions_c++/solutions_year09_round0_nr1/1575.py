#include <assert.h>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <limits>
#include <utility>
#include <stdlib.h>

using namespace std;

class Dict;
struct Dict : public map<char, Dict>
{};

Dict dict;

typedef set<char>       CharSet;
typedef vector<CharSet> InputWord;

size_t solve(Dict& dict, const InputWord& iword, size_t idx = 0, string word=string(""))
{
    if (idx >= iword.size())
    {
        clog << " " << word << endl;
        return 1;
    }

    size_t result = 0;

    for (CharSet::const_iterator it=iword[idx].begin();
         it != iword[idx].end();
         ++it)
    {
        if (dict.count(*it) > 0)
            result += solve(dict[*it], iword, idx+1, word + *it);
    }

    return result;
}

int main(int argc, const char* argv[])
{
    clog.rdbuf(NULL);

    fstream fs(argv[1]);

    if (!fs)
        return 1;

    string line;

    size_t wordLen;
    size_t dictSize;
    size_t caseCount;

    fs >> wordLen >> dictSize >> caseCount;
    getline(fs,line);

    clog << "WordLen:" << wordLen << " DictSize:" << dictSize << " CaseCount:" << caseCount << endl;

    for (size_t i=0; i<dictSize; ++i)
    {
        getline(fs, line);
        assert(line.size() >= wordLen);

        Dict* d = &dict;
        for (size_t j=0; j<wordLen; ++j)
        {
            d = &(*d)[line[j]];
        }
    }

    for (size_t caseNum=1; caseNum<=caseCount; ++caseNum)
    {
        getline(fs,line);

        InputWord   iword;

        clog << "CaseInput #" << caseNum << ": ";
        for (size_t i=0; i<line.size(); ++i)
        {
            CharSet charset;

            if (line[i] != '(')
            {
                charset.insert(line[i]);
                clog << line[i];
            } else
            {
                clog << '(';

                while (line[++i] != ')')
                {
                    charset.insert(line[i]);
                    clog << line[i];
                }

                clog << ')';
            }

            iword.push_back(charset);
        }
        clog << endl;

        size_t result = solve(dict, iword);
        cout << "Case #" << caseNum << ": " << result << endl;
    }

    return 0;
}
