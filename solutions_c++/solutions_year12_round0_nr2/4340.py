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

int num(int *, int,int,int,int,ofstream &);
int main()
{
	ifstream fin;
	ofstream fout;
	string combinestr;
	fin.open("B-small-attempt0.in");
	fout.open("results.txt");
	int total;
	fin>>total;
	for(int i=0;i<total;i++)
	{	int* series;
		int no;
		fin>>no;
		int sur;
		fin>>sur;
		int large;
		fin>>large;
		series=new int[no];
		int more;
		for(int m=0;m<no;m++)
		{
			fin>>series[m];
		}
		more=num(series,sur ,large,no,i,fout);
	}

	system("pause");
}

int num(int *series, int surprise, int large,int size,int i,ofstream &fout)
{
	cout<<"Suprise:"<<surprise<<endl<<"size:"<<size<<endl<<"large:"<<large<<endl;
	int count=0;
	int nSur=0;
	for(int n=0;n<size;n++){
		if(ceil((float)series[n]/3)>=large  && series[n]>1){
			count++;
		}
		if(ceil((float)series[n]/3)==large-1 && series[n]>(large-2)*3+1 && series[n]>1){
			nSur++;
		}
		if(series[n]==0)
		{if(large==0) count++;}
		
		if(series[n]==1)
		{if(large==1) count++;}
	}
	count=count+min(surprise,nSur);
	fout<<"Case #"<<i+1<<": "<<count<<endl;
	return count;
}