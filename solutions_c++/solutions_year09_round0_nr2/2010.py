#include <cstdio>
#include <cstring>
#include <map>

struct Node
{
	Node* parent;
	int rank;
	int altitude;

	Node(int anAltitude = -1): parent(this), rank(0), altitude(anAltitude) {}

	void reset()
	{
		parent = this;
		rank = 0;
		altitude = 0;
	}
};
 
Node* find(Node* x)
{
	if (x->parent == x)
	{
		return x;
	}
	else
	{
		return x->parent = find(x->parent);
	}
}

void unite(Node* x, Node* y)
{
	Node* xRoot = find(x);
	Node* yRoot = find(y);

	if (xRoot->rank > yRoot->rank)
	{
		yRoot->parent = xRoot;
	}
	else if (xRoot->rank < yRoot->rank)
	{
		xRoot->parent = yRoot;
	}
	else if (xRoot != yRoot) // Unless x and y are already in same set, merge them
	{
		yRoot->parent = xRoot;
		xRoot->rank = xRoot->rank + 1;
	}
}

int H, W;
Node map[100][100];
bool visited[100][100];

void flow(int i, int j)
{
	int alt = map[i][j].altitude;
	int di[] = {-1, 0, 0, 1};
	int dj[] = {0, -1, 1, 0};

	int minAlt = alt;
	int minK = -1;
	for (int k = 0; k < 4; ++k)
	{
		if (i+di[k] >= 0 && i+di[k] < H && j+dj[k] >= 0 && j+dj[k] < W)
		{
			int currAlt = map[i+di[k]][j+dj[k]].altitude;

			if (currAlt < minAlt)
			{
				minK = k;
				minAlt = currAlt;
			}
		}
	}

	if (minK > -1)
	{
		unite(&(map[i][j]), &(map[i+di[minK]][j+dj[minK]]));
		flow(i + di[minK], j + dj[minK]);
	}
}

int main()
{
	int T;

	scanf("%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		scanf("%d %d", &H, &W);

		memset(visited, 0, sizeof(visited));

		for (int i = 0; i < H; ++i)
		{
			for (int j = 0; j < W; ++j)
			{
				map[i][j].reset();
				scanf("%d", &(map[i][j].altitude));
			}
		}
		

		for (int i = 0; i < H; ++i)
		{
			for (int j = 0; j < W; ++j)
			{
				flow(i, j);
			}
		}

		std::map<Node*, char> basin;
		char letter = 'a';

		printf("Case #%d:\n", t);

		for (int i = 0; i < H; ++i)
		{
			for (int j = 0; j < W; ++j)
			{
				Node* repr = find(&(map[i][j]));
				if (basin.find(repr) == basin.end())
				{
					basin[repr] = letter;
					printf("%c", letter);
					++letter;
				}
				else
				{
					printf("%c", basin[repr]);
				}
				if (j < W-1)
					printf(" ");
			}
			printf("\n");
		}
	}

	return 0;
}
