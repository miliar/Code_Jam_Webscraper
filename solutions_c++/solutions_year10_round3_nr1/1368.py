#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

int main()
{

	ifstream infile("A-large.in");
	ofstream outfile("out.txt");

	unsigned int caseno,casecnt=0;
	unsigned long int nowires, cross,i,j;
	infile >> caseno;

	while(casecnt<caseno)
	{
		//cout << "Case #" << ++casecnt << ": ";
		outfile << "Case #" << ++casecnt << ": ";
		cout << "Case #" << casecnt << ": ";
		cross = 0;
		infile >> nowires;
		int left[nowires];
		int right[nowires];
		for(i=0;i<nowires;i++)
		{
			infile >> left[i] >> right [i];
		}
		for(i=0;i<nowires;i++)
		{
			for(j=i+1;j<nowires;j++)
			{
				if(left[j]>left[i] && right[j]<right[i]) cross++;
				if(left[j]<left[i] && right[j]>right[i]) cross++;
			}
		}
		cout << cross << endl;
		outfile << cross << endl;
	}
	return 0;
}
