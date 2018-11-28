#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

int main()
{
	int t,n;
	ifstream ifile;
	ofstream ofile;
	ifile.open("input.txt");
	ofile.open("output.txt");
	ifile>>t;
	char C[100];//=new char(n);
	int A[100];//=new int(n);
	for(int i=0;i<t;i++)
	{
		ifile>>n;
		for(int j=0;j<n;j++)
		{
			ifile>>C[j];
			ifile>>A[j];
		}
		char l_robot='\0',p_robot;
		int time=0,O_last_time=0,B_last_time=0;
		int O_pos=1,B_pos=1;
		for(int j=0;j<n;j++)
		{
			p_robot=C[j];
			int diff,time_diff;
			switch(p_robot)
			{
			case 'O':
				time_diff=time-O_last_time;
				if(l_robot==p_robot)
				{
					diff=abs(O_pos-A[j]);
					O_pos=A[j];					
					time+=diff+1;
					O_last_time=time;
				}
				else
				{
					diff=abs(O_pos-A[j]);
					if(diff>=time_diff)
					{
						O_pos=A[j];
						time+=(diff-time_diff)+1;
						O_last_time=time;
					}
					else
					{
						O_pos=A[j];
						time+=1;
						O_last_time=time;
					}
				}
				l_robot='O';
				break;
			case 'B':
				time_diff=time-B_last_time;
				if(l_robot==p_robot)
				{
					diff=abs(B_pos-A[j]);
					B_pos=A[j];
					time+=diff+1;
					B_last_time=time;
				}
				else
				{
					diff=abs(B_pos-A[j]);
					if(diff>=time_diff)
					{						
						B_pos=A[j];
						time+=(diff-time_diff)+1;
						B_last_time=time;
					}
					else
					{
						B_pos=A[j];
						time+=1;
						B_last_time=time;
					}
				}
				l_robot='B';
				break;
			}
		}
		ofile<<"Case #"<<i+1<<": "<<time<<"\n";
	}
	ifile.close();
	ofile.close();
}