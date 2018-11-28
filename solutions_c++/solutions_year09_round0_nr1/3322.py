// alienlan.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	
	//a[0][2] = 'a';
	//a[1][3] = 'b';
	int L = 0;
	int D = 0;
	int N = 0;
	cin>>L>>D>>N;
	char** pdic = new char*[D];
	int* pAns = new int[N];
	for (int i = 0;i != N;i++)
	{
		pAns[i] = 0;
	}
	for (int i = 0;i != D;i++)
	{
		pdic[i] = new char[L];
	}
	

	for (int i = 0;i != D ;i++)
	{
		for (int j = 0;j != L;j++)
		{
			cin>>pdic[i][j];
		}
	}
	/////////////
	
	for (int i = 0;i != N ; i++)
	{
		/////////////////
		char letters[100][100];
		for (int j = 0;j != L;j++)
		{
			char a;
			cin>>a;
			if (a == '(')
			{
				cin>>a;
				int numcol = 0;
				while (a != ')')
				{
					
					letters[j][numcol] = a;
					cin>>a;
					numcol++;
				}
				letters[j][numcol] = '0';
			}
			else
			{
				letters[j][0] = a;
				letters[j][1] = '0';
			}
		}

		////////////
		
		int len = 0;
		int firstcol = 0;
		int col = 0;
		while (letters[len][firstcol] != '0')
		{
			for (int n = 0 ;n != D;n++)
			{
				len = 0;
				if (pdic[n][len] == letters[len][firstcol])
				{
					len++;
					col = 0;
					while ( len != L)
					{
						while (letters[len][col] != '0')
						{
							if (pdic[n][len] == letters[len][col])
							{
								len++;
								col = 0;
								if (len == L)
								{
									pAns[i]++;
									len = 0;
									col = 0;
									break;
								}
							}
							else
							{
								col++;
							}
						}
						break;
						
					}
				}
			}
			firstcol++;
			len = 0;
		}
		for (int i = 0;i != L;i++)
		{
			int j = 0;
			while (letters[i][j] != '0')
			{
				cout<<letters[i][j];
				j++;
			}
			cout<<'0'<<endl;
		}
		cout<<endl;

		
		
	}
	for (int i = 0;i != N;i++)
	{
		cout<<"Case #"<<i+1<<": "<<pAns[i]<<endl;
	}

	for (int i = 0;i != D;i++)
	{
		for (int j = 0;j != L;j++)
		{
			cout<<pdic[i][j];
		}
		cout<<endl;
	}
	cout<<endl;
	return 0;
}


