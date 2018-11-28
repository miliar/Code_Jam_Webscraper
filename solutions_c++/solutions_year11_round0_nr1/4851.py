#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <queue>

using namespace std;

#define OTHER(X) (1 - X)

int T;

void do_case()
{
    int N;
    cin >> N;
//    printf("N:%d\n", N);
    
    vector<int> v[2];
    queue<pair<int, int> > qNext;
    
    for (int i = 0; i < N; ++i)
    {
	char ch;
	int b;
	cin >> ch;
	cin >> b;
	if (ch == 'O')
	{
	    v[0].push_back(b); 
	    qNext.push(make_pair<int, int>(0, b));
	}
	else
	{
	    v[1].push_back(b); 
	    qNext.push(make_pair<int, int>(1, b));
	}
	
//	printf("c: %c d: %d\n", ch, b);
    }
    
    int num[2];
    num[0] = 0; num[1] = 0;
    int pos[2];
    pos[0] = 1; pos[1] = 1;
    int time = 0;
    while (!qNext.empty())
    {
	pair<int, int> next = qNext.front(); qNext.pop();
//	printf("ki: %d hova: %d\n", next.first, next.second);
//	printf("%d %d %d\n", time, pos[0], pos[1]);
	if (pos[next.first] != next.second)
	{
	    int dist = next.second - pos[next.first];
	    int dt = abs(dist) + 1;
	    num[next.first]++;
	    pos[next.first] = next.second;

	    if (num[OTHER(next.first)] != v[OTHER(next.first)].size())
	    {
		int tmp = v[OTHER(next.first)][num[OTHER(next.first)]] - pos[OTHER(next.first)] ;
		if (  tmp > 0 )
			pos[OTHER(next.first)]+= min(dt, abs(tmp));
		else if (tmp < 0)
		    pos[OTHER(next.first)]-= min(dt, abs(tmp));
	    }
	    time += dt;
	}
	else
	{	
	    time++;
	    num[next.first]++;
	    if (num[OTHER(next.first)] != v[OTHER(next.first)].size())
	    {
		int tmp = v[OTHER(next.first)][num[OTHER(next.first)]] - pos[OTHER(next.first)];
		if (  tmp > 0 )
		    pos[OTHER(next.first)]++;
		else if (tmp < 0)
		    pos[OTHER(next.first)]--;
	    }
	}
//	printf("%d %d %d\n", time, pos[0], pos[1]);
    }
    
    printf("%d\n", time);
}

int main()
{
    cin >> T;
    for(int i = 0; i < T; ++i)
    {
	printf("Case #%d: ", (i+1));
	do_case();
    }

    return 0;
}