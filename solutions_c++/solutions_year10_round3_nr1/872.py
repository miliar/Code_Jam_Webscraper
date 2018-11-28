#include<iostream>
using namespace std;

int main()
{
	int cases;
	cin >> cases;
	
	int **wires = (int **)malloc(1001 * sizeof(int *));
	for(int i = 0; i < 1001; i++)
		wires[i] = (int *)malloc(2 * sizeof(int));
	
	for(int t = 1; t <= cases; t++)
	{
		int numWires = 0;
		cin >> numWires;
		for(int i = 0; i < numWires; i++)
			cin >> wires[i][0] >> wires[i][1];
			
		int intersections = 0;
		for(int i = 0; i < numWires; i++)
		{
			for(int j = i + 1; j < numWires; j++)
			{
				if(((wires[i][0] - wires[j][0]) * (wires[i][1] - wires[j][1])) < 0)
					intersections++;
			}
		}
		cout << "Case #" << t << ": " << intersections << endl;
	}
	
	return 0;
}