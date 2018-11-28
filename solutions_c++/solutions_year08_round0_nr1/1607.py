#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main (int argc, char** argv) {
  string line;
  ifstream myfile (argv[1]);
  char outfile[255];
	sprintf(outfile, "%s.out", argv[1]);
  ofstream out ( outfile);
  if (myfile.is_open())
  {
	
      getline (myfile,line);
	int cases_count = atoi(line.c_str());
	for(int i = 0; i < cases_count; i++) {
		int switch_count = 0;
      		getline (myfile,line);
		int names_count = atoi(line.c_str());
		//cout << "name count :" << names_count << endl;
		vector<string> names;
		map<string, int> engine_counts;
		for(int j = 0; j < names_count; j++){
      			getline (myfile,line);
			names.push_back(line);
			engine_counts[line] = 0;
		}
      		getline (myfile,line);
		int querys_count = atoi(line.c_str());
		//cout << "query count :" << querys_count << endl;
		vector<string> querys;
		int counts_remove_repeated = 0;
		string last_line;
		for(int j = 0; j < querys_count; j++){
      			getline (myfile,line);
			if( j > 0 ) {
			if(line != last_line){
			querys.push_back(line);
				counts_remove_repeated++;
			}
			}
			else {
			querys.push_back(line);
			counts_remove_repeated++;
			}
			last_line = line;
		}
		int j = 0;
		//cout << "removed count :" << counts_remove_repeated << endl;
		while( j < counts_remove_repeated ){
			engine_counts[querys[j]] = 1;
			int t = 0;
			for(int k = 0; k < names_count; k++)
				t += engine_counts[names[k]];
			if(t== names_count) {
				switch_count++;
				for(int k = 0; k < names_count; k++)
					engine_counts[names[k]] = 0;
				engine_counts[querys[j]] = 1;
			}
			j++;
		}
		out << "Case #" << i + 1 << ": " << switch_count << endl;	
		
	}
    myfile.close();
    out.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}

