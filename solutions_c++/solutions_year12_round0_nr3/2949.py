#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include <math.h>

using namespace std;

int main(int argc, char* argv)
{
	int cases;
	cin >> cases;

	int R = 0, MIN = 0, MAX = 0, dig = 0, temp = 0, made = 0, temp1 = 0;
	
	for(int i = 0; i < cases; i++)
	{
		cin >> MIN;
		cin >> MAX;
		R = 0;
		for(int k = MIN; k <= MAX; k++)
		{
			// count digits
			temp = k;
			dig = 0;
			while(temp > 0)
			{
				temp = temp / 10;
				dig = dig + 1;
			}
			
			// shift digits
			made = k;
			for(int j = 0; j < dig - 1; j++)
			{
				temp = made % 10;
				temp1 = made / 10;
				made = (temp * pow(10, (dig - 1))) + temp1;
				
				// check
				if(made > k && made <= MAX)
				{
					R = R + 1;
				}
			}
		}
		cout << "Case #" << (i+1) << ": " << R << endl;
	}
	
	return 0;
}
