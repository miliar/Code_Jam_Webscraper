#include <iostream>
#include <string>
#include <vector>

typedef unsigned int uint;
using namespace std;

int L,D,N;

char ** _matrix;

int calc(vector<string> possChars, vector<int> possRows)
{
    int col = L - possChars.size();
    string rowS = *possChars.begin();

    if(possChars.size() == 1)
    {
        int result = 0;
        for (uint i=0 ; i<rowS.length() ; i++)
        {
            vector<int>::iterator it;
            for (it=possRows.begin() ; it<possRows.end() ; it++)
                if(_matrix[*it][col] == rowS[i])
                    result++;
        }
        return result;
    }
    else
    {
        vector<int> newRows;
        for (uint i=0 ; i<rowS.length() ; i++)
        {
            vector<int>::iterator it;
            for (it=possRows.begin() ; it<possRows.end() ; it++)
            {
                if(_matrix[*it][col] == rowS[i])
                {
                    newRows.push_back(*it);
                }
            }
        }
        possChars.erase(possChars.begin());

        return calc(possChars, newRows);
    }
}

int solve()
{
    vector<string> possChars;

    char c_pattern[500];
    fscanf(stdin, "%s\n", c_pattern);
    string pattern = c_pattern;

    int currentChar = 0;
    bool par = false;
    for (uint i=0 ; i<pattern.length() ; i++)
    {
        if(pattern[i] == '(')
        {
            par = true;
            string str;
            possChars.push_back(str);
            continue;
        }
        if (pattern[i] == ')')
        {
            par = false;
            currentChar++;
            continue;
        }
        if (par)
        {
            possChars[currentChar].push_back(pattern[i]);
        }
        else
        {
            string ch;
            ch.push_back(pattern[i]);
            possChars.push_back(ch);
            currentChar++;
        }
    }

    vector<int> rows;
    for (int i=0 ; i<D ; i++ ) rows.push_back(i);

    return calc(possChars, rows);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.txt", "w", stdout);

    scanf("%d%d%d\n", &L, &D, &N);

    _matrix = new char*[D];

    for (int i=0 ; i<D ; i++)
    {
        _matrix[i] = new char[L];
        for(int j=0 ; j<L ; j++)
        {
            char ch;
            while((ch = getchar()) == '\n');
            _matrix[i][j] = ch;
        }
    }

    for (int caseId = 1 ; caseId <= N ; caseId++)
    {
        printf("Case #%d: ", caseId);
        int res = solve();
        printf("%d\n", res);
        fflush(stdout);
    }
}
