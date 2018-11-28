#include <iostream>
using std::cin;
using std::cout;
using std::endl;

#include <stdio.h>
using namespace std;

#include <fstream>
using namespace std;

#include <string>
using namespace std;

#include <math.h>

int main()
{
	srand(12321);

	int i, j, k;
	string temp;

	int count[10];
	int count2[10];
	ofstream of("C:\\Documents and Settings\\customer\\Desktop\\A-small-out.txt");	
	//ofstream of("C:\\Documents and Settings\\customer\\Desktop\\A-large-out.txt");	
	ifstream f("C:\\Documents and Settings\\customer\\Desktop\\A-small.in");
	//ifstream f("C:\\Documents and Settings\\customer\\Desktop\\A-large.in");

	int cases;
	f >> cases;

	int number;
	for(i=0; i< cases; i++)
	{
		f >> number;

		for(j=0; j<10; j++)
		{
			count[j]=0;
		}

		for(k=0; k<9 && number >= pow(10.0f, k); k++)
		{
			count[(number % (int)pow(10.0f, k+1)) / (int)pow(10.0f, k)]+=1;
		}
	


		int good;
		int val;
		do
		{
			good=1;
			number++;

			for(j=0; j<10; j++)
			{
				count2[j]=count[j];
			}

			for(k=0; k<9 && number >= pow(10.0f, k); k++)
			{
				val=(number % (int)pow(10.0f, k+1)) / (int)pow(10.0f, k);
				if(val==0)
				{
					continue;
				}
				count2[val]-=1;
				if(count2[val]<0)
				{
					good=0;
					k=10;
					continue;
				}
			}

			if(good==1)
			{
				for(j=1; j<10; j++)
				{
					if(count2[j]>0)
					{
						good=0;
						j=11;
					}
				}
			}
		} while(good==0);
		cout << "Case #" << i+1 << ": " << number << endl;
		of << "Case #" << i+1 << ": " << number << endl;
	}


	cout << "done";
	char pause;
	cin >> pause;


	return 0;
}