#include<iostream>
#include<windows.h>
#include<string>
#include<fstream>
#include<iomanip>
#include<direct.h>
#include<queue>
#include<algorithm>

using namespace std;

struct Node{
bool state;//true表ON状态 FALSE表OFF状态
bool power;//TRUE表接到电了 FALSE表示没有接到电
};

bool swichs(bool olds)
{
	if(olds == true)
		return false;
	else return true;
}

int main()
{
	string fileinname,filename;
	fileinname = "smallinput.txt";
	fstream foutfileinname("A-small-attempt0.in");
	//fstream foutfileinname("smallinput.txt");
	filename = "A-small-attempt0.out";
	fstream foutfilename(filename.c_str(), ios::out);
	int caseint,n,i,k,j,p,q,x,y;
	Node T[13];
	//scanf("%d",&caseint);
	foutfileinname>>caseint;



/*	for(i=0;i<caseint;i++)
	{
		//scanf("%d %d",&n,&k);
		foutfileinname>>n>>k;
		//printf("Case #%d: ",i+1);
		foutfilename<<"Case #"<<i+1<<": "; 
		if(n==1)
		{
			if(k%2 == 0 || k==0)
				//printf("OFF");
			foutfilename<<"OFF";
			else if(k%2 == 1)
				//printf("ON");
				foutfilename<<"ON";
		}
		else if(n>1)
		{
			if(k%2 == 1 && k != 1)
			{
				//printf("ON");
				foutfilename<<"ON";
			}
			else
				//printf("OFF");
				foutfilename<<"OFF";
		}
	//	printf("\n");
*/
	for(i=0;i<caseint;i++)
	{
		foutfileinname>>n>>k;
		//initially
		T[0].power=true;//第一个通电的
		T[0].state=false;//状态刚开始都为OFF
		for(j=1;j<n;j++)
		{
			T[j].power=false;
			T[j].state=false;
		}
		for(p=0;p<k;p++)
		{
			for(j=0;j<n;j++)
			{
				//如果当前开关通电的话
				if(T[j].power == true)
				{
					//改变状态
					T[j].state = swichs(T[j].state);
				}
			}

			//更改后面的通电状态
			for(j=1;j<n;j++)
			{
				//bool temp1=true;
				if(T[j-1].power == true && T[j-1].state == true)
				{
					T[j].power = true;
				}
				else T[j].power = false;
				/*for(x=0;x<j;x++)
				{
					if(T[x].power == false || T[x].state == false)
					{
						temp1=false;
						break;
					}
				}*/
				/*if(temp1 == true)
					T[j].power = true;
				else T[j].power = false;
				//else T[j].power = false;
				//如果这道闸门打开了 一路往下送电
				if(T[j].state == true && T[j].power == true)
					{
						for(q=j+1;q<n && T[q-1].state == true ; q++)
						{
							T[q].power = true;
						}
					}*/
			}
/*
			for(j=1;j<n;j++)
			{
				bool temp1=true;
				for(x=0;x<j;x++)
				{
					if(T[x].power == false || T[x].state == false)
					{
						temp1=false;
						break;
					}
				}
				if(temp1 == false)
					T[j].power = false;
				//else T[j].power = false;
				//如果这道闸门打开了 一路往下送电
				if(T[j].state == true && T[j].power == true)
					{
						for(q=j+1;q<n && T[q-1].state == true ; q++)
						{
							T[q].power = true;
						}
					}
			}
*/

			//更改后面的开关状态
			/*for(j=1;j<n;j++)
			{
				//前一个是OFF状态或者不通电 下一个就断电
				if(T[j-1].state == false || false == T[j-1].power)
				{
					T[j].power = false;
				}
			}*/

			

			


		}

		//最后查看是否通电 
			bool res = true;
		/*for(p=0;p<n;p++)
		{
			if(T[p].power == false || T[p].state ==false)
			{
				res = false;
				break;
			}
		}*/
		//if(res == false)
		if(T[n-1].power == true && T[n-1].state ==true)
			foutfilename<<"Case #"<<i+1<<": ON";
		else 
			foutfilename<<"Case #"<<i+1<<": OFF";

		if(caseint != i)  foutfilename<<"\n";
	}

}