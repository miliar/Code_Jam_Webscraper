#include <iostream>
#include <utility>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

vector< pair<unsigned long long int, unsigned long long int> > boxes;
vector< pair<unsigned long long int, unsigned long long int> > toys;

map< pair< pair<unsigned long long int, unsigned long long int>, pair<unsigned long long int, unsigned long long int> >, unsigned long long int > memo;

unsigned long long int dp(unsigned long long int boxIndex, unsigned long long int toyIndex, unsigned long long int intoBox, unsigned long long int intoToy)
{
    //cout << "DP of " << boxIndex << " " << toyIndex << " " << unsigned long long intoBox << " " << unsigned long long intoToy << endl;
    if (boxIndex == boxes.size() || toyIndex == toys.size())
    {
	// We hit the base case of nothing left
	return 0;
    }
    //cout << "Types " << boxes[boxIndex].second << " " << toys[toyIndex].second << endl;

    // We have it in the memo
    pair<unsigned long long int, unsigned long long int> indices = pair<unsigned long long int, unsigned long long int>(boxIndex, toyIndex);
    pair<unsigned long long int, unsigned long long int> intos = pair<unsigned long long int, unsigned long long int>(intoBox, intoToy);
    pair< pair<unsigned long long int,unsigned long long int>, pair<unsigned long long int, unsigned long long int> > p = pair< pair<unsigned long long int, unsigned long long int>, pair<unsigned long long int, unsigned long long int> >(indices, intos);
    if (memo.find(p) != memo.end())
    {
	return memo[p];
    }


    unsigned long long int boxesLength = boxes[boxIndex].first - intoBox;
    unsigned long long int toysLength = toys[toyIndex].first - intoToy;

    // Check cases
    // Types match
    if (boxes[boxIndex].second == toys[toyIndex].second)
    {
	// Check lengths
	if (boxesLength == toysLength)
	{
	    memo[p] = (boxesLength + dp(boxIndex+1, toyIndex+1, 0, 0));
	    //cout << "Returning " << memo[p] << " for " << boxIndex << " " << toyIndex << " (eq)" << endl;
	    return memo[p];
	}
	else if (boxesLength > toysLength)
	{
	    memo[p] = (toysLength + dp(boxIndex, toyIndex+1, intoBox+toysLength, 0));
	    //cout << "toysLength" << toysLength << endl;
	    //cout << "Returning " << memo[p] << " for " << boxIndex << " " << toyIndex << " (box)" << endl;
	    return memo[p];
	}
	else
	{
	    memo[p] = (boxesLength + dp(boxIndex+1, toyIndex, 0, intoToy+boxesLength));
	    //cout << "Returning " << memo[p] << " for " << boxIndex << " " << toyIndex << " (toy)" << endl;
	    return memo[p];
	}
    }
    // Types don't match
    else
    {
	//cout << "Getting max" << endl;
	return memo[p] = max(dp(boxIndex+1, toyIndex, 0, intoToy), dp(boxIndex, toyIndex+1, intoBox, 0));
    }
}

int main()
{
    unsigned long long int t;
    cin >> t;
    for (unsigned long long int i = 0; i < t; i++)
    {
	// Do stuff!
	unsigned long long int n, m;
	cin >> n;
	cin >> m;
	boxes.clear();
	toys.clear();
	memo.clear();
	for (unsigned long long int j = 0; j < n; j++)
	{
	    unsigned long long int numBoxes, type;
	    cin >> numBoxes >> type;
	    //cout << "Saw type (boxes) " << type;
	    boxes.push_back(pair<unsigned long long int, unsigned long long int>(numBoxes, type));
	}
	for (unsigned long long int j = 0; j < m; j++)
	{
	    unsigned long long int numToys, type;
	    cin >> numToys >> type;
	    //cout << "Saw type (toys) " << type;
	    toys.push_back(pair<unsigned long long int, unsigned long long int>(numToys, type));
	}

	// Now solve (using DP)!
	cout << "Case #" << i+1 << ": " << dp(0, 0, 0, 0) << endl;
    }
}
