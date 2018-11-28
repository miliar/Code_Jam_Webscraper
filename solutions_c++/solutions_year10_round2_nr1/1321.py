///////////////////////////////////////////
//	File Fix-It
//	Empty win 32 console project
//	C++
///////////////////////////////////////////

#define INPUT_PATH "A-small.in"
#define OUTPUT_PATH "A.small.out"

#include <iostream>
#include <fstream>
using namespace std;

struct path
{
	char name[101];
	int lv;
	int parent;
};

int T,N,M;
char currentString[101];
int Exist, Added;
path data[1000];
int NumberData;


void main()
{
	ifstream input;
	input.open(INPUT_PATH);
	ofstream output;
	output.open(OUTPUT_PATH);
	input >> T;
	for (int i=0; i< T; i++)
	{
		NumberData = 0;
		Exist = 0;
		input >> N >> M;
		for (int j=0; j<N+M; j++)
		{
			input >> currentString;
			int k=0;
			int lv = 0;
			int parent = -1;
			while (k < strlen(currentString))
			{
				int l =k;
				while (currentString[l] != '/' && currentString[l] != 0) l++;
				if (l>k)
				{
					char buff[100];
					bool exist = false;
					strncpy(buff,currentString+k,l-k);
					buff[l-k] = 0;
					int z;
					for (z=0; z< NumberData; z++)
						if (strcmp(buff,data[z].name) == 0 
							&& lv == data[z].lv
							&& parent == data[z].parent) 
						{
							exist = true;
							break;
						}
					if (!exist)
					{
						data[NumberData].lv = lv;
						data[NumberData].parent = parent;
						strcpy(data[NumberData].name,buff);
						lv ++;
						parent = NumberData ++;
						if (j<N) Exist ++;
					}
					else
					{
						lv ++;
						parent = z;
					}
					k = l;
				}
				k++;
			}
		}

		output << "Case #" << i+1 << ": " << NumberData - Exist << endl;
		
	}
	input.close();
	output.close();
}