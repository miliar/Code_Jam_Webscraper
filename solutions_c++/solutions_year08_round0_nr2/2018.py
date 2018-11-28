#include<iostream>
#include<fstream>
#include<stdio.h>
using namespace std;
struct time
	{
	int hour;
	int minute;
	int pos;//1-A 2-B
	};
struct table
	{
	struct time start;
	struct time arrival;
	};
void qsort(int left,int right,struct time num[],int E)
	{
	int pos=(left+right)/2;
	int i=left,j=right;
	struct time p=num[pos],tmp;
	while(i<=j)
		{
		while(num[i].hour<=p.hour)i++;
		while(num[j].hour>=p.hour)j--;
		if(i<=j)
			{
			if(num[i].hour==num[j].hour)
				{
				if(num[i].minute>num[j].minute)
					{tmp=num[i];num[i]=num[j];num[j]=tmp;}
				else if(num[i].minute==num[j].minute)
					{
					if(E==1)
						if(num[i].pos==2)
							{tmp=num[i];num[i]=num[j];num[j]=tmp;}
					if(E==2)
						if(num[i].pos==1)
							{tmp=num[i];num[i]=num[j];num[j]=tmp;}
					}
				}
			else
				{tmp=num[i];num[i]=num[j];num[j]=tmp;}
			i++;j--;
			}
		}
	if(i<right)qsort(i,right,num,E);
	if(j>left)qsort(left,j,num,E);
	}
int qsort2(int n,struct time num[],int E)
	{
	struct time tmp;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
			{
			if(num[i].hour<num[j].hour)
				{tmp=num[i];num[i]=num[j];num[j]=tmp;}
			else if(num[i].hour==num[j].hour)
				{
				if(num[i].minute<num[j].minute)
					{tmp=num[i];num[i]=num[j];num[j]=tmp;}
				else if(num[i].minute==num[j].minute)
					{
					if(E==1)
						if(num[i].pos==2)
							{tmp=num[i];num[i]=num[j];num[j]=tmp;}
					if(E==2)
						if(num[i].pos==1)
							{tmp=num[i];num[i]=num[j];num[j]=tmp;}
					}
				}
			}
	}
int main()
    {
    FILE *fin,*fout;
	fin=fopen("B.in","r");
	fout=fopen("B.out","w");
	int casen;
	fscanf(fin,"%d",&casen);	
	for(int Ci=1;Ci<=casen;Ci++)
		{
		int Ttime;
		struct table At[101],Bt[101];
		fscanf(fin,"%d",&Ttime);
		int An,Bn;
		fscanf(fin,"%d %d",&An,&Bn);
		for(int i=1;i<=An;i++)
			{
			int a,b,c,d;
			fscanf(fin,"%d:%d %d:%d",&a,&b,&c,&d);
			At[i].start.hour=a;
			At[i].start.minute=b;
			At[i].start.pos=1;
			At[i].arrival.hour=c;
			At[i].arrival.minute=d;
			At[i].arrival.pos=1;
			}
		for(int i=1;i<=Bn;i++)
			{
			int a,b,c,d;
			fscanf(fin,"%d:%d %d:%d",&a,&b,&c,&d);
			Bt[i].start.hour=a;
			Bt[i].start.minute=b;
			Bt[i].start.pos=2;
			Bt[i].arrival.hour=c;
			Bt[i].arrival.minute=d;
			Bt[i].arrival.pos=2;
			}
		struct time AnsA[202],AnsB[202];
		for(int i=1;i<=An;i++)
			{
			AnsA[i]=At[i].start;
			AnsB[i]=At[i].arrival;
			AnsB[i].minute+=Ttime;
			if(AnsB[i].minute>=60)
				{AnsB[i].hour+=1;AnsB[i].minute%=60;}
			}
		for(int i=1;i<=Bn;i++)
			{
			AnsB[An+i]=Bt[i].start;
			AnsA[An+i]=Bt[i].arrival;
			AnsA[An+i].minute+=Ttime;
			if(AnsA[An+i].minute>=60)
				{AnsA[An+i].hour+=1;AnsA[An+i].minute%=60;}
			}
		qsort2(An+Bn,AnsA,1);
		qsort2(An+Bn,AnsB,2);
		//for(int i=1;i<=An+Bn;i++)
    	//	cout<<AnsA[i].hour<<":"<<AnsA[i].minute<<" "<<AnsA[i].pos<<endl;
    	//system("pause");
		int Sa,Sb;
		int Pa,Pb;
		Sa=Sb=Pa=Pb=0;
		for(int i=1;i<=An+Bn;i++)
			{
			if(AnsA[i].pos==2)Pa++;
				else if(Pa==0)
					Sa++;
				else Pa--;
			if(AnsB[i].pos==1)Pb++;
				else if(Pb==0)
					Sb++;
				else Pb--;
			}
		fprintf(fout,"Case #%d: %d %d\n",Ci,Sa,Sb);
		}
	//system("pause");
    fclose(fout);
    return 0;
    }
