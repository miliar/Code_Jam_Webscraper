#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <string>

using namespace std;

#define ALL(container) (container).begin(),(container).end()
#define REP(i,N) for (int i=0; i<(N); ++i)
#define FOR(i,i_begin,i_end) for (int i=(i_begin); i<=(i_end); ++i)
#define FORD(i,i_begin,i_end) for (int i=(i_begin); i>=(i_end); --i)
#define FOREACH(it, container) for(__typeof((container).begin()) it = (container).begin(); it != (container).end(); ++it)
#define clearStream(_stream_, _str_) getline((_stream_),(_str_))

int main(){

	ifstream inf("A-large.in");
	ofstream outf("A-large.out");
	
	
	int NumberOfCase = 0;
	inf >> NumberOfCase;
	
	REP(i, NumberOfCase){
		vector<string> searchName;
		vector<bool> flag;
		int NumberOfSearch = 0;
		inf >> NumberOfSearch;
		int flag_count=0, result_count=0;
		string clear_str="";
		clearStream(inf, clear_str);

		REP( j, NumberOfSearch){
			
			string inputLine; getline(inf, inputLine);
			searchName.push_back(inputLine);
			flag.push_back(false);
		}
		int NumberOfQuery = 0;
		inf >> NumberOfQuery;


	 	clearStream(inf, clear_str);
		int beforeIter = -1, beforetmp = -1;
		REP( j, NumberOfQuery){
			
			string input_query; getline(inf, input_query);
						
			bool flag_check = false;
			REP( k, searchName.size()){
				if(searchName[k] == input_query){
					beforetmp = k;
					if(flag[k] == true){
						
						
						break;
					}
					else{
						flag[k] = true;
						flag_check = true;
						break;
					}
				}
			}
			if( flag_check ){
				flag_count++;
				if(flag_count >= searchName.size()){
					result_count++;
					flag_count = 0;
					beforeIter = beforetmp;
					REP( k, flag.size()){
						flag[k] = false;
					}
				}
				else if(beforeIter >= 0){
					if( flag[beforeIter] == false && flag_count >= searchName.size()-1){
						result_count++;
						flag_count = 0;
						beforeIter = beforetmp;
						REP( k, flag.size()){
							flag[k] = false;
						}
					}
				}
			}

		}
		outf << "Case #" << i + 1 << ": " << result_count << endl;
		
		
	}

	outf.close();
	inf.close();
	return 0;
}