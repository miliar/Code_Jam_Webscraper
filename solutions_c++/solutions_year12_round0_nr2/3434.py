#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solve();

int main()
{
    int T;
    cin >> T;

    for(int i=0; i<T; ++i)
	{
	    cout << "Case #" << i+1 << ": " << solve() << endl;
	}

    return 0;
}


int solve()
{
    int N,S,p;
    cin >> N >> S >> p;

    vector<int> scores(N);
    for(int i=0; i<N; ++i)
	{
	    cin >> scores[i];
	}

    int needed = 0;
    int free = 0;

    for(int i=0; i<N; ++i)
	{
	    if(scores[i] >= p)
		{
		    int number = p - (scores[i]-p)/2;
		    if(number == 2)
			needed++;
		    else if(number < 2)
			free++;
		}
	}

    if(needed > S)
	return free + S;
    
    return free + needed;

}
