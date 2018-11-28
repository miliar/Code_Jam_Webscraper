#include<iostream>
#include<fstream>
using namespace std;

void findUp(int **ptr,int start,int end,int &intersection);
void findDown(int **ptr,int start,int end,int &intersection);

void main()
{
	unsigned short number_of_inputs,count=1;
	char *input_file=new char[20];
	char *output_file=new char[20];

	strcpy(input_file,"A-small-attempt4.in");
	//strcpy(input_file,"input.txt");
	strcpy(output_file,"output.txt");
	
	ifstream fin;
	fin.open(input_file);

	ofstream fout;
	fout.open(output_file);
	
	fin>>number_of_inputs;
	//cout<<number_of_inputs;

	int **ptr=new int*[10000];
	for(int i=0;i<10000;i++)
	{
		ptr[i]=new int[2];
		ptr[i][0]=0;
		ptr[i][1]=0;
	}

	while(number_of_inputs--!=0)
	{
		int wires=0;
		fin>>wires;

	for(int i=0;i<10000;i++)
	{
		ptr[i][0]=0;
		ptr[i][1]=0;
	}

		int left_window;
		int right_window;

		for(int i=0;i<wires;i++)
		{
			fin>>left_window;
			ptr[left_window][0]=1;

			fin>>right_window;
			ptr[left_window][1]=right_window;
		}
		
		int intersection=0;
		int wire_count=0;
		for(int i=1;i<=10000 && wire_count < wires;i++)
		{
			if(ptr[i][0]==1)
				wire_count++;

			if(i!=ptr[i][1] && ptr[i][0]==1)		
			{
				int diff=i-ptr[i][1];
				if(diff<0)
				{
					findUp(ptr,i,ptr[i][1],intersection);
				}
				else
				{
					findDown(ptr,ptr[i][1],i,intersection);
				}
			}
		}
		fout<<"Case #"<<count++<<": ";
		fout<<intersection;
		fout<<endl;
	}
}

void findUp(int **ptr,int start,int end,int &intersection)
{
	for(int i=start;i<end;i++)
	{
		if(ptr[i][1]<ptr[start][1] && ptr[i][0]==1)
			intersection++;
	}
}

void findDown(int **ptr,int start,int end,int &intersection)
{
	for(int i=end;i>start;i--)
	{
		if(ptr[i][1]>ptr[end][1] && ptr[i][0]==1)
			intersection++;
	}
}