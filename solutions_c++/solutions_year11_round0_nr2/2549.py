#include <iostream.h>
#include <fstream.h>

// Code Jam 2011
// Qualification Round
// B. Magicka


int main(int argc, char *argv[])
{
	int T,t;
	int N,n;
	int C,c;
	int D,d;
	
	char inchar;
	
	int index;

	char elementlist[100];
	char outputlist[100];
	char combinelist[36][3];
	char opposedlist[28][2];	
	ifstream inFile;
	
	//inFile.open("test.in");
	if ( argc < 2 )
	{
		cout << "No input file given!" << endl;
		exit(1);
	}
	inFile.open(argv[1]);
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> T;
	
	for (t=0;t<T;t++)
	{
		inFile >> C;
		
		for (c=0;c<C;c++)
		{
			inFile >> inchar;
			combinelist[c][0] = inchar;
			inFile >> inchar;
			combinelist[c][1] = inchar;
			inFile >> inchar;
			combinelist[c][2] = inchar;
		}
		
		inFile >> D;
		
		for (d=0;d<D;d++)
		{
			inFile >> inchar;
			opposedlist[d][0] = inchar;
			inFile >> inchar;
			opposedlist[d][1] = inchar;
		}
		
		inFile >> N;
		
		for (n=0;n<N;n++)
		{
			inFile >> inchar;
			elementlist[n] = inchar;
		}
		
		index = 0;
		
		outputlist[0] = elementlist[0];
		
		index++;
		
		for (n=1;n<N;n++)
		{
			outputlist[index++] = elementlist[n];
/*			for (d=0;d<index;d++)
			{
				cout << elementlist[d];
			}
*/
			for (c=0;c<C;c++)
			{
				if ( 	(outputlist[index-2] == combinelist[c][0] && outputlist[index-1] == combinelist[c][1])
						||
						(outputlist[index-2] == combinelist[c][1] && outputlist[index-1] == combinelist[c][0]) )
				{
					// elements combine
					outputlist[index-2] = combinelist[c][2];
					index = index-1;
					break;
				}
			}
			
			for (d=0;d<D;d++)
			{
				for (c=0;c<index-1;c++)
				{
					if ( 	(outputlist[c] == opposedlist[d][0] && outputlist[index-1] == opposedlist[d][1])
							||
							(outputlist[c] == opposedlist[d][1] && outputlist[index-1] == opposedlist[d][0]) )
					{
						// elements oppose
						index = 0;
					}
				}
			}
			
		}
		
		cout << "Case #" << t+1 << ": [";
		for (n=0;n<index;n++)
		{
			if ( n != 0 )
				cout << ", ";
			cout << outputlist[n];
		}
		cout << "]";
		cout << endl;
	}
		
		
	
	inFile.close();
	return 0;
}