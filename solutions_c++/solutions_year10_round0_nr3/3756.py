#include <iostream>
#include <cstring>
#include <sstream>
#include <cctype>
using namespace std;

int stringToInt(string convert)
{
	int i;
	istringstream buf(convert);
	buf >> i;
	return i;
}


void parseInts(string ints, int *array)
{
	string temp;
	int count = 0;
	for(int i = 0; i < ints.length(); i++)
	{
		if(isdigit(ints[i]))
			temp += ints[i];
		else
		{
			array[count] = stringToInt(temp);
			count++;
			temp.erase(temp.begin(), temp.end());
		}
	}
	
	array[count] = stringToInt(temp);
	count++;
}

void swapQueue(int * queue, int N)
{
	int temp = queue[0];
	for(int i = 0; i < N; i++)
		queue[i] = queue[i+1];
	
	queue[N-1] = temp;
}

int main()
{
	string temp;
	getline(cin, temp);
	int T;
	parseInts(temp, &T);
	
	int outputs[T];
	
	for(int i = 0; i < T; i++)
	{
		int euros = 0;
		
		int vars[3];
		getline(cin, temp);
		parseInts(temp, vars);
		int R = vars[0], k = vars[1], N = vars[2];
		
		int queue[N];
		getline(cin, temp);
		parseInts(temp, queue);
		
		
		for(int a = 0; a < R; a++)
		{
			int tempK = k;
			int count = N;
			
			while(tempK >= queue[0])
			{
				euros += queue[0];
				tempK -= queue[0];
				--count;
				
				if(count > 0)
					swapQueue(queue, N);
				else
					tempK = queue[0] - 1;
			}
		}
		
		outputs[i] = euros;
	}
	
	for(int b = 0; b < T; b++)
		printf("Case #%d: %d\n", b+1, outputs[b]);
}