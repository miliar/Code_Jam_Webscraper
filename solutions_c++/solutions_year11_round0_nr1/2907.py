/*Bot Trust*/

#include<cstdio>
#include<iostream>

using namespace std;

char robot[100];
int blue[100],button[100],orange[100];

int main()
{
	int bindex,bpos,i,j,N,oindex,opos,T,time;
	freopen("A-large.in","rt",stdin);
	freopen("A.out","wt",stdout);
	cin>>T;
	for(i=1;i<=T;i++)
	{
		cin>>N;
		bindex=oindex=0;
		for(j=0;j<N;j++)
		{
			cin>>robot[j]>>button[j];
			if(robot[j]=='B')
				blue[bindex++]=button[j];
			else
				orange[oindex++]=button[j];
		}
		bpos=1;
		opos=1;
		time=0;
		j=0;
		bindex=oindex=0;
		while(j<N)
		{
			time++;
			if(robot[j]=='B')
			{
				if(bpos==button[j])
					j++,bindex++;
				else if(bpos<button[j])
					bpos++;
				else
					bpos--;
				if(opos<orange[oindex])
					opos++;
				else if(opos>orange[oindex])
					opos--;
			}
			else
			{
				if(opos==button[j])
					j++,oindex++;
				else if(opos<button[j])
					opos++;
				else
					opos--;
				if(bpos<blue[bindex])
					bpos++;
				else if(bpos>blue[bindex])
					bpos--;
			}
		}
		printf("Case #%d: %d\n",i,time);
	}
	return 0;
}