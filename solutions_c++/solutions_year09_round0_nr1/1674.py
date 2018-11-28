#include <iostream>
#include <string>
using namespace std;
const int MAXD = 5000;
int t[MAXD][2], c, result, d;
string dictionary[MAXD], pattern, word;
bool found(int p)
{
    string temp1, temp2;
    int l = 0, r = d - 1, m;
    if(p == 0)
        return true;
    temp2.assign(word, 0, p);
    while(l <= r)
    {
        m = (l + r) / 2;
        temp1.assign(dictionary[m], 0, p);
        if(temp1 == temp2)
            return true;
        if(temp1 > temp2)
            r = m - 1;
        else
            l = m + 1;
    }
    return false;
}
void generate(int p)
{
    int i;
    if(!found(p))
        return;
    if(p == c)
        result++;
    else
        for(i = t[p][0]; i <= t[p][1]; i++)
        {
            word[p] = pattern[i];
            generate(p + 1);
        }
}
int main()
{
    freopen("inout.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int l, n, i, j;
    cin >> l >> d >> n;
    for(i = 0; i < d; i++)
        cin >> dictionary[i];
    sort(dictionary, dictionary + d);
    for(i = 1; i <= n; i++)
    {
        result = 0;
        c = 0;
        cin >> pattern;
        for(j = 0; j < pattern.size(); j++)
            if(pattern[j] == '(')
            {
                t[c][0] = j + 1;
                while(pattern[j] != ')')
                    j++;
                t[c++][1] = j - 1;
            }
            else
            {
                t[c][0] = j;
                t[c++][1] = j;
            }
        word.clear();
        for(j = 0; j < l; j++)
            word += " ";
        generate(0);
        cout << "Case #" << i << ": " << result << endl;
    }
    return 0;
}
