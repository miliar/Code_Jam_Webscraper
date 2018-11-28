#include <iostream>
#include <utility>
#include <vector>
#include <string>
#include <algorithm>
#include <deque>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
	// Do stuff!
	int n;
	vector < vector < int > > adj;
	cin >> n;
	for (int j = 0; j < n; j++)
	{
	    vector<int> adjList;
	    int mi;
	    cin >> mi;
	    for (int k = 0; k < mi; k++)
	    {
		int adjNum;
		cin >> adjNum;
		// Zero indexing
	        adjList.push_back(adjNum-1);
	    }
	    adj.push_back(adjList);
	}

	/*
	// Print the adjacency list
	for (int j = 0; j < n; j++)
	{
	    cout << j << ":";
	    for (int k = 0; k < adj[j].size(); k++)
	    {
		cout << " " << adj[j][k];
	    }
	    cout << endl;
	}
	*/

	// Now do BFS, and check for cross edges
	bool done = false;
	bool* seenOverall = new bool[n];
	for (int j = 0; j < n; j++)
	{
	    seenOverall[j] = false;
	}
	for (int j = 0; j < n; j++)
	{
	    if (seenOverall[j]) continue;
	    deque <int> curNodes;
	    bool* seen = new bool[n];
	    for (int k = 0; k < n; k++)
	    {
		seen[k] = false;
	    }
	    seen[j] = true;
	    seenOverall[j] = true;
	    curNodes.push_back(j);
	    while (curNodes.size() > 0)
	    {
		int node = curNodes.front();
		curNodes.pop_front();
		for (int k = 0; k < adj[node].size(); k++)
		{
		    int expNode = adj[node][k];
		    if (seen[expNode])
		    {
			done = true;
			break;
		    }
		    seen[expNode] = true;
		    seenOverall[expNode] = true;
		    curNodes.push_back(expNode);
		}
		if (done)
		{
		    break;
		}
	    }

	    if (done) break;
	}

	cout << "Case #" << i+1 << ": " << (done ? "Yes" : "No") << endl;
    }
}
