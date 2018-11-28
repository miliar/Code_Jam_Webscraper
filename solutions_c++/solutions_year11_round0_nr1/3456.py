/*
// gcja.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	return 0;
}

*/
#include "stdafx.h"
#include<iostream>
#include<fstream>
#include<conio.h>
//#include<inttypes.h>
//#include<iomanip>
//#include<assert.h>
//#include<ctype.h>
//#include<errno.h>
//#include<float.h>
//#include<limits.h>
//#include<locale.h>
//#include<math.h>
//#include<string.h>
//#include<stdarg.h>
//#include<stddef.h>
//#include<stdint.h>
#include<stdio.h>
//#include<stdlib.h>
//#include<time.h>
//#include<wchar.h>
//#include<wctype.h>
//#include<bigint.h>
//#include<bigint.cpp>
//#define bigint CBigInt
//#include"ritwik.h"
using namespace std;
struct ts {
	char color;
	int pos;
};

void getNextTask(char clr,struct ts * task,int *dest,int *task_number,int total_task)
{
	for(int i = *task_number+1;i<total_task;i++)
	{
		if(task[i].color==clr)
		{
			*dest = task[i].pos;
			*task_number = i;
			return;
		}
	}
}
int main()
{
	int t;
	ifstream fi("A-small-attempt0.in",ios::binary|ios::in);
	ofstream fo("outputAs.out",ios::out);
	fi>>t;
	//cin>>t;
	
	for(int t_c=0;t_c<t;t_c++)
	{
		//fi>>n;
		int time=0;
		int	pos_O=1,pos_B=1;
		int total_task=0;

		//cin>>total_task;
		fi>>total_task;

		struct ts * task = new struct ts[total_task];
		int task_counter=-1;
		int O_task_number=-1,B_task_number=-1;
		int O_dest=1,B_dest=1;
		
		time = 0;
		
		for(int i=0;i<total_task;i++)
			fi>>task[i].color>>task[i].pos;
			
		for(int i=0;i<total_task;i++)
			cout<<task[i].color<<task[i].pos<<endl;
		
		
		
		getNextTask('O',task,&O_dest,&O_task_number,total_task);
		getNextTask('B',task,&B_dest,&B_task_number,total_task);
		
		int task_done=0;
		while(task_counter<total_task-1)
		{
			task_done=0;
			if(pos_O==O_dest)
			{
				if(task_counter==O_task_number-1)
				{
					task_counter++;
					task_done=1;
					getNextTask('O',task,&O_dest,&O_task_number,total_task);
				}
			}
			else
			{
				if(pos_O<O_dest)	pos_O++;
				else				pos_O--;
			}
			
			if(pos_B==B_dest)
			{
				if((task_counter==B_task_number-1)&&(task_done==0))
				{
					task_counter++;
					getNextTask('B',task,&B_dest,&B_task_number,total_task);
				}
			}
			else
			{
				if(pos_B<B_dest)	pos_B++;
				else		pos_B--;
			}
			time++;
		}
		
		fo<<"Case #"<<t_c+1<<": "<<time<<endl;
		//cout<<"Case #"<<t_c+1<<": "<<time<<endl;
		cout<<"task "<<t_c<<" completed";
	}
	fi.close();
	fo.close();
	return 0;
}