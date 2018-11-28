#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int T, N;
long long R, C;
vector<long long> g, cap;
vector<int> next;

int main()
{
    ifstream input("C-large.in");
    ofstream output("C-large.out");
    input >> T;
    for (int casenum = 1; casenum <= T; casenum++)
    {
        input >> R >> C >> N;
        g.resize(N);
        for (int i = 0; i < N; i++) input >> g[i];
        cap.resize(N);
        next.resize(N);
        for (int i = 0; i < N; i++)
        {
            cap[i] = 0;
            int j = i;
            while (cap[i] + g[j] <= C)
            {
                cap[i] += g[j];
                j = (j + 1) % N;
                if (j == i) break;
            }
            next[i] = j;
        }
        vector<int> visited(N);
        vector<int> list;
        vector<long long> sum;
        sum.push_back(0);
        for (int i = 0; i < N; i++) visited[i] = -1;
        int k = 0;
        while (visited[k] < 0)
        {
            visited[k] = list.size();
            list.push_back(k);
            sum.push_back(sum[sum.size()-1]+cap[k]);
            k = next[k];
        }
        int cyclelen = list.size() - visited[k];
        long long cyclesum = sum[sum.size()-1] - sum[visited[k]];
        output << "Case #" << casenum << ": ";
        if (R <= list.size())
            output << sum[R] << endl;
        else
        {
            R -= visited[k];
            long long cycle = R / cyclelen;
            int rem = R % cyclelen;
            output << cycle * cyclesum + sum[visited[k]+rem] << endl;
        }
    }
    input.close();
    output.close();
    return 0;
}
