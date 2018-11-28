#include<iostream>
#include<fstream>
#include<stdio.h>
using namespace std;

ofstream fout("ans2.txt");
FILE *input = fopen("B-large.in","r");
//ifstream fin("B-small-attempt0.in");

void sort(int a[],int n)
{
	int temp;
	for(int i=0;i<n;i++)
		for(int j=0;j<n-1-i;j++)
			if(a[j] > a[j+1])
			{
				temp = a[j];
				a[j] = a[j+1];
				a[j+1] = temp;
   			}
}

int main()
{
	int cas;
	while(fscanf(input," %d",&cas) != EOF)
	{
		for(int output=1;output<=cas;output++)
		{
			int a,b,turn;
			fscanf(input," %d %d %d",&turn,&a,&b);
			int temph,tempm,rtemph,rtempm,a_leave[a],a_arrive[a],b_leave[b],b_arrive[b];
			for(int i=0;i<a;i++)
			{
				fscanf(input," %d:%d %d:%d",&temph,&tempm,&rtemph,&rtempm);
				a_leave[i] = temph*60+tempm;
    			a_arrive[i] = rtemph*60+rtempm+turn;
			}
			for(int i=0;i<b;i++)
			{
				fscanf(input," %d:%d %d:%d",&temph,&tempm,&rtemph,&rtempm);
				b_leave[i] = temph*60+tempm;
    			b_arrive[i] = rtemph*60+rtempm+turn;
			}
			sort(a_leave,a);
			sort(a_arrive,a);
			sort(b_leave,b);
			sort(b_arrive,b);
			for(int i=0;i<a;i++)
			{
				/*cout<<a_arrive[i][0]<<endl;
				system("pause");*/
				for(int j=0;j<b;j++)
					if(a_arrive[i] <= b_leave[j])
					{
						b_leave[j] = -1;
						break;
     				}
   			}
   			//cout<<output<<"XXX"<<endl;
   			for(int i=0;i<b;i++)
			{
				/*cout<<a_arrive[i][0]<<endl;
				system("pause");*/
				for(int j=0;j<a;j++)
				{
					if(b_arrive[i] <= a_leave[j])
					{
						/*cout<<i<<" "<<j<<" "<<b_arrive[i][0]<<" "<<a_leave[j][0]<<endl;
						system("pause");*/
						a_leave[j] = -1;
						break;
     				}
 				}
   			}
			int countA=0,countB=0;
   			for(int i=0;i<a;i++)
   			{
   				//cout<<a_leave[i][0]<<endl;
   				if(a_leave[i] >= 0)
   					countA++;
			}
			for(int i=0;i<b;i++)
   				if(b_leave[i] >= 0)
   					countB++;
			fout<<"Case #"<<output<<": "<<countA<<" "<<countB<<endl;
		}
 	}
	return 0;
}
