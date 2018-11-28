// Welcome.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "fstream"
#include "string.h"
#include "iostream"
using namespace std;

#define INFILE "C-large.in"
#define OUTFILE "C-large.out"

char input[1000];
int leninput;
int func[21][502];
char* welcome="welcome to code jam";
int lenwel;

void calFunc()
{
	memset(func,0,sizeof(func));
	for (int j=0; j<=leninput; j++)
		func[0][j]=1;
	//for (int i=0; i<=lenwel; i++)
	//	func[i][0]=0;
	for (int i=1; i<=lenwel; i++)
		for (int j=1; j<=leninput; j++)
		{
			if (welcome[i-1]==input[j-1])
			{
				func[i][j]=func[i-1][j-1]+func[i][j-1];
				func[i][j]=func[i][j]%10000;
			}
			else
			{
				func[i][j]=func[i][j-1];
			}

		}

}

int _tmain(int argc, _TCHAR* argv[])
{
	lenwel=strlen(welcome);
	ifstream infile(INFILE);
	ofstream outfile(OUTFILE);
	int n;
	infile>>n;
	char temp[1];
	infile.getline(temp,1);
	for (int i=0; i<n; i++)
	{
		infile.getline(input,1000);
		leninput=strlen(input);
		calFunc();
		outfile<<"Case #"<<i+1<<": ";
		int zeropad=0;
		if (func[lenwel][leninput]<10)
			zeropad=3;
		else
			if (func[lenwel][leninput]<100)
				zeropad=2;
			else
				if (func[lenwel][leninput]<1000)
					zeropad=1;
		for (int j=0; j<zeropad; j++)
			outfile<<"0";
		outfile<<func[lenwel][leninput]<<endl;
		//for (int j=0; j<=lenwel; j++)
		//{
		//	for (int k=0; k<=leninput; k++)
		//		cout<<func[j][k]<<" ";
		//	cout<<endl;
		//}
		//cout<<"--------"<<endl;
	}
	infile.close();
	outfile.close();
	return 0;
}

