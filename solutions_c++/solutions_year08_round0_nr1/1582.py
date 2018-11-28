#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <sstream>

using namespace std;

ifstream ifs("in.txt");
ofstream ofs("out.txt");

string tmp;

int main()
{
	int N;
	ifs>>N;

	for(int n = 0 ; n < N ; n++){
		int S; ifs>>S; getline(ifs,tmp);
		vector<string> search_engines(S);
		for(int s = 0 ; s < S ; s++)
			getline(ifs,search_engines[s]);

		int Q; ifs>>Q; getline(ifs,tmp);
		vector<string> incoming_queries(Q);
		for(int q = 0 ;q < Q ; q++)
			getline(ifs,incoming_queries[q]);
		
		vector<int> times(S , 0);

		for(int q = Q-1 ; q>=0 ; q--){
			
			for(int s = 0 ; s < S ; s++){
				if ( incoming_queries[q] == search_engines[s] ){

					int min = -1;
					for( int i =0 ; i < S ; i++) if ( i!= s )
						if ( min == -1 || min > times[i])
							min = times[i];
					
					times[s] = min+1;

					break;
				}
			}
		}
		int min = times[0];
		for( int i =1 ; i < S ; i++)
			if (min > times[i]) min = times[i];
		
		ofs<<"Case #"<<n+1<<": "<<min<<endl;





	}


	return 0;
};
