#include<vector>
#include<string>
#include<iostream>
#include <stdio.h>
#include <iostream.h>
using namespace std;
int calmoney(int r,int k,int n,int group[]);
void main()
{
	FILE *fp = fopen("C-small-attempt1.in.txt","r");
	FILE *fp2 = fopen("C-small-attempt1.out.txt","w");
//	vector <int> a;
//	vector<int>::iterator   it;
	if(!fp)
	{
		printf("cannot open file\n");
		exit(0);
	}
	int t;
	fscanf(fp,"%d",&t);
	for(int i=1;i<=t;i++)
	{
		int tmp,r,k,n;
		int j = 0;
		int group[1000]={0};
		fscanf(fp,"%d%d%d",&r,&k,&n);
		char c='x';
		while(c!='\n'&&fscanf(fp,"%d%c", &tmp, &c) > 0)
		{
			group[j++] = tmp;
//			printf("%d ",tmp);
//			a.push_back(tmp);
		}
//		printf("\n");
		int money = calmoney(r,k,n,group);
		fprintf(fp2,"Case #%d: %d",i,money);
		if(i!=t)
			fprintf(fp2,"\n");
	}
	fclose(fp);
	fclose(fp2);
}
int calmoney(int r,int k,int n,int group[])
{
	int money = 0,ridenum=0,j=0;
	for(int i=0;i<r;i++)
	{
		int onboat[1000]={0};
		while(1)
		{

//			onboat = j;
			if( (ridenum + group[j]) <= k && onboat[j]==0)
			{
				ridenum += group[j];
				onboat[j] = 1;
				j++;
				if(j == n)
					j = 0;
//				if(j == onboat)
//					break;
			}
			else
			{
				break;
			}
		}
		money += ridenum;
		ridenum = 0;
	}
	return money;
}