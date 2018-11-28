#include "common.h"
using namespace std;


struct point
{
	int a,b;
};
bool mycompare (point i,point j) { return (i.a<j.a); }

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


	/*************************************************************************/

	fin>>cases;
	fin.get();
	
	for(int itr=0 ; itr < cases; itr++ )
	{
		int N;
		fin>>N;
		vector <point> wire;
		wire.resize(N);
		for(int i=0; i<N; i++)
		{
			fin>>wire[i].a>>wire[i].b;
		}
		sort(wire.begin(), wire.end(), mycompare);
		int itx = 0;
		for(int it = 0; it < N; it++)
		{
			for(int idx = it; idx < N; idx++)
			{
				if(wire[idx].b < wire[it].b )
					itx++;
			}
		}
		fout<<"Case #"<<itr+1<<": ";                       
		//output     
		fout<<itx;
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