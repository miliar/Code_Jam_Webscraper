#include <iostream>
#include <fstream>
#include <conio.h>

#define BUFFER_LINE 5000

using std::ifstream;
using std::ofstream;
using std::ios;

class Box
{
public:
	int value;
	bool used;
};

int main()
{
	ifstream inputFile("Input.txt");
	char inbuf[BUFFER_LINE];
	if(inputFile.good())
	{
		ofstream outputFile("Output.txt", ios::out);
		inputFile.getline(inbuf,BUFFER_LINE);
		int nCase = atoi(inbuf);
		for(int iCase = 1; iCase <= nCase; iCase++)
		{
			inputFile.getline(inbuf,BUFFER_LINE);
			int max = atoi(inbuf);

			Box* buffer = (Box*)malloc(max*sizeof(Box));
			for(int i=0; i<max; i++)
				buffer[i].used = false;

			int index = 0;
			for(int j=1; j<=max; j++)
			{
				int select = 0;
				do
				{
					if(!buffer[index].used) 
						select++;
					if(++index>max) 
						index = 0;
				}
				while(select!=j);

				buffer[index-1].value = j;
				buffer[index-1].used = true;
			}

			outputFile << "Case #" << iCase << ":";

			inputFile.getline(inbuf,BUFFER_LINE);
			char delims[] = " ";   
			char *result = NULL;   
			result = strtok(inbuf, delims);   
			bool skip = true;
			while(result!= NULL) 
			{     
				if(!skip)
				{
				 int need = atoi(result); 
				 outputFile << " " << buffer[need-1].value;
				}
				else
					skip = false;
				result = strtok( NULL, delims );  
			}
			outputFile << "\n";

			free(buffer);
		}
		inputFile.close();
		outputFile.close();
	}
	else
	{
		printf("Error : Can not open input file.\n");
	}

	printf("Press any key to continue...");
	getch();
	return 0;
}