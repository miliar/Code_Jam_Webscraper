#include <iostream>
#include <string>
#include <cstdlib>
#include <map>
#include <bitset>

using namespace std;

class SearchEngine
{
	int N; // number of test cases
	int S; // number of search engines
	int Q; // number of incoming queries

	map<string,int> enginenum;
	bool *bitvector;
	int falsecount;
	int switchcount;

	string query;
	int egnum;

	public:



	void take_input()
	{
		// read number of test cases 
		cin >> N;
		for ( int n = 0 ; n < N ; n++) // for each test case
		{

			//cout << endl << "n:: " << n << endl;

			switchcount = 0;
			// read number of search engines
			cin >> S;
			int ch = getchar();
			ch = '\0';
			//cout << endl << "Engines ::" << endl;

			bitvector = new bool[S];

			for ( int s = 0 ; s < S ; s++) // for each search engine
			{
				// read name and encode
				string engine="";
				getline(cin,engine);
//				for ( unsigned int i = 0 ; i < engine.length() ; i++)
//				{
//					if ( engine[i] == ' ' )
//					{
//						engine[i] = 'Z';
//					}
//				}

				//enginenum.insert(make_pair(engine,s));
				enginenum[engine] = s ;
				bitvector[s] = true;
				//cout << engine.c_str() << " -> " << s << endl;
			} // end of s loop

			falsecount = 0;

			// read number of queries
			cin >> Q;
			ch = getchar();
			ch = '\0';
			//cout << "Queries :: " << endl;
			for ( int q = 0 ; q < Q ; q++ )
			{
				// read query 
				query = "";
				getline(cin,query);
//				for ( unsigned int i = 0 ; i < query.length() ; i++)
//				{
//					if ( query[i] == ' ' )
//					{
//						query[i] = 'Z';
//					}
//				}

				// cout << "----------------------------------" << endl;
				// cout << query.c_str() << " : " ;
				// cout << enginenum[query] << endl;
				egnum = -99;
				egnum = enginenum[query];

				if ( bitvector[egnum] == true ) // We are changing bit from true to false
				{
					falsecount++;
					bitvector[egnum] = false;
				}

				//dump_vector();
				// cout << "FalseCount ::" << falsecount << endl;

				if ( falsecount == S ) // all false
				{
					// Switch at this point
					switchcount++;

					// Back to postion
					for ( int s = 0 ; s < S ; s++ )
					{
						bitvector[s] = true;
					}
					falsecount = 1;
					bitvector[egnum] = false;
                    

				}


			} // end of q loop

			cout << "Case #" << n+1 << ": " << switchcount << endl;

			delete bitvector;


		}

	}

	void dump_vector()
	{

		cout << endl;	
		for ( int i = 0 ; i < S ; i++ )
		{
			cout << bitvector[i] << " ";
		}
		cout << endl;	

	}

};


int main(int argc,char *argv[])
{

	SearchEngine s;
	s.take_input();


	return 0;

}
