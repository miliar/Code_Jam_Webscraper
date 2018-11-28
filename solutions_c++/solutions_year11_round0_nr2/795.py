#include <iostream>
#include <vector>
#include <fstream>
#include <map>
#include <string>

using namespace std;

bool check_oppose(vector<char> const& v, char to_find)
{
    for (int i = 0; i < v.size(); ++i)
    {
        if (v[i] == to_find)
            return true;
    }
    return false;
}

int main()
{
    ifstream fin("task2.in");
    ofstream fout("task2.out");
    int total;
    fin >> total;

    for (int brojac = 0; brojac < total; ++brojac)
    {
        int C;
        fin >> C;
        map<string, char> combine;
        for (int i = 0; i < C; ++i)
        {
            string s;
            fin >> s;
            string tmp;
            tmp.push_back(s[0]);
            tmp.push_back(s[1]);
            combine[tmp] = s[2];
            tmp = "";
            tmp.push_back(s[1]);
            tmp.push_back(s[0]);
            combine[tmp] = s[2];
        }
        map<char, vector<char> > oppose;
        int D;
        fin >> D;
        for (int i = 0; i < D; ++i)
        {
            string s;
            fin >> s;
            oppose[s[0]].push_back(s[1]);
            oppose[s[1]].push_back(s[0]);
        }
        string invoke;
        int _;
        fin >> _;
        fin >> invoke;
        vector<char> sol;
        int sz = invoke.size();
        for (int i = 0; i < sz; ++i)
        {
            char current = invoke[i];
            sol.push_back(current);
            if (sol.size() >= 2)
            {
                // Check combine
                string combination;
                combination.push_back(sol[sol.size() - 1]);
                combination.push_back(sol[sol.size() - 2]);
                if (combine.find(combination) != combine.end())
                {
                    sol.pop_back();
                    sol.pop_back();
                    sol.push_back(combine[combination]);
                }
                // Check contains
                current = sol[sol.size() - 1];
                if (oppose.find(current) == oppose.end()) continue;
                for (int j = 0; j < oppose[current].size(); ++j)
                {
                    if (check_oppose(sol, oppose[current][j]))
                    {
                        sol.clear();
                        break;
                    }
                }
            }
        }
        fout << "Case #" << brojac + 1 << ": [";
        if (sol.size() != 0)
            fout << sol[0];
        for (int i = 1; i < sol.size(); ++i)
        {
            fout << ", " << sol[i];
        }
        fout << "]" << endl;
    }

    return 0;
}
