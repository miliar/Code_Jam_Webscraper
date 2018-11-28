#include <iostream>
#include <string>
#include <fstream>

using namespace std;

string words[5000];
string tests[500];
bool exist [5000];
int l, d, n;

ofstream outs ("output.txt");
//#define cout outs

ifstream ins ("input.txt");
#define cin ins

void updateList (string a, int x)
{
    bool flag;
    for (int i = 0; i < d; i++)
        if (exist[i])
        {
            flag = false;
            for (int j = 0; j < a.length(); j++)
                if (a[j] == words[i][x])
                {
                    flag = true;
                    break;
                }
            if (!flag)
                exist[i] = false;
        }
}

int findTotal (string a)
{
    int total = 0;
    for (int i = 0; i < d; i++)
        exist[i] = true;
    int x = 0;
    for (int i = 0; i < a.length(); i++)
    {
        if (a[i] == '(')
        {
            i++;
            string temp = "";
            while ( a[i] != ')')
            {
                temp+=a[i];
                i++;
            }
            updateList(temp, x);
        }
        else
        {
            string temp = "";
            temp+=a[i];
            updateList(temp, x);
        }
        x++;
    }
    for (int i = 0; i < d; i++)
        if (exist[i])
            total++;

    return total;
}

int main()
{
    int j = 1;
    cin >> l >> d >> n;
    getline(cin, words[0]);
    for (int i = 0; i < d; i++)
        getline(cin, words[i]);
    for (int i = 0; i < n; i++)
    {
        getline(cin, tests[i]);
        outs << "Case #" << j << ": " << findTotal(tests[i]) << endl;
        j++;
    }

    return 0;
}
