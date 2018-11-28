#include <iostream>
#include <conio.h>
#include <string>
#include <fstream>


using namespace std;


void main()
{
	string line;
	std::freopen("output_Recycle.txt", "w", stdout);
	ifstream file("C-small-attempt0.in", ios::in);
	
	if(!file)
		cout<<"File not opened\n";
	
	int sum=0;
	int count;
	file>>count;

	for(int i=0;i<count;i++)
	{
		int n1,n2;
		file>>n1;
		file>>n2;
		sum=0;

		int range=n2-n1+1;
		
		int* ptr=new int[range];

		for(int i=0;i<range;i++) //copying numbers to array
		{
			ptr[i]=i+n1;
		}

		//traversing the array
		for(int j=0;j<range;j++)
		{
			int temp=ptr[j];
			int size=0;

			while(temp>0)
			{
				temp=temp/10;
				size++;
			}

			//making all alternatives
			for(int k=1;k<size;k++)
			{
				temp=ptr[j];
				int head=temp/(int)pow((float)10,k);
				temp=temp-head*(int)pow((float)10,k);
				temp=temp*(int)pow((float)10,size-k)+head;

				//calculating size of the other combination

				int temp1=temp;
				int size1=0;

				while(temp1>0)
				{
					temp1=temp1/10;
					size1++;
				}

										
				if(size==size1)
				{
				
					for(int l=j+1;l<range;l++)
					{
						if(l!=j)
						{
							if(temp==ptr[l]&&temp>ptr[j])
							{
								sum++;
								break;
							}
						}

					}
				}
			}

			/*for(int m=j;m<range-1;m++)
			{
				ptr[m]=ptr[m+1];
			}
			j--;
			range--;
			*/

		}

		cout<<"Case #"<<i+1<<": ";
		cout<<sum<<endl;

		delete [] ptr;
	}

	
}