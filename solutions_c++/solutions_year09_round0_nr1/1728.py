#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <vector>
#include <cassert>

using namespace std;

typedef vector<char> vc;

set<string> dictionary;

int CountWords(vector<vc> & tokens,string builded,int i=0)
{
    if (i == tokens.size()) return dictionary.find(builded) != dictionary.end();
    //In process test
    set<string>::iterator next = dictionary.lower_bound(builded);
    if (next == dictionary.end()) return 0;
    string cut =  (*next).substr(0,builded.size());
    if (cut.compare(builded) != 0) return 0;

    int res=0;
    for (int j=0;j < tokens[i].size();++j)
        res+=CountWords(tokens,builded+tokens[i][j],i+1);
    return res;
}

int DoCase(string word)
{
    vector<vc> tokens;
    bool bInsideComma = false;
    vc tmp;
    for (string::iterator iter = word.begin();iter != word.end();++iter)
    {
        char c = *iter;
        if (c == '(')
        {
            assert(!bInsideComma);
            bInsideComma=true;
            continue;
        }
        if (c == ')')
        {
            assert(bInsideComma);
            bInsideComma=false;
            tokens.push_back(tmp);
            tmp.clear();
            continue;
        }
        if (bInsideComma) tmp.push_back(c);
        else
        {
            vc tmp2;
            tmp2.push_back(c);
            tokens.push_back(tmp2);
        }
    }
    assert(bInsideComma == false);
    return CountWords(tokens,string());

}

int main (int argc,char * argv[])
{
    int L,D,N;
    cin >> L >> D >> N;
    for (int i=0;i < D;++i)
    {
        string str;
        cin >> str;
        assert(str.size() == L);
        dictionary.insert(str);
    }
    for (int i=0;i < N;++i)
    {
        string c;
        cin >> c;
        cout << "Case #" << i+1 << ": " << DoCase(c) << endl;
    }
    return 0;
}
