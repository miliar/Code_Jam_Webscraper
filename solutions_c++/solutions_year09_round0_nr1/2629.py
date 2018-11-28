#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

int solve(string pattern, string word)
{
    int lindex = pattern.find_first_of('(');
    if (lindex == string::npos)
    {
        if (pattern.compare(word) == 0)
            return 1;

        return 0;
    }

    for (int i=0; i<lindex; i++)
    {
        if (pattern[i] != word[i])
        {
            return 0;
        }
    }

    string subword = word.substr(lindex);
        
    int rindex = pattern.find_first_of(')');
    string tmp = pattern.substr(rindex+1);

    int result = 0;
    for (int i=lindex+1; i<rindex; i++)
    {
        string subpattern = pattern.substr(i,1);
        subpattern += tmp;

        result += solve(subpattern, subword);
    }

    return result;
}

void main()
{
    FILE *fp;
    if ((fp = fopen("in.txt", "r")) == NULL)
    {
        return;
    }

    int i,j,l,d,n;
    vector<string> dict;
    vector<string> pattern;

    fscanf(fp, "%d", &l);
    fscanf(fp, "%d", &d);
    fscanf(fp, "%d", &n);

    for (i=0; i<d; i++)
    {
        char str[20];
        fscanf(fp, "%s", str);
        dict.push_back(str);
    }

    for (i=0; i<n; i++)
    {
        char str[1024];
        fscanf(fp, "%s", str);
        pattern.push_back(str);
    }

    if ((fp = fopen("out.txt", "w+")) == NULL)
    {
        return;
    }

    for (i=0; i<n; ++i)
    {
        int sum = 0;
        for (j=0; j<d; ++j)
        {
            sum += solve(pattern[i], dict[j]);
        }

        fprintf(fp, "Case #%d: %d\n", i+1, sum);
    }

}