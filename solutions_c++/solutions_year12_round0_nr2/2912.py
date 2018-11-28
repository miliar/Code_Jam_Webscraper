#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <utility>
#include<map>

using namespace std;

int main(int argc, char **argv) {
	ifstream input (argv[argc-1]);
	char tmap[26];
	string tmp;
	string num;
	string mapinput[3];
	string mapoutput[3];
	int result;
	int input_size;

	if(argc!=2){
		cout << "There is no input file!" << endl;
		return -1;
	}


	input>>tmp;
	input_size=atoi(tmp.c_str());

	for(int i=1; i<=input_size; i++){
		input>>tmp;
		int people_num=atoi(tmp.c_str());
		input>>tmp;
		int sur_num=atoi(tmp.c_str());
		input>>tmp;
		int max_num=atoi(tmp.c_str());
		vector<int> score;

		for(int j=0;j<people_num; j++){
			input>>tmp;
			score.push_back(atoi(tmp.c_str()));
		}

		result=0;

		//cout<<people_num << endl;
		for(int j=0;j<people_num; j++){
			if(score[j]>=max_num*3-2){
				result++;
			}else if(score[j]>=max_num*3-4 && max_num*3-4>=0 && sur_num>0){
				result++;
				sur_num--;
			}
		}

		cout << "Case #" << i << ": " << result << endl;

	}

	return 0;
}