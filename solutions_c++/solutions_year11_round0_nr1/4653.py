#include<iostream>
#include<cstring>
#include<cstdio>
#include<stdlib.h>
#include<cmath>
using namespace std;
int main()
{
	FILE *p1;
	p1=fopen("a.txt","r");
	int T,N,i,j,curr_posO=1,curr_posB=1,curr_time=0,Onext,Bnext,k=0,button[100],x,time[100];
	char robot[100];
	for(x=0;x<100;x++)
	{
		robot[x]='N';
		button[x]=1;
	}
	fscanf(p1,"%d",&T);
	cout<<"t value is "<<T<<endl;
	for(j=0;j<T;j++)
	{
		fscanf(p1,"%d",&N);
		cout<<"N value is "<<N<<endl;
		for(i=0;i<N;i++)
		{
			fscanf(p1,"%s",&robot[i]);
			fscanf(p1,"%d",&button[i]);
			cout<<robot[i]<<" "<<button[i]<<endl;
		}
		i=0;
		curr_posO=1;
		curr_posB=1;
		for(curr_time=0;i<N;curr_time++)
		{
			for(k=i+1;(robot[k]==robot[i]) && k<N;k++)
			{
			}
//			cout<<"k is "<<k<<endl;
			switch(robot[i])
			{
				case 'O':
					{

						if(curr_posO==button[i])
						{
							if(curr_posB>button[k])
							{
								curr_posB--;
							}
							if(curr_posB<button[k])
							{
								curr_posB++;
							}
							i++;
							break;
						}
						if(curr_posO<button[i])
						{
							if(curr_posB>button[k])
							{
								curr_posB--;
							}
							if(curr_posB<button[k])
							{
								curr_posB++;
							}
							curr_posO++;
							break;
						}
						if(curr_posO>button[i])
						{
							if(curr_posB>button[k])
							{
								curr_posB--;
							}
							if(curr_posB<button[k])
							{
								curr_posB++;
							}
							curr_posO--;
							break;
						}
					}
				case 'B':
					{
						if(curr_posB==button[i])
						{
							if(curr_posO>button[k])
							{
								curr_posO--;
							}
							if(curr_posO<button[k])
							{
								curr_posO++;
							}
							i++;
							break;
						}
						if(curr_posB<button[i])
						{
							if(curr_posO>button[k])
							{
								curr_posO--;
							}
							if(curr_posO<button[k])
							{
								curr_posO++;
							}
							curr_posB++;
							break;
						}
						if(curr_posB>button[i])
						{
							if(curr_posO>button[k])
							{
								curr_posO--;
							}
							if(curr_posO<button[k])
							{
								curr_posO++;
							}
							curr_posB--;
							break;
						}
					}
			}
		}
		time[j]=curr_time;
		
	}
	FILE *P;
	P=fopen("T.txt","w");
	for(x=0;x<T;x++)
		fprintf(P,"Case #%d: %d\n",(x+1),time[x]);
	return 0;
}