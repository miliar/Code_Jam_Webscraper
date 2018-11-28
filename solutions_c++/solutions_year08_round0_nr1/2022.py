//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused
#include <iostream>
#include <fstream>
#include <map>
#include <sstream>
#include <cmath>

using namespace std;

bool check_for_switch(string& next_query, map<string,bool>& used ){

	bool need_switch = true;

	for( map<string,bool>::iterator it = used.begin(); it != used.end(); it++ ){
		if( it->first != next_query && it->second ==  false )
			return false;
	}
	
	return need_switch;
}

void reset_used(  map<string,bool>& used ){
   	for( map<string,bool>::iterator it = used.begin(); it != used.end(); it++ ){
		it->second = false;
	}
}

int main(int argc, char* argv[])
{
	int N;


	argc--; argv++;

	ifstream in(argv[0]);

	in >> N;



	for( int i = 0; i< N; i++ )	{
		int S;
		int Q;
		int switches = 0;

		map<string,bool> used;

		in >> S;

		for( int j = 0; j < S; j++ ){
			string name;
			do{         
				getline(in,name);
			}while(name == "" );
			used[name] = false;
		}

		in >> Q;
		reset_used(used);
		for( int j = 0; j < Q; j++ ){
			string query;
			do{
				getline(in,query);
			}while(query == "" );



			if( check_for_switch(query, used) ){
				//devo cambiare
				 reset_used(used);
				 switches++;
			}
			used[query] = true;


		}
		cout << "Case #" << i + 1 << ": " << switches << endl;


    }

	in.close();
  
	return 0;
}

//---------------------------------------------------------------------------
