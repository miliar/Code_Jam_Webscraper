#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<fstream>
#include<queue>
using namespace std;
int G[1100];
queue<int> q;
queue<int> q1;
int main()
{
    ifstream fin("C-small-attempt0.IN");
    ofstream fout("output.txt");
    int T;
    fin>>T;
    for(int i = 1; i <= T;i++)
    {
        int R,k,N;
        memset(G,0,sizeof(G));
        fin>>R>>k>>N;
        while(!q.empty())
            q.pop();
        while(!q1.empty())
            q1.pop();
        for(int j = 1; j <= N;j++)
        {
            fin>>G[j];
            q.push(G[j]);
        }
        long long sum = 0;
        int tmp = 0;
        for(int j = 1; j <= R;j++)
        {
            while(!q.empty() && tmp + q.front() <= k)
            {
                tmp+=q.front();
                q1.push(q.front());
                q.pop();
            }
            sum+=tmp;
            tmp = 0;
            while(!q1.empty())
            {
                q.push(q1.front());
                q1.pop();
            }
        }
        fout<<"Case #"<<i<<": "<<sum<<endl;
    }    
    system("pause");
    return 0;
}
