#include <iostream>
using namespace std;
class Colour
{
	public:
	Colour* next;
	char c;
	int isColourSet;
	int isColourMin;
};
void setColour(Colour* c)
{
	if(c == NULL)
		cout << "error!!";
	if(c->next == NULL)
		return;
	if(c->next->next == NULL)
	{
		return;
	}
	setColour(c->next);

	c->next = c->next->next;
	c->isColourMin = 0;
	
}
int main()
{
	int numTestCases = 0;
	cin >> numTestCases;
	int H, W;
	int minimum;
	
	for(int testCaseNum = 1; testCaseNum <= numTestCases; testCaseNum++)
	{
		cout << "Case #" << testCaseNum << ":\n";
		char nextChar = 'a';
		cin >> H >> W;
		Colour* Colours[H + 2][W + 2];
		int altitudes[H + 2][W + 2];
		for(int i = 1; i <= H; i++)
		{
			for(int j = 1; j <= W; j++)
			{
				cin >> altitudes[i][j];	
				Colours[i][j] = (Colour *) malloc (sizeof (Colour));
				Colours[i][j]->isColourMin = -1;
				Colours[i][j]->isColourSet = -1;
				Colours[i][j]->next = NULL;
			}
		}
		
		
	//	cout << "I am here\n";
		for(int j = 0; j < H + 2; j++)
		{
			altitudes[j][0] = 15000;
			altitudes[j][W + 1] = 15000;
		}
		for(int j = 0; j < W + 2; j++)
		{
			altitudes[H + 1][j] = 15000;
			altitudes[0][j] = 15000;
		}
	/*	for(int i = 0; i <= H + 1; i++)
		{
			for(int j = 0; j <= W + 1; j++)
			{
				cout << altitudes[i][j] << " " ;
			}
			cout << "\n";
		}
	*/
		for(int i = 1; i <= H; i++)
		{
			for(int j = 1; j <= W; j++)
			{
				minimum = altitudes[i][j];
				if(altitudes[i - 1][j] < minimum)
				{
					minimum = altitudes[i - 1][j];
					Colours[i][j]->next = Colours[i - 1][j];
				}
				if(altitudes[i][j - 1] < minimum)
				{
					minimum = altitudes[i][j - 1];
					Colours[i][j]->next = Colours[i][j - 1];
				}
				if(altitudes[i][j + 1] < minimum)
				{
					minimum = altitudes[i][j + 1];
					Colours[i][j]->next = Colours[i][j + 1];
				}
				if(altitudes[i + 1][j] < minimum)
				{

					minimum = altitudes[i + 1][j];
					Colours[i][j]->next = Colours[i + 1][j];
				}
//				cout << i << " " << j << " " << minimum << "\n";
				/*for(int i = 1; i <= H; i++)
				{
					for(int j = 1; j <= W; j++)
					{
						cout << Colours[i][j]->colour << " ";
					}
					cout << "\n";
				}*/
			}
		}
		
		for(int i = 1; i <= H; i++)
		{
			for(int j = 1; j <= W; j++)
			{
				if(Colours[i][j]->isColourMin == -1)
				{
					setColour(Colours[i][j]);
				}
			}
		}
		
		for(int i = 1; i <= H; i++)
		{
			for(int j = 1; j <= W; j++)
			{
				if(Colours[i][j]->isColourSet == -1)
				{
					Colours[i][j]->isColourSet = 0;
					if(Colours[i][j]->next == NULL)
					{
						Colours[i][j]->c = nextChar;
						nextChar++;
						continue;
					}
					else if(Colours[i][j]->next->isColourSet == -1)
					{
						Colours[i][j]->next->c = nextChar;
						Colours[i][j]->next->isColourSet = 0;
						nextChar++;
					}
					Colours[i][j]->c = Colours[i][j]->next->c;
				}
			}
		}
		
		for(int i = 1; i <= H; i++)
		{
			for(int j = 1; j <= W; j++)
			{
				cout << Colours[i][j]->c << " ";
			}
			cout << "\n";
		}
	}
}

