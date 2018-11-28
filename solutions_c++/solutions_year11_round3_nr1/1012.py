#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
	freopen("outputtttbiggggg.txt","w",stdout);
    
    int T;
    cin>>T;
    int cas=1;
    while (T--)
    {
		int M,N;
		cin>>M>>N;
		vector<string> v(M+2);
		string dummy = "";
		for (int i=0; i<N+2; i++)
			dummy += '.';
		v[0] = dummy;
		v[M+1] = dummy;
		
		for (int i=1; i<M+1; i++)
		{
			cin>>dummy;
			v[i] = ('.' + dummy + '.');
		}
		
		bool IMPOSSIBLE = false;
		for (int row=1; row<M+1; row++)
		{
			if (IMPOSSIBLE)
				break;
			for (int j=1; j<N+1; j++)
			{
				if (v[row][j] == '#')
				{
					if (v[row][j+1] == '#' && v[row+1][j] == '#' && v[row+1][j+1]=='#')
					{
						v[row][j] = '/';
						v[row][j+1] = '\\';
						v[row+1][j] = '\\';
						v[row+1][j+1] = '/';
					}
					else
					{
						IMPOSSIBLE = true;
						break;
					}
				}
			}
		}
		cout<<"Case #"<<cas<<":"<<endl;
		cas++;
		if (IMPOSSIBLE)
		cout<<"Impossible"<<endl;
		else
		{
			for (int i=1; i<M+1; i++)
			{
				for (int j=1; j<N+1; j++)
				{
					cout<<v[i][j];
				}
				cout<<endl;
			}
		}
	}
	return 0;
}
