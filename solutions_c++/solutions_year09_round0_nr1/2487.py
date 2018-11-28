#include <iostream>
#include <fstream>
#include <stack>

using namespace std;

ifstream  fin;
ofstream  fout;

int main()
{
	fin.open("small.in");
	fout.open("small.out");
	
	char numbers[100];

	fin.getline(numbers,100);

	int L = 0;
	int D = 0;
	int N = 0;
	int results[500];

	for(int a = 0; a <500; a++)
		results[a] = 0;

	sscanf(numbers,"%d %d %d",&L,&D,&N);

	char keywords[6000][20];

	for (int i = 0; i < D; i++)
	{
		fin.getline(keywords[i],20);
	}

	char words[600][1000];

	for (int i = 0; i < N; i++)
	{
		fin.getline(words[i],1000);
	}
    


	for (int i = 0; i < N; i++)
	{
		char wordsgroup[15][1000];
        int count = 0;

		for (int j = 0; words[i][j] != '\0'; j++)
		{
			if (words[i][j]=='(')
			{
				int temp = j+1;
				int count1 = 0;

				while (words[i][temp] != ')')
				{
				
					wordsgroup[count][count1]=words[i][temp];
                    count1++;
					temp++;
				}
				wordsgroup[count][count1]='\0';
				j=temp;
				count++;
		
			}
			else
			{
				wordsgroup[count][0]=words[i][j];
				wordsgroup[count][1]='\0';
				count++;
			}
		}
       
	   for (int k = 0; k < D; k++)
	   {
		   int indicate = 0;
		   for (int j = 0; j < L; j++)
		   {
		      char c = keywords[k][j];
			  int count2 = 0;
			  while(wordsgroup[j][count2] != '\0')
			  {
				  if (wordsgroup[j][count2] == c)
				  {    
					   indicate++;
				       count2++;
				  }
				  else
					  count2++;
			  }
		   }
		   if (indicate==L)
              results[i]++;
	   }
	}


	for (int y = 0; y < N; y++)
		fout<<"Case #"<<(y+1)<<": "<<results[y]<<endl;

}

