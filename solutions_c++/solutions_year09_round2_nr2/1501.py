#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <string>
#include <queue>


using namespace std;

int main()
{
	ifstream fsi("prb22.in");
	ofstream fso("prb2.out");
	
	int tc;
	fsi >> tc;

	cout << "No of Test Cases -> " << tc << endl; 
	
	for ( int tcn =1;tcn<=tc ;tcn++ )
	{
		long int N;
		fsi>> N;
		printf("NUmber-> %ld\n",N);
		int num[25];
		for (int i = 0;i< 25 ;i++ )
		{
			num[i] = 0;
		}
		long int temp = N;
		int i = 0;
		while (temp != 0)
		{
			num[i] = temp%10;
			printf("%d ",num[i]);
			temp = temp/10;
			i++;
		}
		printf("\n");

		temp = num[0];
		int j;
		for (j= 1 ; ;j++ )
		{
			if(temp > num[j])
				break;
			else temp = num[j];
		}
		printf("j->%d\n",j);
		long int outnumber;
		

		for(int l = 0; l< j-1;l++)
		for (int k = 0; k< j-1; k++)
		{
			if(num[k+1]>num[k])
			{
				temp = num[k];
				num[k] = num[k+1];
				num[k+1] = temp;
			}
		}

		for (int k = j-1; k>=0 ;k-- )
		{
			if(num[k]>num[j])
			{
				temp = num[k];
				num[k] = num[j];
				num[j] = temp;
				break;
			}
		}

		for(int l = 0; l< j-1;l++)
		for (int k = 0; k< j-1; k++)
		{
			if(num[k+1]>num[k])
			{
				temp = num[k];
				num[k] = num[k+1];
				num[k+1] = temp;
			}
		}
		

		outnumber = 0;
		for (int z = 0;z<21 ;z++ )
		{
			outnumber = outnumber + (num[z]*pow(10,z));
		}
		printf("%ld \n",outnumber);

		fso << "Case #"<< tcn << ": ";
		printf("%d ",outnumber);
		fso<<outnumber;
		
		fso<<endl;
		printf("\n");
	}
}
