#include <stdio.h>
#include <iostream>
#include<string.h>
#include<fstream>
using namespace std;

int main(int argc, char *argv[])
{
	ifstream myfile;
	ofstream outfile;
	outfile.open("A-large.out");
	myfile.open("A-Large.in");
	string tempStr;
	int L,D,N;
	string *str;
	myfile>>L>>D>>N;
	cout<<L<<" "<<" "<<D<<" "<<N<<endl;
	str = new string[D];
	int *index,*tempIndex,*temp;
	index = new int[D+1];
	tempIndex = new int[D+1];
	for (int i=0;i<D ;i++ )
	{
		myfile>>str[i];
		index[i] = i;
	}
	index[D] = -1;

	for (int i=0;i<D ;i++ )
	{
		cout<<str[i]<<endl;
	}
	char ch;
	int j,k,p,m;
	for (int n=0;n<N ;n++ )
	{
		for (int i=0;i<D ;i++ )
		{
			index[i] = i;
		}
		index[D] = -1;
		for (int i=0;i<L ;i++ )
		{
			myfile>>ch;
			if (index[0]== -1)
			{
				myfile>>tempStr;
				break;
			}
			k = 0;p=0;
			if (ch=='(')
			{
				while (1)
				{
					myfile>>ch;
					if (ch==')')
					{
						break;
					}
					j=0;p=0;
					while (index[j] != -1)
					{
						if (str[index[j]][i] == ch)
						{
							tempIndex[k] = index[j];
							k++;
						}
						/*else 
						{
							index[p] = index[j];
							//index[p+1] = index[j+1]; //firesafety
							p++;
						}*/
							j++;
							
					}
					//index[p+1] = -1;
				}
			}
			else
			{
				j=0;
				while (index[j] != -1)
				{
					if (str[index[j]][i] == ch)
					{
						tempIndex[k] = index[j];
						k++;
					}
					j++;
				}
			}
				tempIndex[k] = -1;
				temp = index;

				index = tempIndex;
				tempIndex = temp;

			}
			m = 0;
			while( index[m] !=-1)
			{
				m++;
			}
			outfile<<"Case #"<<n+1<<": "<<m<<endl;
			
	}

	outfile.close();
	myfile.close();
	return 0;
}
