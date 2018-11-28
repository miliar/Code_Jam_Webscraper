#include <cstdio>
#include <vector>

using namespace std;

class Point {
	public:
		int x;
		int y;
};

class Element {
	public:
		int alt;
		bool isSink;
		bool basinSet;
		Point basin;
		char label;
		
		Element(void);
};

Element::Element(void)
{
	basinSet = false;
	isSink = false;
}

class Label {
	public:
		Point basin;
		char name;
};

char findLabel(vector<Label> *labels, int x, int y)
{
	for(int i=0;i<(int)labels->size();i++)
		if (labels->at(i).basin.x == x && labels->at(i).basin.y == y)
			return labels->at(i).name;
	
	return 0;
}

int get(Element map[100][100], int x, int y, int h, int w)
{
	if (x < 0 || y < 0 || x >= h || y >= w)
		return 10002;
	return map[x][y].alt;
}

bool isSink(Element map[100][100], int x, int y, int h, int w)
{
	int curr = map[x][y].alt;
	if (get(map, x-1, y, h, w) >= curr && get(map, x+1, y, h, w) >= curr && get(map, x, y-1, h, w) >= curr && get(map, x, y+1, h, w) >= curr)
		return true;
	return false;
}

Point findSink(Element map[100][100], int x, int y, int h, int w)
{
	if (map[x][y].basinSet)
		return map[x][y].basin;
	
	Point sink;
	
	if (map[x][y].isSink)
	{
		sink.x = x;
		sink.y = y;
		return sink;
	}
	
	int min = get(map, x-1, y, h, w);
	
	if (get(map, x+1, y, h, w) < min)
		min = get(map, x+1, y, h, w);
	
	if (get(map, x, y-1, h, w) < min)
		min = get(map, x, y-1, h, w);
	
	if (get(map, x, y+1, h, w) < min)
		min = get(map, x, y+1, h, w);
	
	if (get(map, x-1, y, h, w) == min)
		sink = findSink(map, x-1, y, h, w);
	else if (get(map, x, y-1, h, w) == min)
		sink = findSink(map, x, y-1, h, w);
	else if (get(map, x, y+1, h, w) == min)
		sink = findSink(map, x, y+1, h, w);
	else if (get(map, x+1, y, h, w) == min)
		sink = findSink(map, x+1, y, h, w);
	
	map[x][y].basin = sink;
	map[x][y].basinSet = true;
	
	return sink;
}

int main(void)
{
	int t;
	scanf("%d", &t);
	
	for(int k=0;k<t;k++)
	{
		int h, w;
		scanf("%d %d", &h, &w);
		
		Element map[100][100];
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				scanf("%d", &map[i][j].alt);
		
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				map[i][j].isSink = isSink(map, i, j, h, w);
		
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				if (!map[i][j].basinSet)
					map[i][j].basin = findSink(map, i, j, h, w);
		
		vector<Label> labels;
		char act = 'a';
		
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
			{
				char label = findLabel(&labels, map[i][j].basin.x, map[i][j].basin.y);
				if (label != 0)
					map[i][j].label = label;
				else
				{
					Label l;
					l.name = act;
					map[i][j].label = act;
					act++;
					l.basin.x = map[i][j].basin.x;
					l.basin.y = map[i][j].basin.y;
					labels.push_back(l);
				}
			}
		
		printf("Case #%d:\n", k+1);
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
				printf("%c ", map[i][j].label);
			printf("\n");
		}
	}
	
	return 0;
}