#include <iostream>
#include <fstream>
#include <climits>
#include <cstring>
using namespace std;

#define N 20
#define M 1000000

struct node
{
    int con[32];
    int val;
    int len;
};

ifstream fin;
ofstream fout;
node candy[N];
int n;
int minp;

void split(int tmp, int k)
{
    int t = 1;
    candy[k].len = 0;
    candy[k].val = tmp;
    while(tmp > 0)
    {
        if(tmp & 1)
        {
            candy[k].con[candy[k].len] = t;
            ++candy[k].len;
        }
        t = t << 1;
        tmp = tmp >> 1;
    }
}

int divide(int sump, node sums, int k)
{
    int i, j;
    if(sump == 0)
        return 0;
    if(sump == sums.val)
    {
        if(sump < minp)
            minp = sump;
    }
    if(k == n)
        return 0;
    divide(sump, sums, k + 1);
    sump -= candy[k].val;
    for(i = 0; i < candy[k].len; ++i)
    {
        for(j = 0; j < sums.len; ++j)
        {
            if(candy[k].con[i] == sums.con[j])
                break;
        }
        if(j == sums.len)
        {
            sums.val += candy[k].con[i];
            sums.con[j] = candy[k].con[i];
            ++sums.len;
        }
        else
        {
            sums.val -= candy[k].con[i];
            --sums.len;
            sums.con[j] = sums.con[sums.len];
        }
    }
    divide(sump, sums, k + 1);
    return 0;
}

int main()
{
    fin.open("C-small-attempt0.in", ios::in);
    if(!fin.is_open())
    {
        cout << "Can not open file\n";
        return 1;
    }
    fout.open("C-small-attempt0.out", ios::out | ios::trunc);
    if(!fout.is_open())
    {
        cout << "Can not open file\n";
        return 1;
    }

    int t, tmp;
    int i, k;
    int sum;
    node sums;
    fin >> t;
    for(k = 1; k <= t; ++k)
    {
        fin >> n;
        sum = 0;
        minp = INT_MAX;
        for(i = 0; i < n; ++i)
        {
            fin >> tmp;
            sum += tmp;
            split(tmp, i);
        }
        sums.len = 0;
        sums.val = 0;
        divide(sum, sums, 0);
        fout << "Case #" << k << ": ";
        if(minp == INT_MAX)
            fout << "NO" << endl;
        else
            fout << sum - minp << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
