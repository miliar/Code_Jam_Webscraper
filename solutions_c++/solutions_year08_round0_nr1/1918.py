#include <fstream>
#include <string>

using namespace std;

int N; //number of test cases
int S; //number of search engines
string engine[100];
int Q; //number of queries
string query[1000];

int main()
{
	int i, j, k, l;
	int Y;
	bool engineUsed[100];
	int tracker;
	string temp;
//	ifstream input_file("A-small.in");
	ifstream input_file("A-large.in");
//	ofstream output_file("A-small.out");
    ofstream output_file("A-large.out");
	input_file>>N;
	for (i = 1; i<=N; i++)
	{
		Y = 0;
		input_file>>S;
	    getline( input_file, temp ); //read /n
		for (j = 0;j<S;j++)
		{
			getline( input_file, engine[j] );
			engineUsed[j] = false;
		}
		input_file>>Q;
	    getline( input_file, temp ); //read /n
		for (j = 0;j<Q;j++)
		{
			getline( input_file, query[j]);
		}
		tracker = S;
		for (j = 0;j<Q;j++) //cal
		{
//			output_file<<"query: "<<query[j]<<endl;
			for (k = 0;k<S;k++)
			{
				if ( ( query[j] == engine[k] ) && ( engineUsed[k] == false) )
				{
					if ( tracker >1 )
					{
					    engineUsed[k] = true;
					    tracker--;
//					    output_file<<"step: "<<j<<" same: "<<engine[k]<<endl;
//						output_file<<"tracker: "<<tracker<<endl;
					}
					else//tracker = 1; we have to save the universe!
					{
						Y++; //switch
						tracker = S-1;
						for (l=0;l<S;l++)
							engineUsed[l] = false;
						engineUsed[k] = true;
//						output_file<<"step: "<<j<<" switch from: "<<engine[k]<<endl;
						break;
					}
				}
			}
		} //end cal
		output_file<<"Case #"<<i<<": "<<Y<<endl;
	}
	return 0;
}
