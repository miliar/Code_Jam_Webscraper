#include <iostream>
#include <fstream>
#include <limits>
#include <list>

int findNextNonLabeledCell(bool *markedMap, int size)
{
	for (int i = 0; i < size; ++i)
		if (!markedMap[i])
			return i;
	return -1;
}

enum e_direction
{
	NORTH = 0,
	WEST,
	EAST,
	SOUTH,
	BASIN 
};

int main(int argc, char *argv[])
{
	std::ifstream inputFile(argv[1]);

	int numberOfMaps;
	inputFile >> numberOfMaps;

	for (int indexMap = 0; indexMap < numberOfMaps; ++indexMap)
	{
		int H = 0;
		int W = 0;

		inputFile >> H;
		inputFile >> W;

		int *elevationMap = new int[H * W];
		bool *markedMap = new bool[H * W];
		char *labelMap = new char[H * W];
		char nextLabel = 'a';

		for (int indexRow = 0; indexRow < H; ++indexRow)
			for (int indexCol = 0; indexCol < W; ++indexCol)
			{
				int curValue = 0;
				inputFile >> curValue;
				elevationMap[indexRow * W + indexCol] = curValue;
				markedMap[indexRow * W + indexCol] = false;
				labelMap[indexRow * W + indexCol] = '0';
			}

		while (1)
		{
			int indexCell = findNextNonLabeledCell(markedMap, H * W);

			if (indexCell == -1)
				break;

			std::list<int> path;

			path.clear();

			int curCell = indexCell;
			while (1)
			{
				int curValue = elevationMap[curCell];
				// NORTH

				int valueNeighbors[4];
				valueNeighbors[NORTH] = std::numeric_limits<int>::max();
				valueNeighbors[SOUTH] = std::numeric_limits<int>::max();
				valueNeighbors[WEST]  = std::numeric_limits<int>::max();
				valueNeighbors[EAST]  = std::numeric_limits<int>::max();

				if (curCell >= W)
					valueNeighbors[NORTH] = elevationMap[curCell - W];
				if (curCell < (H - 1) * W)
					valueNeighbors[SOUTH] = elevationMap[curCell + W];
				if (curCell % W != 0)
					valueNeighbors[WEST] = elevationMap[curCell - 1];
				if (curCell % W != W - 1)
					valueNeighbors[EAST] = elevationMap[curCell + 1];

				int curMin = curValue;
				e_direction nextDirection = BASIN;

				for (int i = 0; i < 4; i++)
				{
					if (valueNeighbors[i] < curMin)
					{
						nextDirection = static_cast<e_direction>(i);
						curMin = valueNeighbors[i];
					}
				}

				if (nextDirection == BASIN)
				{
					markedMap[curCell] = true;
					labelMap[curCell] = nextLabel;

					for (std::list<int>::iterator iter = path.begin(); iter != path.end(); iter++)
					{
						markedMap[*iter] = true;
						labelMap[*iter] = nextLabel;
					}
					path.clear();
					nextLabel++;
					break;
				}

				int indexNextNeighbor = 0;
				switch(nextDirection)
				{
				case NORTH: indexNextNeighbor = curCell - W; break;
				case SOUTH: indexNextNeighbor = curCell + W; break;
				case WEST:	indexNextNeighbor = curCell - 1; break;
				case EAST:  indexNextNeighbor = curCell + 1; break;
				default:
				    break;
				}

				if (markedMap[indexNextNeighbor])
				{
					char labelFound = labelMap[indexNextNeighbor];
					markedMap[curCell] = true;
					labelMap[curCell] = labelFound;

					for (std::list<int>::iterator iter = path.begin(); iter != path.end(); iter++)
					{
						markedMap[*iter] = true;
						labelMap[*iter] = labelFound;
					}
					path.clear();
					break;
				}
				else
				{
					path.push_back(curCell);
					curCell = indexNextNeighbor;
				}
			}
		}

		std::cout << "Case #" << indexMap + 1 << ":" << std::endl;

		for (int indexRow = 0; indexRow < H; ++indexRow)
		{
			for (int indexCol = 0; indexCol < W; ++indexCol)
				std::cout << labelMap[indexRow * W + indexCol] << " ";
			std::cout << std::endl;
		}
	}
}