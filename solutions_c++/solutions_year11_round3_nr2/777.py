#include <cstdio>
#include <iostream>
#include <fstream>
//#include <string>

using namespace std;



int main(int argc, char* argv[])
{
	ifstream fin ("B-small-attempt2.in");
	//ifstream fin ("B-large.in");
    ofstream fout ("B-output-small.txt");
	//ofstream fout ("B-output-large.txt");

	int cases;
	fin >> cases;
	/*{string buffer;
	getline(fin,buffer);} //if needed to read the next lines as lines*/

	for(int i=0; i<cases; i++)
	{
		cout << "Case #"<<(i+1) <<": ";
		fout << "Case #"<<(i+1) <<": ";

		long long int L; //number of boosters
		fin >> L;
		long long int t; //time for booster to be built
		fin >> t;
		long long int N; //stars
		fin >> N;
		long long int C; //
		fin >> C;
		long long int *dist = new long long int[C];

		for(long long int j=0; j<C; j++)
		{
			fin >> dist[j];
		}

		long long int counter = 0;
		//int k = 0;
		bool k = false;
		long long *remaining = new long long int[N];
		
		for(long long int j=0; j<N; j++)
		{
			counter += 2*dist[j%C];
			
			remaining[j] = 0;

			if(counter > t)
			{
				//builds are complete
				if(!k)
				{
					remaining[j] = (counter - t)/2;
					k = true;
				}
				else
				{
					remaining[j] = (dist[j%C]);
				}
			}
		}

		delete[] dist;

		/*if(k<N)
			remaining[k] = -1;*/
		
		long long int time;
		if(counter<t)
			time = counter;
		else
			time = t;

		/*if(remaining[0] != -1)
		{*/
			for(long long int j=0; j<L; j++)
			{
				long long int max = 0;
				long long int pos = -1;
				//for(int k=0; k<N && remaining[k]!=-1; k++)
				for(long long int k=0; k<N; k++)
				{
					if(remaining[k] > max)
					{
						max = remaining[k];
						pos = k;
					}
				}
				if(pos != -1)
				{
					time += remaining[pos];
					remaining[pos] = 0;
				}
			}

			//for(int j=0; j<N && remaining[j]!=-1; j++)
			for(long long int j=0; j<N; j++)
				time += 2*remaining[j];
		//}
		delete [] remaining;

		cout<<time<<endl;
		fout<<time<<endl;
	}
	system("pause");
	return 0;
}