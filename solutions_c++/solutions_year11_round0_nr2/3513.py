#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main(void){
	int T;	
	cin >> T;
	for (int i=0; i < T; i++) 
	{
		
		char subsFrom[50][2];
		char subsTo[50];

		char opposed[50][2];
		char input[200];		
		char result[200];

		char baseelements[8]={'Q','W','E','R','A','S','D','F'};		

		//subtitutions
		int n_sub = 0;
		cin >> n_sub;
		for (int j=0; j < n_sub; j++)
		{
			cin >> subsFrom[j][0];
			cin >> subsFrom[j][1];
			cin >> subsTo[j];
		}

		//oposites
		int n_opos = 0;
		cin >> n_opos;
		for (int j=0; j < n_opos; j++)
		{
			cin >> opposed[j][0];
			cin >> opposed[j][1];
		}

		int n_input = 0;
		cin >> n_input;
		for (int j=0; j < n_input; j++)
			cin >> input[j];

		int outputPosition = 0;
		result[0] = input[0];
		bool subPos = true;
		for (int k = 1; k < n_input; k++)
		{
			
			outputPosition++;
			result[outputPosition] = input[k];

			// check for substitution
			for (int a = 0; a < n_sub; a++) {
				if ((result[outputPosition] == subsFrom[a][0] && result[outputPosition-1] == subsFrom[a][1]) ||
					(result[outputPosition] == subsFrom[a][1] && result[outputPosition-1] == subsFrom[a][0])
					)
				{
					outputPosition--;
					result[outputPosition] = subsTo[a];
					break;
				}
			}

			// check for opposite
			if (input[k] == baseelements[0] ||
				input[k] == baseelements[1] ||
				input[k] == baseelements[2] ||
				input[k] == baseelements[3] ||
				input[k] == baseelements[4] ||
				input[k] == baseelements[5] ||
				input[k] == baseelements[6] ||
				input[k] == baseelements[7])
			{
				bool sub = false;
				for (int a = 0; a < n_opos; a++) 
				{
					if (result[outputPosition] == opposed[a][0])
					{
						for (int g=outputPosition; g > 0; g--)
						{
							if (result[g-1] == opposed[a][1]) {
								outputPosition = -1;
								a = n_opos;break;
							}
						}
					}
					if (result[outputPosition] == opposed[a][1])
					{
						for (int g=outputPosition; g > 0; g--)
						{
							if (result[g-1] == opposed[a][0]) {
								outputPosition = -1;
								a = n_opos;break;
							}
						}
					}
				}
			}

		}
		cout << "Case #" << (i+1) <<": [";
		if (outputPosition >= 0) cout << result[0];
		for (int e = 1; e <= outputPosition; e++)
			cout << ", " << result[e] ;
		cout << "]\n";
	}
}