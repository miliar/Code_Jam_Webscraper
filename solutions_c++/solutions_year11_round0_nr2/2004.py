#include <cstdio>
#include <vector>
using namespace std;

#define DB 0

int charToInt(char x)
{
	if (x == 'Q') return 1;
	if (x == 'W') return 2;
	if (x == 'E') return 3;
	if (x == 'R') return 4;
	if (x == 'A') return 5;
	if (x == 'S') return 6;
	if (x == 'D') return 7;
	if (x == 'F') return 8;
	return 0;
}

char combine[9][9]; // c if i and j combine c, or 0 if i and j don't combine anything
bool oppose[9][9]; // true if i and j are opposed to each other

vector<char> list;

void init()
{
	list.clear();
	for (int i = 0; i < 9; i++)
		for (int j = 0; j < 9; j++)
		{
			combine[i][j] = 0;
			oppose[i][j] = false;
		}
}

bool onList(int x) // true if x is on list
{
	int size = list.size();
	for (int i = 0; i < size; i++)
		if (charToInt(list[i]) == x) return true;
	return false;
}

bool shallIClear(char x) // true if list should be cleared
{
	for (int i = 1; i < 9; i++)
	{
		if (oppose[i][charToInt(x)] && onList(i))
			return true;
		else continue;
	}
	return false;
}

void printList()
{
	printf("[");
	int size = list.size();
	if (size > 0)
		printf("%c", list[0]);
	for (int i = 1; i < size; i++)
		printf(", %c", list[i]);
	printf("]\n");
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++)
	{
		init();
		int C, D, N;
		scanf("%d", &C);
		getchar();
		while (C--)
		{
			char a, b, c;
			scanf("%c%c%c", &a, &b, &c);
			combine[charToInt(a)][charToInt(b)] = c;
			combine[charToInt(b)][charToInt(a)] = c;
			getchar();
		}
		scanf("%d", &D);
		getchar();
		while (D--)
		{
			char a, b;
			scanf("%c%c", &a, &b);
			oppose[charToInt(a)][charToInt(b)] = true;
			oppose[charToInt(b)][charToInt(a)] = true;
			getchar();
		}
		scanf("%d", &N);
		getchar();
		#if DB
		for (int i = 0; i < 9; i++, printf("\n"))
			for (int j = 0; j < 9; j++)
				printf("%d ", oppose[i][j]);
		#endif
		while (N--)
		{
			char x = getchar();
			#if DB
			printf("%c: ", x);
			#endif
			if (list.size() > 0)
			{
				// check if x combine with previous character
				char prev = list[list.size()-1];
				char combined = combine[charToInt(x)][charToInt(prev)];
				if (combined != 0)
				{
					list.pop_back();
					list.push_back(combined);
					#if DB
					printList();
					#endif
					continue;
				}

				// check if x oppose with sth on the list
				if (shallIClear(x))
					list.clear();
				else
					list.push_back(x);
			}
			else
				list.push_back(x);
			#if DB
			printList();
			#endif
		}

		// print result
		printf("Case #%d: ", Ti);
		printList();
	}
	return 0;
}

