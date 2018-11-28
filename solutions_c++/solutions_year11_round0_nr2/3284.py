#include <iostream>
#include <fstream>
using namespace std;

#define N 105
#define C 40
#define D 40

ifstream fin;
ofstream fout;
char list[N];
char com[C][5];
char opp[D][5];
int c, d, n;
int posl;

int add(char ele)
{
    int i, j;
    char oppw;
    if(posl == -1)
    {
        ++posl;
        list[posl] = ele;
        return 0;
    }
    for(i = 0; i < c; ++i)
    {
        if((com[i][0] == ele && com[i][1] == list[posl]) || (com[i][1] == ele && com[i][0] == list[posl]))
        {
            --posl;
            add(com[i][2]);
            return 0;
        }
    }
    for(i = 0; i < d; ++i)
    {
        if(ele != opp[i][0] && ele != opp[i][1])
            continue;
        if(ele == opp[i][0])
            oppw = opp[i][1];
        else
            oppw = opp[i][0];
        for(j = 0; j <= posl; ++j)
            if(oppw == list[j])
            {
                posl = -1;
                return 0;
            }
    }
    ++posl;
    list[posl] = ele;
    return 0;
}

int main()
{
    fin.open("B-large.in", ios::in);
    if(!fin.is_open())
    {
        cout << "Can not open file\n";
        return 1;
    }
    fout.open("B-large.out", ios::out | ios::trunc);
    if(!fout.is_open())
    {
        cout << "Can not open file\n";
        return 1;
    }

    int t;
    int i, k;
    char str[N];
    fin >> t;
    for(k = 1; k <= t; ++k)
    {
        fin >> c;
        for(i = 0; i < c; ++i)
            fin >> com[i];
        fin >> d;
        for(i = 0; i < d; ++i)
            fin >> opp[i];
        fin >> n;
        posl = -1;
        fin >> str;
        for(i = 0; i < n; ++i)
        {
            add(str[i]);
        }
        fout << "Case #" << k << ": [";
        for(i = 0; i < posl; ++i)
        {
            fout << list[i] << ", ";
        }
        if(posl != -1)
            fout << list[posl];
        fout << "]" << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
