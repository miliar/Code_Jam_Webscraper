#include <iostream>
#include <fstream>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath> 

#define fill_(x,v) memset(x,v,sizeof(x))
#define for_(i,a,b) for (__typeof(b) i=(a); i<(b); i++)
#define min(x,y) (((x)>(y)) ? (y) :(x))
#define max(x,y) (((y)>(x)) ? (y) :(x)) 


using namespace std;
	int N;
bool checkF(vector<string> nm, char c, int K)
{

	int i,j;
	bool blue = false;
		for ( i = 0; i < N && !blue; i++)
		{
			int num = 0;
			for ( j = 0; j < N; j++)
				if (nm[i][j] == c)
				{ 
					num ++;
					if (num == K) blue = true;
				}
				else num = 0;
				
		}
		
		for ( i = 0; i < N && !blue; i++)
		{
			int num = 0;
			for ( j = 0; j < N; j++)
				if (nm[j][i] == c)
				{
					num ++;
					if (num == K) blue = true;
				}
				else num = 0;
				
		}

		for ( i = 0; i < N && !blue; i++)
		{
			int ii = i; 
			int jj = 0;
			int num = 0;
			for (; ii < N && jj < N && !blue; ii++, jj++)
			{
				
				if (nm[jj][ii] == c)
				{
				
					num ++;
					if (num == K) blue = true;
				}
				else num = 0;
			}

		}
		

		for ( i = 0; i < N && !blue; i++)
		{
			int ii = i; 
			int jj = 0;
			int num = 0;
			for (; ii >= 0 && jj < N && !blue; ii--, jj++)
				if (nm[jj][ii] == c)
				{
					num ++;
					if (num == K) blue = true;
				}
				else num = 0;

		}

		for ( i = 0; i < N && !blue; i++)
		{
			int ii = i; 
			int jj = N - 1;
			int num = 0;
			for (; ii < N && jj >= 0 && !blue; ii++, jj--)
				if (nm[jj][ii] == c)
				{
					num ++;
					if (num == K) blue = true;
				}
				else num = 0;
		}

		
		for ( i = 0; i < N && !blue; i++)
		{
			int ii = i;  
			int jj = N - 1;
			int num = 0;
			for (; ii >= 0 && jj >= 0 && !blue; ii--, jj--)
				if (nm[jj][ii] == c)
				{
					num ++;
					if (num == K) blue = true;
				}
				else num = 0;
		}
		return blue;

}
void main()
{

	ifstream inp("e:\\A-large.in");
	ofstream out("e:\\output.txt");
	int NN;
	inp>> NN;
	int i,j;
	for (int nn = 1; nn <= NN; nn++)
	{
cout<<nn<<endl;
		int K;
		inp >> N >> K;
		vector<string> m, nm;
		for ( i = 0; i < N; i++)
		{
			string s;
			m.push_back(s);
	
		}
		
		for ( i = 0; i < N; i++)
		{
			string s;
			inp >> s;
			nm.push_back(s);
			m[ N - 1 - i ] = s;
		}

		// rotate;
		for ( i = 0; i < N; i++)
		for ( j = 0; j < N; j ++)
		{
			nm[i][j] = m[j][N - 1 -i];
		}

		
		for ( i = 0; i < N; i ++)  
		{
			j = 0;
			while ( j < N &&nm[j][i] !='.')
			{j++;
			}
		
			int k;
			for ( k = j + 1; k < N; k++)
				if ( nm[k][i] != '.')
				{
					
					nm[j][i] = nm[k][i];
					nm[k][i] ='.';
					j++;
				}
		}
	
		bool blue = checkF(nm,'B',K);
		bool red = checkF(nm,'R',K);
		string res;
		if ( !blue&&!red) res ="Neither";
		if (blue&&red) res ="Both";
		if (blue &&!red) res ="Blue";
		if (!blue && red) res ="Red";



		out<<"Case #"<<nn<<": "<< res<<endl;
	}// end of nn

}