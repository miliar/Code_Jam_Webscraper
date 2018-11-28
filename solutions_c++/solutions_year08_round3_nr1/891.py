#include <iostream>
#include <fstream>
#include <conio.h>

#define BUFFER_LINE 100000

using std::ifstream;
using std::ofstream;
using std::ios;

class Slot
{
public:
	Slot(int v) {val = v; next=NULL; prev=NULL;}
	int multiply;
	int val;
	Slot* next;
	Slot* prev;
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
			int P, K, L;
			sscanf(inbuf, "%d %d %d", &P, &K, &L);
			int maxSlot = P*K;

			inputFile.getline(inbuf,BUFFER_LINE);
			char delims[] = " ";   
			char *result = NULL;   
			Slot* header = NULL;
			result = strtok(inbuf, delims);   
			while(result!= NULL) 
			{     
				int cur = atoi(result);
				if(header == NULL)
				{
					header = new Slot(cur);
				}
				else
				{
					Slot* temp = header;
					Slot* add = NULL;
					while(temp->next!= NULL)
					{
						if(cur >= temp->val)
						{
							add = temp;
							break;
						}
						temp = temp->next;
					}

					if(temp->next == NULL)
					{
						if(cur >= temp->val)
							add = temp;
					}

					if(add != NULL)
					{
						if(add == header)
						{
							header->prev = new Slot(cur);
							header->prev->next = header;
							header = header->prev;
						}
						else
						{
							Slot* keep = new Slot(cur);
							keep->prev = add->prev;
							add->prev->next = keep;
							keep->next = add;
							add->prev = keep;
						}
					}
					else
					{
						temp->next = new Slot(cur);
						temp->next->prev = temp;
					}
				}
				result = strtok( NULL, delims );  
			}

			int multiply = 1;
			Slot* temp = header;
			for(int i=0; temp && i<P; i++)
			{
				for(int j=0; temp && j<K; j++)
				{
					temp->multiply = multiply;
					temp = temp->next;
				}
				multiply++;
			}

			int answer = 0;
			if(header)
			{
				Slot* temp = header;
				while(temp)
				{
					answer += (temp->val*temp->multiply);
					temp = temp->next;
				}
			}

			outputFile << "Case #" << iCase << ": " << answer << "\n";
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