#include <fstream>
#include <iostream>
#include <math.h>
/*

Input

4
1 0
1 1
4 0
4 47

Output
 
Case #1: OFF
Case #2: ON
Case #3: OFF
Case #4: ON

*/

int snappers;

inline int power(int base, int exponent)
{
	return (int)pow((float)base,(float)exponent);
}

bool isFlagAt(int index, int status)
{
	int mask = power(2, index);
	return (status & mask) == mask;
}

void setFlagAt(int index, int value)
{
	int mask = power(2, index);
	if(value == 0)
	{
		if(isFlagAt(index, snappers))
		{
			snappers &= snappers-mask;
		}
	}
	else
	{
		snappers |= mask;
	}
}

void switchState(int index)
{
	if(isFlagAt(index, snappers))
	{
		setFlagAt(index, 0);
	}
	else
	{
		setFlagAt(index, 1);
	}
}

void printBinary(int status)
{
	for(int i=0;i<32;i++)
	{
		if(i%8==0)
			printf(" ");

		if(isFlagAt(i, status))
			printf("1");
		else
			printf("0");
	}
	printf("\n");
}

int main(int argc, char* argv[])
{
	std::fstream input("data.txt", std::ios::in);

	int cases = 0; input >> cases;

	//printf("->%d case(s).\n", cases);
	std::fstream output("output.txt", std::ios::out);

	for(int i=0; i<cases; i++)
	{
		snappers = 0;
		int N, K = 0;
		input >> N; // number of Snappers
		input >> K;	// times snapped fingers

		//printf("-->N: %d.\n", N);
		//printf("-->K: %d.\n", K);

		for(int a=0; a<K; a++)
		{
			int lastSet = -1;
			if(isFlagAt(N, snappers))
				snappers = 0;

			for(int s=0; s<N; s++)
			{
				if(isFlagAt(s, snappers))
				{
					lastSet = s;
				}
				else
				{
					break;
				}
			}

			//printf("-->lastSet: %d.\n", lastSet);

			int idx = 0;
			
			if(lastSet >= 0)
			{
				for(int s=0; s<=lastSet+1; s++)
				{
					switchState(s);
				}
			}
			else
			{
				switchState(0);
			}
		}

		int allOnMask = 0;

		for(int s=0; s<N; s++)
			allOnMask |= power(2,s);

		//printf("AllOnMask = "); printBinary(allOnMask);
		//printf("Snappers = "); printBinary(snappers);

		if(allOnMask == snappers)
		{
			//printf("#%d ON\n", (i+1));
			output << "Case #" << (i+1) << ": ON\n";
		}
		else
		{
			//printf("#%d OFF?\n", (i+1));
			output << "Case #" << (i+1) << ": OFF\n";
		}
	}

	printf("Done!");
	getchar();
	return 0;
}