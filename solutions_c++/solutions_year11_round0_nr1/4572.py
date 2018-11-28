#include <string>
#include <cstdio>
#include <vector>

struct Point
{
	char bot;
	int button;
};

int main(int argc, char *argv[])
{
	int numCases;

	scanf("%i", &numCases);
	for (int i=0 ; i<numCases ; ++i)
	{
		int numPoints;
		scanf("%i", &numPoints);

		std::vector<Point> points;
		points.resize(numPoints);
		for (int j=0 ; j<numPoints ; ++j)
			scanf(" %c %i", &points[j].bot, &points[j].button);

		std::vector<Point> bluePoints;
		std::vector<Point> orangePoints;

		for (int j=0 ; j<numPoints ; ++j)
		{
			if (points[j].bot == 'O')
				orangePoints.push_back(points[j]);
			else
				bluePoints.push_back(points[j]);
		}

		int currentAction = 0;
		int currentBlueAction = 0;
		int currentOrangeAction = 0;

		int bluePosition = 1;
		int orangePosition = 1;

		char currentBot = points[0].bot;
		
		int numActions = 0;

		while (currentAction < points.size())
		{
			bool nextAction = false;

			//blue bot
			if (currentBlueAction < bluePoints.size())
			{
				if (bluePoints[currentBlueAction].button == bluePosition)
				{
					if (currentBot == 'B')
					{
						++currentBlueAction;
						nextAction = true;
					}
				}
				else if (bluePoints[currentBlueAction].button < bluePosition)
				{
					--bluePosition;
				}
				else
					++bluePosition;
			}

			//orange bot
			if (currentOrangeAction < orangePoints.size())
			{
				if (orangePoints[currentOrangeAction].button == orangePosition)
				{
					if (currentBot == 'O')
					{
						++currentOrangeAction;
						nextAction = true;
					}
				}
				else if (orangePoints[currentOrangeAction].button < orangePosition)
				{
					--orangePosition;
				}
				else
				{
					++orangePosition;
				}
			}

			if (nextAction)
			{
				++currentAction;
				currentBot = points[currentAction].bot;
			}

			++numActions;
		}

		printf("Case #%i: %i\n", i+1, numActions);
	}

	return 0;
}

