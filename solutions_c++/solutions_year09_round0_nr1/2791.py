// Problem A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "iostream"
#include "fstream"
#include "string"

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	string D[5000],N[500];
	int Count[5000],l,d,n;
	ifstream ifile=ifstream("A-large.in",ios::in);
	ofstream ofile=ofstream("Poblem A",ios::out);
	cout.rdbuf(ofile.rdbuf());
	ifile>>l>>d>>n;
	int i;
	for(i=0;i<d;i++)
	{
		ifile>>D[i];
		Count[i]=0;
	}
	for(i=0;i<n;i++)
	{
		ifile>>N[i];
	}

	for(i=0;i<n;i++)
	{
		int j;
		for(j=0;j<d;j++)
		{
			Count[j]=0;
		}
		for(j=0;j<d;j++)//把D中的每一个与当前的N相比较
		{
			int h=0,k=0;
			for(k=0;k<l;k++)
			{
				if(N[i][h]=='(')
				{
					while(N[i][h]!=')')
					{
						if(D[j][k]==N[i][h])
						{
							Count[j]++;
						}
						h++;
					}
				}
				else
				{
					if(N[i][h]==D[j][k])
					{
						Count[j]++;
					}
					else
						break;
				}
				h++;
			}
		}

		int temp=0;
		for(j=0;j<d;j++)
		{
			if(Count[j]==l)	temp++;
		}
		cout<<"Case #"<<i+1<<": "<<temp<<endl;
	}

	system("pause");
	return 0;
}

