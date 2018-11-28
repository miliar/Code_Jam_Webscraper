#include "iostream"
#include "cstdlib"
#include "string"
#include "stdio.h"

using namespace std;

int main(int argc, char * argv[]) {

	if(argc != 2) {
		cout << "usage: program_name input_file" << endl;
		exit(1);
	}
	
	FILE * fp = fopen(argv[1],"r");
	if(!fp) {
		cout << "input file " << argv[1] << " not exists" << endl;
		exit(2);
	}
	
	int num_testcase, num_engine, num_search;
	char buffer[256];
	char engine[100][256];
	int search[1000];
	fgets(buffer, 256, fp);
	sscanf(buffer,"%d",&num_testcase); // 1st line
	//cout << "num_testcase: " << num_testcase << endl;
	for(int i = 0; i < num_testcase; i++) {
		fgets(buffer, 256, fp);
		sscanf(buffer,"%d",&num_engine); // 2nd line
		//cout << "num_engine: " << num_engine << endl;
		for(int j = 0; j < num_engine; j++) {
			fgets(engine[j], 256, fp);
			//*strchr(engine[j],'\n') = '\0';
			//cout << "engine[j]: " << engine[j] << endl;
		}
		fgets(buffer, 256, fp);
		sscanf(buffer,"%d",&num_search); // 3rd section
		//cout << "num_search: " << num_search << endl;
		for(int j = 0; j < num_search; j++) {
			fgets(buffer, 256, fp);
			//*strchr(buffer,'\n') = '\0';
			//cout << "buffer: " << buffer << endl;
			for(int k = 0; k < num_engine; k++) {
				if(strcmp(buffer,engine[k]) == 0) {
					search[j] = k;
					//cout << "search[j]: " << search[j] << endl;
				}
			}
		}
	
		bool visited[100];
		for(int ii = 0; ii < num_engine; ii++) {
			visited[ii] = false;
		}
		int num_switch = 0;
		for(int ii = 0; ii < num_search; ii++) {
			visited[search[ii]] = true;
			bool allvisited = true;
			for(int j = 0; j < num_engine; j++) {
				if(visited[j] == false) allvisited = false;
			}
			if(allvisited) {
				num_switch++;
				for(int j = 0; j < num_engine; j++) {
					visited[j] = false;
				}
				visited[search[ii]] = true;
			}
		}
		
		cout << "Case #" << (i+1) << ": " << num_switch << endl;
	}
	
	return 0;
	
}
