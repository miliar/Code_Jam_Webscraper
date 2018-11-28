// GCJ_2011_1.cpp : Defines the entry point for the console application.
//

#include <iostream>
using namespace std;

int compare(int a, int b)
{
	if(a>b) return 1;
	else if(a<b) return -1;
	else return 0;
}
int dist(int a, int b)
{
	return ((a>b)?a-b:b-a);
}
int min(int a, int b)
{
	return ((a>b)?b:a);
}

int getmintime2()
{
	int numsteps,num_o,num_b;
	cin>>numsteps;
	char sequence[102];
	int seq_o[102];
	int seq_b[102];
	num_o = num_b =0;
	seq_o[num_o++]=1; seq_b[num_b++]=1;
	for(int i=0;i<numsteps;i++)
	{
		
		cin>>sequence[i];
		int but;
		cin>>but;
		(sequence[i]=='O')?seq_o[num_o++]=but:seq_b[num_b++]=but;
	}
	seq_o[num_o]=seq_o[num_o-1];
	seq_b[num_b]=seq_b[num_b-1];
	int time=0;
	int current =0;
	int current_o=1,current_posn_o=1;
	int current_b=1,current_posn_b=1;
	while(current!=numsteps)
	{
		if(sequence[current]=='O')
		{
		  int thistime = dist(current_posn_o,seq_o[current_o]) +1 ;
		  current_posn_o=seq_o[current_o];
		  time+=thistime;
		  current_o++;
		  current++;
		  current_posn_b += compare(seq_b[current_b],current_posn_b) * min(thistime,dist(seq_b[current_b],current_posn_b));
		}
		else
		if(sequence[current]=='B')
		{
		  int thistime = dist(current_posn_b,seq_b[current_b]) +1 ;
		  current_posn_b=seq_b[current_b];
		  time+=thistime;
		  current_b++;
		  current++;
		  current_posn_o += compare(seq_o[current_o],current_posn_o) * min(thistime,dist(seq_o[current_o],current_posn_o));
		}

	}
	return time;

}

int main(int argc, char* argv[])
{
	int num_test;
	cin>>num_test;
	for(int i=0;i<num_test;i++)
	{
		cout<<"Case #"<<i+1<<": "<<getmintime2()<<"\n";
	}
	return 0;
}

