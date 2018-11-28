#include<iostream>
using namespace std;

int main()
{
int testcases,n;
int steps[100];
char robot[100];
cin>>testcases;

int t=1;
while(t<=testcases)
{
cin>>n;
for(int i=0;i<n;i++)
{
cin>>robot[i]>>steps[i];
}
int time=0;

int j=0;
int prevposa=1,prevposb=1;
int shift =0;
int prevtimeroboa=0,prevtimerobob=0;
while(j<n)
{
	if(robot[j]=='O')
	{
		shift = steps[j]-prevposa;
		if(shift<0)
		shift = -shift;
		prevposa = steps[j];
		if(time-prevtimeroboa>=shift)
		time = time+1;
		else
		{
		int timefactor =  shift-(time - prevtimeroboa) +1;
		//cout<<"timefactor "<<timefactor<<"\n";
		time+=timefactor;
		}
		prevtimeroboa = time;
		//cout<<"Entered robot O"<<shift<<"  "<<prevposa<<"   "<<time<<"\n";
	}
	else if(robot[j]=='B')
	{
		shift= steps[j]-prevposb;
		if(shift<0)
		shift = -shift;
		prevposb= steps[j];
		if(time-prevtimerobob>=shift)
		time = time+1;
		else
		{
		int timefactor = shift-(time - prevtimerobob) +1;
		//cout<<"timefactor "<<timefactor<<"\n";
		time = time+timefactor;
		}
		prevtimerobob = time;
		
		//cout<<"Entered robot B"<<shift<<"  "<<prevposb<<"   "<<time<<"\n";
	}
	j++;
}
	cout<<"Case #"<<t<<": "<<time<<"\n";
	t++;
}
}
	
	



