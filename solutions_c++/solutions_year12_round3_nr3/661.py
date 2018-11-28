#include <iostream>
#include <vector>
#include <map>
#include <list>

using namespace std;

template <typename  Container>
void readArray(Container& C, int numberOfEntries)
{
	for(int i = 0; i < numberOfEntries; i++)
	{
	    typename Container::value_type value;
		cin >> value;
		C.push_back(value);
	}
}

typedef pair<long long, int> ValueType;

vector<ValueType> B, T;

long long cache[101][101];

long long getResult(int pos1, int pos2)
{
	long long r = 0;
	int p1 = pos1, p2 = pos2;
	bool b = false;

	if(pos1 == B.size()) return 0;
	if(pos2 == T.size()) return 0;

	// cached case
	// if( cache[pos1][pos2] != -1) return cache[pos1][pos2];

	// simple case
	if( B[pos1].second == T[pos2].second) 
	{
		r = min( B[pos1].first, T[pos2].first);

		B[pos1].first -= r;
		T[pos2].first -= r;

		b = true;
	}
	
	long long r2 = r + max( getResult(pos1 + 1, pos2), getResult(pos1, pos2 + 1));

	if(b)
	{
		B[p1].first += r;
		T[p2].first += r;
	}

	// cache[p1][p2] = r2;
	// printf("%d %d %d\n", pos1, pos2, r2);

	return r2;
}

void processCase()
{
	int N, M;

	cin >> N;
	cin >> M;

	B.clear();
	T.clear();

	for(int i = 0; i < 101; i++)
		for(int j = 0; j < 101; j++)
			cache[i][j] = -1;

	for(int i = 0; i < N; i++)
	{
		ValueType value;

		cin >> value.first;
		cin >> value.second;

		B.push_back(value);
	}
	

	for(int i = 0; i < M; i++)
	{
		ValueType value;

		cin >> value.first;
		cin >> value.second;

		T.push_back(value);
	}

	long long result = getResult(0, 0);

	cout << result;
}

int main(int argc, const char * argv[])
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
			processCase();
		printf("\n");
	}
	
    return 0;
}
