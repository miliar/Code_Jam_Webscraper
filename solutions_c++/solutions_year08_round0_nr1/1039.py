#include<iostream>
#include<string>
#include<fstream>
	using namespace std;


	string engines[101];
	string queries[1001];
	int enginesTemp[288];
	int caseCnt;
	int engineCnt;
	int queryCnt;
		
int checkEngine(string str)
{
	int i;
	for(i=0;i<engineCnt;i++)
		if(engines[i]==str) return i;
	return -1;
}

int choose()
{
	for(int jj=0;jj<engineCnt;jj++)enginesTemp[jj]=0;
	int ss=0;
	int cho=0;
	int ocurengine=0;
	while(ss<queryCnt)
	{
		int fla=checkEngine(queries[ss]);
		if(-1==fla)
		{
			ss++;
		}
		else
		{
			if(0==enginesTemp[fla])
			{
				enginesTemp[fla]++;
				ocurengine++;
				if(ocurengine==engineCnt)
				{
					cho++;
					for(int jj=0;jj<engineCnt;jj++)enginesTemp[jj]=0;
					enginesTemp[fla]++;
					ocurengine=1;
					continue;
				}
				else ss++;
				
			}
			else ss++;
		}
	}
	return cho;
}
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("A-large.out");
	
	
	fin>>caseCnt;
	
	int i;
	
	int choice=0;
	for(i=0;i<caseCnt;i++)
	{
	
		fin>>engineCnt;
		int j;
		string temp;
		getline(fin,temp);
		for(j=0;j<engineCnt;j++)
		{
			getline(fin,engines[j]);
		}

		fin>>queryCnt;
		
		int k;
		getline(fin,temp);
		for(k=0;k<queryCnt;k++)
		{
			getline(fin,queries[k]) ;
		}
		
		choice=choose();
		fout<<"Case #"<<(i+1)<<": "<<choice<<endl;

	}
	fin.close();
	fout.close();

	return 0;
}

