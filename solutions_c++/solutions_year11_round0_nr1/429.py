///Bot Trust
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <algorithm>
#include <stdio.h>
#include <ctype.h>

#define MAX 111
#define FILE_IN "A-large.in"
#define FILE_OUT "output.txt"

using namespace std;

int seq[MAX];
int next0[MAX];
int next1[MAX];
int ord[MAX];
int t, n;

int input(istream &cin)
{
    cin >> n;
    char c;
    for (int i=0; i<n; i++)
    {
        cin >> c >> seq[i];
        //cout << c << seq[i] << endl;
        if (c=='O')
        {
            ord[i] = 1;
        }
        else
        {
            ord[i] = 0;
        }
    }

    if (ord[n-1] == 0)
    {
        next0[n-1] = n-1;
        next1[n-1] = -1;
    }
    else {
        next0[n-1] = -1;
        next1[n-1] = n-1;
    }

    for (int i=n-2; i>=0; i--)
    {
        if (ord[i] == 0)
        {
            next0[i] = i;
            next1[i] = next1[i+1];
        }
        else
        {
            next0[i] = next0[i+1];
            next1[i] = i;
        }
    }

    //for (int i=0; i<n; i++) cout << next0[i] << " "; cout << endl;
    //for (int i=0; i<n; i++) cout << next1[i] << " "; cout << endl;
}

int next(int cur, int curS, int next[])
{
    int curN = next[curS];
    if (curN == -1) return cur;
    if (cur > seq[curN]) return cur-1;
    if (cur < seq[curN]) return cur+1;
    return cur;
}

int solve()
{
    int cur0 = 1, cur1 = 1;
    int curS = 0;
    int ans = 0;
    while (curS < n)
    {
  //      cout << ans << " " << cur0 << " " << cur1  << " " << curS << endl;
    //    system("pause");
        ans++;
        if (ord[curS] == 0)
        {
            cur1 = next(cur1, curS, next1);
            if( cur0 == seq[curS])
            {
                curS++;
            }
            else cur0 = next(cur0, curS, next0);
        }
        else
        {
            cur0 = next(cur0, curS, next0);
            if (cur1 == seq[curS])
            {
                curS++;
            }
            else cur1 = next(cur1, curS, next1);
        }
    }
    return ans;
}

int main()
{
    ifstream cin(FILE_IN);
    cin >> t;
    ofstream fout(FILE_OUT);
    for (int i = 1; i<=t; i++)
    {
    //    init();
        input(cin);
        fout << "Case #" << i << ": " << solve() << endl;
    }
    fout.close();
}
