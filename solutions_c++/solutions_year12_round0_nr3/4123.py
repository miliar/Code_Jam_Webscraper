#include<vector>
#include<fstream>
#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<math.h>
// #include <cstdlib>

#include<algorithm>
#include<map>
#include<iostream>
using namespace std;
bool inout(int* test, int start,int end,int size,int origin){
	int temp=0;
	for(int i=0;i<size;i++)
	{
		temp=temp+int(test[i]*pow(10.0,i));
	}
	if(temp>=start && temp<=end && temp!=origin)
		return 1;
	else return 0;

}
void int2str(int i, char *s) {
	sprintf(s,"%d",i);
}

int weishu(int q){
	if(q/1000!=0) return 4;
	else if(q/100!=0) return 3;
	else if(q/10!=0) return 2;
	else return 1;
}

int num(int *, int,int,int,int,ofstream &);
int main()
{
	ifstream fin;
	ofstream fout;
	string combinestr;
	fin.open("C-small-attempt6.in");
	fout.open("results.txt");
	int total;
	fin>>total;
	cout<<"Total:"<<total<<endl;
	int start;
	int end;
	int pair=0;
	//test

	//
	for(int i=0;i<total;i++)
	{	
		fin>>start;
		cout<<"start: "<<start<<endl;
		fin>>end;
		cout<<"end: "<<end<<endl;
		int nowei=weishu(start);
		cout<<"DIGITS:"<<nowei<<endl;
		for(int m=start;m<=end;m++)
		{
			int* danteng;
			int* temping;
			danteng=new int[nowei];
			temping=new int[nowei];
			for(int n=0;n<nowei;n++)
			{
				danteng[n]=int(m/pow(10.0,n))%10;
				//cout<<danteng[nowei];
			}

			{
				for(int q=0;q<nowei;q++)
				{
					for(int o=0;o<nowei;o++)
					{
						int move=0;
						move=o+q;
						if(move>nowei-1)
							move=move-nowei;
						temping[o]=danteng[move];

					}
					if(inout(temping,start,end,nowei,m)) {pair++;}
				}

			}
			
		}
		fout<<"Case #"<<i+1<<": "<<pair/2<<endl;
		pair=0;
	}
	
	system("pause");
}

