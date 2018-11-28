#include <cstdio>
#include <queue>
#include <string>
#include <utility>
#include <iostream>
using namespace std;

int cmp(int a, int b)
{
	if( a < b ) return -1;
	if( a == b ) return 0;
	return 1;
}

int main()
{
	freopen("input.in", "r", stdin);
	FILE* outp = fopen("output.out", "w");

	int testCase = 0;
	scanf("%d", &testCase);
	for(int tc = 1; tc <= testCase; tc++)
	{
		int N = 0;
		scanf("%d", &N);
		queue < pair < char, int > > whole_queue;
		queue < int > blue_queue;
		queue < int > orange_queue;
		int orange_position = 1;
		int blue_position = 1;

		for(int i = 0; i < N; i++)
		{
			string color;
			int position;
			cin >> color >> position;
			whole_queue.push( make_pair( color[0], position ) );
			if( "B" == color )
			{
				blue_queue.push(position);
			}
			else
			{
				orange_queue.push(position);
			}
		}

		int ans = 0;
		while( !whole_queue.empty() )
		{
			pair < char, int > top = whole_queue.front();
			bool bluemove = false;
			bool orangemove = false;

			if( 'B' == top.first && blue_position == top.second )
			{
				whole_queue.pop();
				blue_queue.pop();
				bluemove = true;
			}
			else if( 'O' == top.first && orange_position == top.second)
			{
				whole_queue.pop();
				orange_queue.pop();
				orangemove = true;
			}

			if(!bluemove && !blue_queue.empty())
			{
				blue_position += cmp(blue_queue.front(), blue_position);
			}
			if(!orangemove && !orange_queue.empty())
			{
				orange_position += cmp(orange_queue.front(), orange_position);
			}

			ans++;
		}

		fprintf(outp, "Case #%d: %d\n", tc, ans);
	}

	fclose(outp);
	return 0;
}