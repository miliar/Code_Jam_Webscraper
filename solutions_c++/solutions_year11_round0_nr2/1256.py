#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("b.in");
ofstream fout("b.out");
#define cin fin
#define cout fout

int ComNum, DesNum;
string combine[100];
string destroy[100];
char list[200];
string s;
int sl;
int ls = 0;

int findcombine(char a, char b)
{
    for (int i = 1; i <= ComNum; ++i )
        if ((combine[i][0]==a)&&(combine[i][1]==b) || (combine[i][0]==b)&&(combine[i][1]==a))
            return i;
    return 0;
}

bool fdestroy(char a, char b)
{
    for (int i = 1; i <= DesNum; ++i )
        if ((destroy[i][0]==a)&&(destroy[i][1]==b) || (destroy[i][0]==b)&&(destroy[i][1]==a))
            return 1;
    return 0;
}

bool finddestroy()
{
    for (int i = 1; i <= ls-1; ++i )
        if (fdestroy(list[i], list[ls])) return 1;
    return 0;
}

void add(char c)
{
    list[++ls] = c;
    if (ls == 1) return ;
    int tmp = findcombine(list[ls-1], list[ls]);
    if (tmp)
    {
        ls -= 2;
        add(combine[tmp][2]);
        return;
    }
    if (finddestroy())
    {
        ls = 0;
        return ;
    }
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t )
    {
        cin >> ComNum;
        for (int i = 1; i <= ComNum; ++i )
            cin >> combine[i]; 
        cin >> DesNum;
        for (int i = 1; i <= DesNum; ++i )
            cin >> destroy[i];
        cin >> sl;
        cin >> s;
        ls = 0;
        for (int i = 0; i < sl; ++i )
            add(s[i]);
        cout << "Case #" << t << ": [";
        for (int i = 1; i <= ls-1; ++i )
            cout << list[i] << ", ";
        if (ls) cout << list[ls];
        cout << "]" << endl;
    }
    system("pause");
}
