#include <fstream>
#include <sstream>
#include <string>
#include <iostream>
#include <stdlib.h>
using namespace std;
#define N 100
int leastP(int *totalArray);
int main()
{
	ifstream infile("F:\\B-large.in");
	ofstream outfile("outputDWG.txt");
	int totalArray[N+3] = {0};
	string strArray[N+3];
	string line;
	string temp;
	int i =0;
	int times =1;
	getline(infile,temp);

	while (getline(infile,line))
	{
		istringstream stream(line);
		/*while(stream >> temp)
		{
			toltalArray[i] = atoi(temp.c_str());
			i++;
		}*/
		while(stream >> totalArray[i++])
		;	
		int out=leastP(totalArray);
		outfile << "Case #"<< times << ": "<< out <<'\n';
		cout<< out<< endl;
		//do some thing here;
		i = 0;	
		times++;
	}
	/*for (int index = 0;index < N+3;index++)
	{
		cout <<totalArray[index] <<endl;
	}*/
	infile.close();
	outfile.close();
}

int leastP(int *totalArray)
{
	int n = totalArray[0];
	int s = totalArray[1];
	int p = totalArray[2];
	int result = 0;
	int a;
	for(int i= 3; i < n+3;i++)
	{
		//cha 1
		int tmp = totalArray[i];
		if (tmp ==0)
		{
			if (p==0)
				result++;
			continue;
		}
		if (tmp % 3==0)
		{
			a = tmp/3;
			if (a>=p)
			{
				result++;
				continue;
			}
			if ((a+1)>=p)
			{
				if (s)
				{
					result++;
					s--;
				}
				continue;
			}
		}
		if ((tmp+1) %3 ==0)
		{
			a =(tmp+1)/3;
			if (a>=p)
			{
				result++;
				continue;
			}
		}
		if ((tmp+2)%3 ==0)
		{
			a =(tmp+2)/3;
			if (a>=p)
			{
				result++;
				continue;
			}
		}//end cha 1
		if ((tmp+4)%3==0)
		{
			a = (tmp+4)/3;
			if (a>=p)
			{
				if (s)
				{
					result++;
					s--;
				}
				continue;
			}
		}
	}
	return result;
}