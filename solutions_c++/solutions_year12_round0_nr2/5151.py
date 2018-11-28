#include<iostream>
#include<fstream>
#include <cstdlib>
#include <stdio.h>
#include <string>
#include<list>

using namespace std;

void sort(int a[],int size)
{
	for(int j=1;j<size;j++)
	{
		for(int k=0;k<j;k++)
		{
			if(a[j]<a[k])
			{
				int temp=a[k];
				a[k]=a[j];
				a[j]=temp;
			}
		}
	}
}

void zeros(int a[])
{
	for(int i=0;i<30;i++)
		a[i]=0;
}

void main()
{
	int nscore,score,min,surprise,t,ti[30];
	int count=0;
	fstream in,out;

	std::string phrase;
	std::string file1= "./input.in";
	std::string file2= "./output.out";

	in.open(file1.c_str(),ios::in);
	out.open(file2.c_str(),ios::out);

	std::getline(in, phrase, '\n');
	
	t=atoi(phrase.c_str());

	for(int i=0;i<t;i++)
	{
		count=0;
		
		std::getline(in, phrase, ' ');
		nscore=atoi(phrase.c_str());

		std::getline(in, phrase, ' ');
		surprise=atoi(phrase.c_str());

		std::getline(in, phrase, ' ');
		min=atoi(phrase.c_str());
		zeros(ti);
//		cout<<"Start"<<endl;

		for(int k=0;k<nscore;k++)
		{
			if((k+1)!=nscore)
				std::getline(in, phrase, ' ');

			else
				std::getline(in, phrase, '\n');
			
			ti[k]=atoi(phrase.c_str());
		}

		sort(ti,nscore);

		for(int j=0;j<nscore;j++)
		{
			
			
			score=ti[j]/3;
			//cout<<ti[j]<<endl;
			int temp=ti[j];

			if(temp==30 || temp==29 || temp==28)
			{
				if(score>=min)
					count++;
			}

			else
			{
				if(score==0)
				{
					if(score==min)
						count++;
					continue;
				}

				if(score+2>=min && surprise!=0)
				{
					if((score*3)+2==temp || (score*3)+3==temp || (score*3)+4==temp)
					{
						count++;
						surprise--;
					}

					else
					{
						if(score+1>=min)
						{
							count++;
							surprise--;
						}

					}
				}

				else
				{
					if(score>=min || ((score+1==min) && ((score*3)+1==temp || (score*3)+2==temp)))
						count++;
				}
			}
			/*
			if(score>=min)
			{
				if(((score*3)==temp || ((score*3)+1)==temp || ((score*3)+2)==temp) && surprise!=nscore)
					count++;

				else
				{
					score--;
					if((((score*3)+2)==temp || ((score*3)+3)==temp || ((score*3)+4)==temp) && score>min) 
						count++;

				}

			}
	
			else
			{
				if((score+1)==min)
				{
					if(((score*3)+1)==temp || ((score*3)+2)==temp)
						count++;
				}

				else
				{
					
					if((score+2)>=min && surprise!=0)
					{
						if(((score*3)+2)==temp || ((score*3)+3)==temp || ((score*3)+4)==temp)
						{
							count++;
							surprise--;
						}
					}
				}
			}

			
			*/
			
		}
		
		out<<"Case #"<<i+1<<": "<<count<<'\n';
	}

	out.close();
	in.close();
	
	//system("pause");
}