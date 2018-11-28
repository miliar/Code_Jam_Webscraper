#include<iostream>
#include<fstream>
#include<sstream>
#include<string>

using namespace std;

int main()
{
	int num_t;
	
	ifstream myfile;
	myfile.open ("B-small-attempt0.in", ios::in);
	myfile>>num_t;
	myfile.ignore();
	int data[num_t][6];
	for(int t = 0; t<num_t; t++)
	{
		string tempstr;
		getline(myfile, tempstr);
		istringstream iss(tempstr);
		int temp, i=0;
		while(iss >> temp)
		{
			data[t][i]=temp;
			i++;
		}
		//myfile.getline(test[t], 101);
	}
	
	myfile.close();
	ofstream myfileout;
	myfileout.open ("B-small-attempt0.out", ios::out);
	for(int t = 0; t<num_t; t++)
	{
		int split[data[t][0]][4], counts=0;
		
		for(int i=3; i<(data[t][0]+3); i++)
		{
			int temp = data[t][i];
			
			if(temp==0)
			{
				split[i-3][0]=0;
				split[i-3][1]=0;
				split[i-3][2]=0;
				split[i-3][3]=0;
			}
			else if(temp==1)
			{
				split[i-3][0]=0;
				split[i-3][1]=0;
				split[i-3][2]=1;
				split[i-3][3]=0;
			}
			else if(temp==30)
			{
				split[i-3][0]=10;
				split[i-3][1]=10;
				split[i-3][2]=10;
				split[i-3][3]=0;
			}
			else if(temp==29)
			{
				split[i-3][0]=9;
				split[i-3][1]=10;
				split[i-3][2]=10;
				split[i-3][3]=0;
			}
			else
			{
				if(temp%3==0 || temp%3==2)
				{
					split[i-3][1]= temp/3;
					temp-=split[i-3][1];
					split[i-3][0]=(temp/2)-1;
					split[i-3][2]=(temp/2)+1;
					split[i-3][3]=1;
				}
				else
				{ 
					split[i-3][0]= (temp/3)-1;
					temp-=split[i-3][0];
					split[i-3][1]=(temp/2);
					split[i-3][2]=(temp/2);
					split[i-3][3]=1;
				}
				counts++;
			}
		}
		
		int diffs = counts-data[t][1], i = 0;
		while(diffs != 0 && i<data[t][0])
		{
			if(split[i][3]==0 || split[i][2]>=data[t][2]) ;
			else
			{
				if(split[i][0]==split[i][1] - 2)
				{
					split[i][0]++;
					split[i][1]--;
					diffs--;
				}
				else if(split[i][0]==split[i][2] - 2)
				{
					split[i][0]++;
					split[i][2]--;
					diffs--;
				}
			}
			i++;
		}
		i=0;
		while(diffs != 0)
		{
			if(split[i][3]==0);
			else
			{
				if(split[i][0]==split[i][1] - 2)
				{
					split[i][0]++;
					split[i][1]--;
					diffs--;
				}
				else if(split[i][0]==split[i][2] - 2)
				{
					split[i][0]++;
					split[i][2]--;
					diffs--;
				}
			}
			i++;
		}
		int counth=0;
		for(int i=3; i<(data[t][0]+3); i++)
		{
			if(split[i-3][2]>=data[t][2]) counth++;
		}
		myfileout<<"Case #"<<t+1<<": "<<counth<<"\n";
	}
	return 0;
}
	