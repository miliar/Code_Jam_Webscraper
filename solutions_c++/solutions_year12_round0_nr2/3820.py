#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <queue>

using namespace std;

class Node
{
public:
	int a[3];
	bool surp;
	Node(int a1 = 0, int a2 = 0, int a3 = 0)
	{
		a[0] = a1;
		a[1] = a2;
		a[2] = a3;
		if( abs(a1 - a2) == 2 || abs(a1-a3) == 2 || abs(a2-a3) == 2 )
			surp = true;
		else
			surp = false;
	}
	int getMax() const
	{
		return a[2];
	}
};

vector<Node> make(int i)
{
	vector<Node> node_vector;
	int temp;
	if ((i % 3) == 0)
	{
		temp = i/3;
		node_vector.push_back( Node(temp, temp, temp) );

		temp = i-3;
		if(temp >= 0)
		{
			temp = temp/3;
			if(temp+2 <= 10)
				node_vector.push_back( Node(temp, temp+1, temp+2) );
		}
	}
	else if ((i%3) == 1)
	{
		temp = i-1;
		temp = i/3;
		if(temp+1 <= 10)
			node_vector.push_back( Node(temp, temp, temp+1) );

		temp = i-4;
		if(temp >= 0)
		{
			temp = temp/3;
			if(temp+2 <= 10)
				node_vector.push_back( Node(temp, temp+2, temp+2) );
		}
	}
	else if ((i%3) == 2)
	{
		temp = i-2;
		temp = i/3;
		if(temp+2 <= 10)
			node_vector.push_back( Node(temp, temp, temp+2) );
		if(temp+1 <= 10)
			node_vector.push_back( Node(temp, temp+1, temp+1) );
	}
	return node_vector;
}

map< int, vector<Node> > node_map;
vector<int> googler;

int DP[101][101][11];

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	for(int i=0; i<=30; ++i)
	{
		node_map[i] = make(i);
	}

	int testCase = 0;
	int N, S, P, temp;

	cin >> testCase;
	for(int t=1; t<=testCase; ++t)
	{
		cin >> N >> S >> P;
		for(int n=0; n<N; ++n)
		{
			cin >> temp;
			googler.push_back(temp);
		}
		memset(&DP[0][0][0], 0, sizeof(DP));

		// P이상 만족 최대 갯수, Surp남은 수
		queue< pair<int,int> > dfs;
		


		dfs.push( make_pair(0,S) );
		for(int i=0; i<googler.size(); ++i)
		{
			queue< pair<int,int> > chain;
			vector<Node>& _rhp = node_map[googler[i]];
			while(!dfs.empty())
			{
				pair<int,int> m_pair = dfs.front();
				dfs.pop();

				if(_rhp.size() == 1)
				{
					chain.push( make_pair(_rhp[0].getMax() >= P?m_pair.first + 1:m_pair.first,
						_rhp[0].surp?m_pair.second - 1:m_pair.second) );
				}
				else
				{
					// 2개일 때
					chain.push( make_pair(_rhp[0].getMax() >= P?m_pair.first + 1:m_pair.first,
						_rhp[0].surp?m_pair.second - 1:m_pair.second) );
					chain.push( make_pair(_rhp[1].getMax() >= P?m_pair.first + 1:m_pair.first,
						_rhp[1].surp?m_pair.second - 1:m_pair.second) );
				}
			}
			dfs = chain;
		}
		
		int maxP = 0;
		while(!dfs.empty())
		{
			pair<int,int> ii = dfs.front();
			dfs.pop();
			if( ii.second == 0 )
				maxP = max(maxP, ii.first);
		}

		printf("Case #%d: %d\n", t, maxP);
		googler.clear();
	}


	return 0;
}