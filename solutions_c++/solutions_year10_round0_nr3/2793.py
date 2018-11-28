#include "common.h"
using namespace std;

int main() 
{
	ifstream fin;
	ofstream fout;

	fin.open(IN_PATH,ios::in);
	if(!fin)
	{
		cout<<"Failed to open input file!! ";
		cin.get();
		return 0;
	}

	fout.open(OUT_PATH);
	if(!fout)
	{
		cout<<"Failed to open output file!! ";
		cin.get();
		return 0;
	}


	/*************************************************************************/
	/* Variable declarations */
	__int64 cases;
	__int64 R, k, N;
	queue <__int64> g;

	/*************************************************************************/

	fin>>cases;
	fin.get();
	
	for(int itr=0 ; itr < cases; itr++ )
	{
		fin>>R>>k>>N;

		while(!g.empty())
		{
			g.pop();
		}

		for(int i = 0; i<N; i++)
		{
			__int64 temp;
			fin>>temp;
			g.push(temp);
		}
		__int64 cost = 0;
		for (int i=0; i<R; i++)
		{	
			__int64 seats = k;
			for(int j = 0; j < N && (seats >= g.front()); j++)
			{
				__int64 temp = g.front();
				seats -= temp;
				cost += temp;
				g.push(temp);
				g.pop();
			}
		}
		fout<<"Case #"<<itr+1<<": ";                       
		//output         
		fout<<cost;
		fout<<"\n";
	}
	fin.close();
	fout.close();

	/*************************************************************************/
	/* Saving the output */
	cout<<"Saved the solution, press a key to quit..";
	cin.get();
	/*************************************************************************/
	return 0;
} 