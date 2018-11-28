#include<iostream>
#include<fstream>
using namespace std;

__int32 check(__int32 runs,__int32 capacity,__int32 * groups,unsigned short size);

void main()
{
	unsigned short number_of_inputs,count=1;
	char *input_file=new char[20];
	char *output_file=new char[20];

	strcpy(input_file,"C-small-attempt1.in");
	strcpy(output_file,"output.txt");

	ifstream fin;
	fin.open(input_file);

	ofstream fout;
	fout.open(output_file);

	fin>>number_of_inputs;

	__int32 number=1;
	while(number_of_inputs--)
	{
		__int32 runs;
		__int32 capacity;
		unsigned short number_of_groups;

		fin>>runs;
		fin>>capacity;
		fin>>number_of_groups;

		__int32 *groups=new _int32[number_of_groups];
		unsigned short count=0;
		while(number_of_groups--)
		{
			__int32 temp;
			fin>>temp;
			groups[count++]=temp;
		}
				
		//count == size
		__int32 money=check(runs,capacity,groups,count);
		fout<<"Case #"<<number++<<": "<<money<<endl;

	}
}

__int32 check(__int32 runs,__int32 capacity,__int32 * groups,unsigned short size)
{
	__int32 total_sum=0;
	short index=0;

	for(int i=0;i<runs;i++)
	{		
		__int32 sum=0;
		int count=0;
		int flag=0;
		while(1)//sum<=capacity && count<size)
		{
			
			sum=sum+groups[index++];
			if(index>=size)
			{
				index=0;
			}
			count++;
			if(sum>capacity)
			{
				flag=1;
				break;
			}
			if(count>=size)
			{
				flag=2;
				break;
			}
		}
		if(flag==1)
		{
			index--;
			if(index<0)
			{
				index=size-1;
			}
			sum=sum-groups[index];
		}				

		total_sum=total_sum+sum;		
	}
	return total_sum;
}