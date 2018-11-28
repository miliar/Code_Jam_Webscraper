#include <fstream>
#include <iostream>
#include <string>
using namespace std;
#define MaxNum 1000
void main()
{
	string   str; 
	int CaseNum;
	int NumEngine[MaxNum];
	int NumQuery[MaxNum];
	int OutPut[20];
	int TestFlag[MaxNum];
	string SearchEngine[MaxNum];
	string Query[MaxNum];
	const char *ch = NULL;
	int flag;
	ifstream infile("A-large.in");
	if (!infile)
	{
		cerr<<"cannot open the input file\n";
		exit(-1);
	}
	getline(infile, str);
	ch = str.c_str();
	CaseNum = atoi(ch);
	//cout<<CaseNum<<endl;
	for (int j=0;j<CaseNum;j++)
	{
		OutPut[j]=0;
	}
	for (int i=0;i<CaseNum;i++)
	{
		getline(infile, str);
		ch = str.c_str();
		NumEngine[i]=atoi(ch);
		//cout<<NumEngine[i]<<endl;
		for (int j=0;j<NumEngine[i];j++)
		{
			getline(infile, SearchEngine[j]);
			//cout<<SearchEngine[j]<<endl;
		}
		getline(infile, str);
		ch = str.c_str();
		NumQuery[i]=atoi(ch);
		//cout<<NumQuery[i]<<endl;
		for (int j=0;j<NumQuery[i];j++)
		{
			getline(infile, Query[j]);
			//cout<<Query[j]<<endl;
		}
		//test swich or not
		for (int j=0;j<NumEngine[i];j++)
		{
			TestFlag[j] = 0;
		}
		flag=0;
		for (int m=0;m<NumQuery[i];m++)
		{
			for (int n=0;n<NumEngine[i];n++)
			{
				if ((Query[m]==SearchEngine[n])&&(TestFlag[n]==0))
				{
					TestFlag[n] = 1;
					flag++;
					n=NumEngine[i];
				}
				else if (Query[m]==SearchEngine[n])
				{
					n=NumEngine[i];
				}
			}
				if (flag >=NumEngine[i])
				{
					flag = 0;
					OutPut[i]++;
					m--;
					for (int j=0;j<NumEngine[i];j++)
					{
						TestFlag[j]=0;
					}
				}
		   }
	}
	infile.close();
	ofstream outfile("Output.out");
	if (!outfile)
	{
		cerr<<"cannot open the output file\n";
		exit(-1);
	}
	for (int i =0;i<CaseNum;i++)
	{
		outfile<<"Case #"<<i+1<<": "<<OutPut[i]<<endl;
	}
}