#include <iostream>
#include <fstream>
#include <queue>
#include <algorithm>
#include <string>

using namespace std;

struct Train
{
    int begin, end;
    int  t;
};

bool CompareBegin(Train a, Train b)
{
    return a.begin<b.begin;
}

inline int TimeToInt(string s)
{
    return ((s[0]-'0')*10 + (s[1]-'0'))*60 + (s[3]-'0')*10 + (s[4]-'0');
}

int main()
{
    ifstream in("input.txt", ios::in);
    ofstream out("output.txt", ios::out);
    string a, b;
    int N, test, T, NA, NB, i;
    Train x[300], curr;
    in >> N;
    for (test=1;test<=N;test++)
    {
        priority_queue<int, vector<int>, greater<int> > Q[2];
        int res[2]={0,0};
        in >> T >> NA >> NB;
        for (i=0;i<NA+NB;i++)
        {
            in >> a >> b;
            x[i].begin=TimeToInt(a);
            x[i].end=TimeToInt(b);
            x[i].t = i < NA ? 0 : 1;
        }
        sort(x, x+NA+NB, CompareBegin);
        
        for (i=0;i<NA+NB;i++)
        {
            curr = x[i];
            
            if (!Q[curr.t].empty())
            {
                if (Q[curr.t].top()+T<=curr.begin) Q[curr.t].pop();
                else res[curr.t]++;
            }
            else res[curr.t]++;
            Q[1-curr.t].push(curr.end);
        }
        out << "Case #" << test << ": " << res[0] << " " << res[1] << endl;
    }
    
    in.close();
    out.close();
    
    return 0;
}
