#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <iostream.h>

#define LINE_SIZE 101
#define SMAX 100
char engine_buffer[SMAX*LINE_SIZE];
char line[LINE_SIZE];

struct tagFlag{
	unsigned __int64 A;
	unsigned __int64 B;
} flag;


int compare (const void * a, const void * b)
{
  return strcmp((const char *)a,(const char *)b);
}

void setBit(int j){
	if(j<64)
	{
		unsigned __int64 mask=1<<j;
		flag.A=flag.A|mask;
	}
	else
		if(j<128)
		{
			j=j-64;
			unsigned __int64 mask=1<<j;
			flag.B=flag.B|mask;
		}
		else{
			printf("ERROR:setBit()\n");
		}
}

void clearBit(int j){
	if(j<64)
	{
		unsigned __int64 mask=0xFFFFFFFFFFFFFFFF^(1<<j);
		flag.A=flag.A&mask;
	}
	else
		if(j<128)
		{
			j=j-64;
			unsigned __int64 mask=0xFFFFFFFFFFFFFFFF^(1<<j);
			flag.B=flag.B&mask;
		}
		else{
			printf("ERROR:clearBit()\n");
		}
}

void init(){
	freopen("A-large.in","r",stdin);
	freopen("myout_large.txt","w",stdout);
}

void main(){

	init();

	int N;

	cin.getline(line,LINE_SIZE);
	N=atoi(line);
	for(int i=0;i<N;i++)
	{
		
		int switch_num=0;
		int SN;
		int QN;

		cin.getline(line,LINE_SIZE);
		SN=atoi(line);
		//TODO:there should be an initialize to enginebuffer,Flag(0)
		flag.A=0;
		flag.B=0;
		for(int j=0;j<SMAX*LINE_SIZE;j++)
			engine_buffer[j]=0;

		for(j=0;j<SN;j++)
		{
			cin.getline(&engine_buffer[j*LINE_SIZE],LINE_SIZE);
			setBit(j);
		}
		qsort(engine_buffer,SN,LINE_SIZE,compare);


		cin.getline(line,LINE_SIZE);
		QN=atoi(line);
		for(j=0;j<QN;j++)
		{
			cin.getline(line,LINE_SIZE);
			char* ans=(char *)bsearch(line,engine_buffer,SN,LINE_SIZE,compare);
			int index=(ans-engine_buffer)/LINE_SIZE;
			clearBit(index);
			if(flag.A==0&&flag.B==0)
			{
				for(int p=0;p<SN;p++)
					setBit(p);
				clearBit(index);
				
				switch_num++;
			}
		}
		cout<<"Case #"<<(i+1)<<": "<<switch_num<<endl;
	}
}

