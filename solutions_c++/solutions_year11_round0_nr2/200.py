#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
using namespace std;

bool has_oppose(const vector<char>& v, char c, const set<pair<char, char> >& oppose)
{
    int i;

    for (i = 0; i < (int) v.size(); i++)
    {
        if (oppose.find(make_pair(v[i], c)) != oppose.end())
        {
            return true;
        }
    }

    return false;
}

string format(const vector<char>& v)
#include <vector>
{
    string ans;
    int i;

    if (v.size() == 0)
    {
        return string("[]");
    }

    ans.append("[");
    ans.append(1, v[0]);
    for (i = 1; i < (int) v.size(); i++)
    {
        ans.append(", ");
        ans.append(1, v[i]);
    }
    ans.append("]");

    return ans;
}

int main()
{
    set<pair<char, char> > oppose;
    map<pair<char, char>, char> combine;
    vector<char> ans;
    int T, t;
    int C, D;
    int i;
    string temp;
    int N;
    char c;

    cin >> T;
    for (t = 1; t <= T; t++)
    {
        oppose.clear();
        combine.clear();
        ans.clear();
        cin >> C;
        for (i = 0; i < C; i++)
        {
            cin >> temp;
            combine[make_pair(temp[0], temp[1])] = temp[2];
            combine[make_pair(temp[1], temp[0])] = temp[2];
        }
        cin >> D;
        for (i = 0; i < D; i++)
        {
            cin >> temp;
            oppose.insert(make_pair(temp[0], temp[1]));
            oppose.insert(make_pair(temp[1], temp[0]));
        }
        cin >> N;
        for (i = 0; i < N; i++)
        {
            cin >> c;
            // check for combination
            if (ans.size() != 0 && combine.find(make_pair(ans[ans.size()-1], c)) != combine.end())
            {
                ans[ans.size()-1] = combine[make_pair(ans[ans.size()-1], c)];
            }
            // check for oppose
            else if (ans.size() != 0 && has_oppose(ans, c, oppose))
            {
                ans.clear();
            }
            // nothing, just append to list
            else
            {
                ans.push_back(c);
            }
        }

        cout << "Case #" << t << ": " << format(ans) << endl;
    }

    return 0;
}

