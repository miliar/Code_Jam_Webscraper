#include <iostream>
#include <string>
#include <vector>
#include <cstring>
using namespace std;

char combine[300][300];
bool delt[300][300];

bool Combine(vector<char>& vec, char c)
{
    if (combine[c][vec[vec.size() - 1]] > 0)
    {
        char t = vec[vec.size() - 1];
        vec.pop_back();
        vec.push_back(combine[c][t]);
        return true;
    }
    return false;
}

bool Delete(vector<char>& vec, char c)
{
    for (int i = 0; i < vec.size(); i++)
        if (delt[vec[i]][c])
        {
            vec.clear();
            return true;
        }
    return false;
}

int main()
{
    int t;
    cin >> t;
    for (int c = 1; c <= t; c++)
    {
        memset(combine, 0, sizeof(combine));
        memset(delt, 0, sizeof(delt));
        int com, del, n;
        cin >> com;
        for (int i = 0; i < com; i++)
        {
            string tmp;
            cin >> tmp;
            combine[tmp[0]][tmp[1]] = tmp[2];
            combine[tmp[1]][tmp[0]] = tmp[2];
        }
        //cout << com << endl;
        cin >> del;
        for (int i = 0; i < del; i++)
        {
            string tmp;
            cin >> tmp;
            delt[tmp[0]][tmp[1]] = true;
            delt[tmp[1]][tmp[0]] = true;
        }
        //cout << del << endl;
        cin >> n;
        string base;
        cin >> base;
        vector<char> v;
        for (int i = 0; i < n; i++)
        {
            if (v.empty())
                v.push_back(base[i]);
            else
            {

                if (!Combine(v, base[i]))
                    if (!Delete(v, base[i]))
                        v.push_back(base[i]);
            }
        }
        cout << "Case #" << c << ": ";
        cout << "[";
        for (int i = 0; i < (int)v.size() - 1; i++)
            cout << v[i] << ", ";
        if (!v.empty())
            cout << v[v.size() - 1];
       cout << "]" << endl;
    }
    return 0;
}

