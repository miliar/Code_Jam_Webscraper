#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#define A 0
#define B 1
using namespace std;

class Event
{
	public:
	int time;
	char type;
	int from;
	int to;

	void setData(int ti, char ty, int f, int t)
	{
		time = ti;
		type = ty;
		from = f;
		to = t;
	}
};
int timeInMin(char *s);
int main(int argc, char *argv[])
{	
	FILE *fin,*fout;
	int cases;
		
	// Fetch # of Input...
	fin = fopen(argv[1],"r");
	if(fin==NULL)
	{cout<<"Unable to open INPUT File.";}
	fout = fopen(argv[2],"w");
	if(fout==NULL)
	{cout<<"Unable to open OUTPUT File.";}

	fscanf(fin,"%d",&cases);
	cout<<"cases="<<cases<<endl;

	int TAT, NA, NB;
	Event list[400];
	for(int i=1;i<=cases;i++)
	{
		// Step_1: Fetch TAT.
		fscanf(fin,"%d",&TAT);
		
		// Step_2: Find # of trips.
		fscanf(fin,"%d %d",&NA,&NB);
		
		// Step_3: Update events.
		char t1[6],t2[6];
		for(int j=0;j<NA;j++)
		{
			fscanf(fin,"%s %s",t1,t2);
			list[2*j].setData(timeInMin(t1),'d',A,B);
			list[2*j+1].setData(timeInMin(t2)+TAT,'a',A,B);
		}	
		for(int j=0;j<NB;j++)
		{
			fscanf(fin,"%s %s",t1,t2);
			list[2*(NA+j)].setData(timeInMin(t1),'d',B,A);
			list[2*(NA+j)+1].setData(timeInMin(t2)+TAT,'a',B,A);
		}
	
		// Step_4: Sort Even list.
		for(int j=0;j<2*(NA+NB);j++)
		{
			for(int k=j+1;k<2*(NA+NB);k++)
			{
				if(list[j].time>list[k].time)
				{
					Event temp;
					temp = list[j];
					list[j] = list[k];
					list[k] = temp;
				}
				else if(list[j].time==list[k].time && list[j].type=='d' && list[k].type=='a')
				{
					Event temp;
					temp = list[j];
					list[j] = list[k];
					list[k] = temp;
				} 	
			}
		}

		// Step_5: Calculate answer.
		int avail[2];
		int Ntrains[2];	
		avail[A]=0; // for A
		avail[B]=0; // for B
		Ntrains[A]=0;
		Ntrains[B]=0;
		for(int j=0;j<2*(NA+NB);j++)
		{
			if(list[j].type=='d')
			{
				if(avail[list[j].from]==0)
				{
					Ntrains[list[j].from]++;
					avail[list[j].from]++;				
				}
				avail[list[j].from]--;				
			}
			else if(list[j].type=='a')
			{
				avail[list[j].to]++;
			}
		}	

		// Step_6: Write Answers.
		fprintf(fout,"Case #%d: %d %d\n",i,Ntrains[A],Ntrains[B]);

	}

	fclose(fin);
	fclose(fout);
	return 0;
}

int timeInMin(char *s)
{
	char h[3];
	char m[3];
	int min;

	h[0]=s[0]; h[1]=s[1]; h[2]='\0';
    m[0]=s[3]; m[1]=s[4]; m[2]='\0';

	min = atoi(h)*60+atoi(m);

	cout<<"TIME="<<s<<",MIN="<<min<<endl;
	return min;
}
