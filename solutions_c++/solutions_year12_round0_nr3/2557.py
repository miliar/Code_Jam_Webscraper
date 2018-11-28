#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<set>
#include<string>
#include<string.h>
#include<fstream>

using namespace std;

long int combs[] = {0,0,1,3,6,10,15,21};
char arr[5000];
bool isComplete = false;
bool canShift(long int xx);
long int shift(long int num,long int xx);
long int up_limit,low_limit,tcount,pos=0,t,result,x=0,tot_shifts=0;
long int calculate_count();
int shifts[10],shift_pos=0;
long int retValue;
char snum[100];
void readFile();
void read_t();
long int get_int();

void main()
{
	readFile();
	read_t();
	for(int xx=0;xx<t;xx++)
	{
		
		low_limit = get_int();
		up_limit  = get_int();
		result = calculate_count();
		ofstream fout;
		fout.open("output.in",ios::app);
		fout << "Case #" << xx+1 << ": " << result<<"\n";
		fout.close();
	}
}

long int calculate_count()
{
	set<int>added;
	long int tot=0;
	long int shifted,sCount=0;
	char sLowLimit[100];
	sprintf(sLowLimit, "%d", low_limit);
	int len=strlen(sLowLimit);
	//ofstream fout;
	//fout.open("log.in",ios::app);
	for (long int xx=low_limit;xx<=up_limit;xx++)
	{
		added.clear();
		shifted = xx;
		tcount = 1;
		tot_shifts=0;
		for(int yy=0;yy<len,tot_shifts<len;yy++)
		{

			if(shifted <=up_limit && shifted >= low_limit && shifted >xx)
				{
					if(added.find(shifted) == added.end())
					{tcount++;added.insert(shifted);}
				}
			else if(shifted <=up_limit && shifted >= low_limit && shifted < xx)
				{tcount=0;break;}
			shifted = shift(shifted,xx);
		}
		tot = tot + combs[tcount];
		//fout << "At xx = " << xx << " Total = " << tot<< "\n";
	}
	//fout.close();
	cout << "yeah";
	return tot;
}
long int shift(long int num, long int beg)
{
	sprintf(snum, "%d", num);
	char t[10];
	do
	{	
		tot_shifts++;
		t[0]=snum[strlen(snum)-1];
		t[1]='\0';
		snum[strlen(snum)-1]='\0';
		strcat(t,snum);
		strcpy(snum,t);
	}while(snum[0] == '0');
	retValue = (atol(t));
	return retValue;
}

void readFile()
{
	ifstream fin;
	fin.open("input.in", ios::in);
	while(fin)
	{
		fin.get(arr[x]);
		//cout << arr[x];
		x++;
	}
	fin.close();
}

void read_t()
{
	while(arr[pos] != '\n')
	{
		t=(t*10) + (arr[pos] - '0');
		pos++;
	}
}

long int get_int()
{
	long int return_value=0;
	while(arr[pos] < '0' || arr[pos] > '9')
		pos++;
	while(arr[pos] >= '0' && arr[pos] <= '9')
		return_value = (return_value*10) + (arr[pos++]-'0');
	return return_value;
}
