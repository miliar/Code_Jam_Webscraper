#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cmath>


using namespace std;


ifstream fin;
ofstream fout;

double translate(char words[65]);


int main()
{
	fin.open("small3.in");
	fout.open("small3.out");

	char numbers[5];

	fin.getline(numbers,5);

	int T;

	sscanf(numbers,"%d",&T);

	char words[65];

	for (int i = 0; i < T; i++)
	{
		fin.getline(words,65);
		double dd = translate(words);
		int ii = dd;
		fout<<"Case #"<<(i+1)<<": "<<ii<<endl;
	}
}



double translate(char words[65])
{
	char *temp = words;
	int trackint = 2;
    char trackchar[65] = "";
	char *temptrack = trackchar;
	*temptrack = '1';

	while (*temp != '\0')
	{ 
		if (*temp == words[0])
            *temptrack = '1';
		else
			{   *temptrack = '0';
		        temptrack++;
				temp++;
			    break;
			}

        /*for (char *temp1 = words; temp1 != temp; temp1++)
		{
			if (*temp1 == *temp)
			{
				*temptrack = '1';
			}
			else
			{   *temptrack = '0';
			    break;
			}

		}*/

		temp++;
		temptrack++;
	}



	while (*temp != '\0')
	{
		bool same = false;
		char* temp2 = trackchar;
		for (char *temp1 = words; temp1 != temp; temp1++)
		{

			if (*temp1 == *temp)
			{
				*temptrack= *temp2;
				temptrack++;
				temp2++;
				same = true;
				break;
			}

			temp2++;
			/*else
			{   *temptrack = trackint + '0';
			    trackint++;
			}*/

		}

		if (!same)
		{
			*temptrack = trackint + '0';
			trackint++;
			temptrack++;
		}
		temp++;
	}

	*temptrack = '\0';

	//cout<<trackint<<endl;
	




	temptrack--;
	int t = *temptrack - '0';
	double p = 0;
	double num = 0;
	double b = trackint;

	char* temptrack1 = trackchar;
	while(*temptrack1 != '\0')
	{
		int t = *temptrack - '0';
		num += t*pow(b,p);
		temptrack--;
		temptrack1++;
		p++;
	}


    
	return num;

    
}





			



