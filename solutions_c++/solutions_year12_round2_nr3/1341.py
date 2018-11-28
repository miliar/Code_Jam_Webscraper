#include <iostream>
#include <vector>
#include <iomanip>
#include <set>
#include <map>

using namespace std;


typedef long long int Long;


bool eval(const vector<Long>& s, const vector<int>& a, const vector<int>& b)
{
    int i = 0, j = 0;
    while (i < a.size() && j < b.size())
    {
        if (a[i] == b[j])
            return false;
        if (a[i] < b[j])
            i++;
        else
            j++;
    }
    for (i = 0; i < a.size(); i++)
    {
        if (i > 0)
            cout << " ";
        cout << s[a[i]];
    }
    cout << endl;
    for (i = 0; i < b.size(); i++)
    {
        if (i > 0)
            cout << " ";
        cout << s[b[i]];
    }
    cout << endl;
    return true;
}


void solve(const vector<Long>& s)
{
    map<Long, vector< vector<int> > > cache;
    map<Long, vector< vector<int> > >::iterator itr;
    map<Long, vector< vector<int> > >::iterator itr2;

    cache.insert(make_pair(0, vector< vector<int> >(1, vector<int>())));

    for (int i = 0; i < s.size(); i++)
    {
        map<Long, vector< vector<int> > > newSpots;

        for (itr = cache.begin(); itr != cache.end(); ++itr)
        {
            Long newVal = itr->first + s[i];
            vector< vector<int> > paths = itr->second;

            for (int j = 0; j < paths.size(); j++)
            {
                vector<int>& path = paths[j];
                path.push_back(i);
            }

            itr2 = cache.find(newVal);
            if (itr2 == cache.end())
            {
                newSpots.insert(make_pair(newVal, paths));
            }
            else
            {
                vector< vector<int> >& otherPaths = itr2->second;
                for (int j = 0; j < paths.size(); j++)
                {
                    for (int k = 0; k < otherPaths.size(); k++)
                    {
                        if (eval(s, paths[j], otherPaths[k]))
                            return;
                    }
                }
                for (int j = 0; j < paths.size(); j++)
                {
                    otherPaths.push_back(paths[j]);
                }
            }
        }

        for (itr = newSpots.begin(); itr != newSpots.end(); itr++)
            cache.insert(*itr);
    }
    cout << "Impossible" << endl;
}


int main()
{
    int T;
    cin >> T;

    for (int caseNum = 1; caseNum <= T; caseNum++)
    {
        int N;
        cin >> N;
        vector<Long> s(N, 0);
        for (int i = 0; i < N; i++)
        {
            cin >> s[i];
        }
        cout << "Case #" << caseNum << ":" << endl;
        solve(s);
    }

    return 0;
}
