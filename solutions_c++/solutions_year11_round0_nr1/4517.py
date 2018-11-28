// bot trust.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<fstream>
#include<cmath>
#include<memory>
using namespace std;

int main()
{
	ifstream cin("A-large.in");
	int T;
	cin>>T;
	int i,j;
	int N;
	int print[100];
	for(i=0;i<T;i++)
	{
		cin>>N;
		int *time=new int[N];
		memset(time,0,N);
		int Opos=-1;
		int Bpos=-1;
		char color[100];
		int pos[100];
		memset(color,0,100);
		memset(pos,0,100);
		for(j=0;j<N;j++)
		{
			cin>>color[j]>>pos[j];
		}
		for(j=0;j<N;j++)
		{
			if(j==0)
			{
				if(color[j]=='O')
				{
					time[0]=pos[j];
					Opos=0;
				}
				else
				{
					time[0]=pos[j];
					Bpos=0;
				}
			}
			else
			{
				if(color[j]=='O')
				{
					if(Opos==-1)
					{
						if(time[j-1]>=pos[j])
						{
							time[j]=time[j-1]+1;
							Opos=j;
						}
						else
						{
							time[j]=pos[j];
							Opos=j;
						}
					}
					else
					{
						if(Opos==j-1)
						{
							time[j]=time[j-1]+abs(pos[j]-pos[j-1])+1; //绝对值
							Opos=j;
						}
						else
						{
							int temp=time[j-1]-time[Opos];
							//int temp=time[Opos+1]-time[Opos];
							/*for(int k=Opos+1;k<j-1;k++)
							{
								temp=temp+abs(pos[k+1]-pos[k])+1;  //绝对值
							}*/
							if(temp>=abs(pos[j]-pos[Opos])+1)
							{
								time[j]=time[j-1]+1;
								Opos=j;
							}
							else
							{
								time[j]=abs(pos[j]-pos[Opos])+1+time[Opos];
								Opos=j;
							}
						}
					}
				}
				else if(color[j]=='B')
				{
					if(Bpos==-1)
					{
						if(time[j-1]>=pos[j])
						{
							time[j]=time[j-1]+1;
							Bpos=j;
						}
						else
						{
							time[j]=pos[j];
							Bpos=j;
						}
					}
					else
					{
						if(Bpos==j-1)
						{
							time[j]=time[j-1]+abs(pos[j]-pos[j-1])+1; //绝对值
							Bpos=j;
						}
						else
						{
							int temp=time[j-1]-time[Bpos];
							/*int temp=time[Bpos+1]-time[Bpos];
							for(int k=Bpos+1;k<j-1;k++)
							{
								temp=temp+abs(pos[k+1]-pos[k])+1;  //绝对值
							}*/
							if(temp>=abs(pos[j]-pos[Bpos])+1)
							{
								time[j]=time[j-1]+1;
								Bpos=j;
							}
							else
							{
								time[j]=abs(pos[j]-pos[Bpos])+1+time[Bpos];
								Bpos=j;
							}
						}
					}
				}
			}
		}
		print[i]=time[N-1];
	}
	
	ofstream   fout; 
    fout.open( "A-large.in"); 
	for(i=0;i<T;i++)
	{
		fout<<"Case #"<<i+1<<": "<<print[i];
		fout<<endl;
	}
	
	return 0;
}
