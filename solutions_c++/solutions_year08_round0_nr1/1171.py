#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>

using namespace std;

int anses[1001][100];
int lots = 100000;

vector <string> slis;
int vals[1000];

ofstream fout("output.txt");

int main(void)
{
	int N,S,Q,i,j,k;
	cin >> N;
	string s;
	int ct=0;
	while(N>0)
	{
		memset(anses,0,sizeof(anses));
		N--;
		ct++;
		cin >> S;
		slis.resize(0);
		getline(cin,s);
		for(i=0; i<S; i++)
		{
			getline(cin,s);
			slis.push_back(s);
		}
		cin >> Q;
		getline(cin,s);
		for(i=0; i<Q; i++)
		{
			getline(cin,s);
			for(j=0; j<S; j++)
			{
				if(slis[j]==s)
					break;
			}
			vals[i]=j;
			if(j==S)
			{
				cout << "ERROR 1 " << endl;
			}
		}
		for(i=0; i<Q; i++)
		{
			k=100000;
			for(j=0; j<S; j++)
			{
				if(anses[i][j]<k)
				{
					k=anses[i][j];
				}
			}
			for(j=0; j<S; j++)
			{
				if(j==vals[i])
				{
					anses[i+1][j]=100000;
				}
				else if(k+1 < anses[i][j])
				{
					anses[i+1][j]=k+1;
				}
				else
				{
					anses[i+1][j]=anses[i][j];
				}
			}
		}
		k=100000;
		for(j=0; j<S; j++)
		{
			if(anses[i][j]<k)
			{
				k=anses[i][j];
			}
		}
		cout << "Case #" << ct << ": " << k << endl;
		fout << "Case #" << ct << ": " << k << endl;
	}
	return 0;
}

		