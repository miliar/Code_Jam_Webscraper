#include <iostream>
#include <utility>
#include <vector>
#include <string>
#include <algorithm>
#include <deque>
#include <map>

using namespace std;


map< pair<int, int>, bool > memo;

vector< pair <int, int> > vinesList;
int d;

bool dp (int i, int l)
{
    //cout << "DP input: " << i << " " << l << endl;
    map< pair<int, int> , bool >::iterator it;
    if ((it=memo.find(pair<int, int>(i, l))) != memo.end())
    {
	return memo[pair<int, int>(i, l)];
    }

    int reach = vinesList[i].first + l;
    if (reach >= d)
    {
	//cout << "Checked reach -- true" << endl;
	memo[pair<int, int>(i, l)] = true;
	return true;
    }
    //cout << "Checked reach -- failed" << endl;

    int j = i+1;
    while (vinesList[j].first <= reach)
    {
	if (dp(j, min(vinesList[j].first - vinesList[i].first, vinesList[j].second)))
	{
	    memo[pair<int, int>(i, l)] = true;
	    return true;
	}
	j++;
    }
    //cout << "Finished looping through vines" << endl;

    memo[pair<int, int>(i, l)] = false;
    return false;
}


int main()
{
    int t;
    cin >> t;
    //cout << t << " test cases" << endl;

    for (int i = 0; i < t; i++)
    {
	vinesList.clear();
	memo.clear();

	// Do stuff!
	int n;
	cin >> n;
	//cout << n << " vines" << endl;

	for (int j = 0; j < n; j++)
	{
	    int di, li;
	    cin >> di >> li;
	    vinesList.push_back(pair<int, int>(di, li));
	    //cout << "Vine #" << j+1 << ": " << di << " " << li << endl;
	}
	//cout << "Read in all vines" << endl;

	cin >> d;
	//cout << d << " dist" << endl;

	bool out = dp(0, vinesList[0].first);
	cout << "Case #" << i+1 << ": " << (out?"YES":"NO") << endl;
    }
}
