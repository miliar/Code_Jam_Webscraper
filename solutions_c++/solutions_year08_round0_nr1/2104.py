#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <iterator>


using namespace std;

int main(void){
	ifstream fin("A-small.in");
	ofstream fout("A-small.out");
	
	map<string,int> match;
	map<int,int>  res;
	vector<string> querys;
	
	int number = 0;
	int engine_num = 0;
	int query_num = 0;
	string cur;
	
	int switch_num = 0;
	
	getline(fin,cur);
	istringstream stream(cur);
	stream>>number;

	for(int i = 0; i < number ; i++){
		match.clear();
		querys.clear();
		switch_num = 0;
		
		//fin>>engine_num;
		getline(fin,cur);
		istringstream stream1(cur);
		stream1>>engine_num;
		
		for(int j = 0; j < engine_num; j++){
			getline(fin,cur);
			//cout<<cur<<endl;
			match.insert(make_pair(cur,0));
		}

		//fin>>query_num;
		getline(fin,cur);
		istringstream stream2(cur);
		stream2>>query_num;
		
		for(int k = 0; k < query_num; k++){
			getline(fin,cur);
			//cout<<cur<<endl;
			querys.push_back(cur);
		}
		//cout<<match.size()<<" "<<querys.size()<<endl;
		
		
		int mark = 0;
		//cout<<"#############"<<i+1<<"^^^^^^^^^^^^^^^"<<endl;
		for(vector<string>::iterator iter = querys.begin(); iter != querys.end(); iter++){
			if(match[*iter] == 0) {
				//cout<<match[*iter]<<endl;
				match[*iter] = 1;
				mark++;
			} else {
				//cout<<mark<<endl;	
			}
			
			if(mark == engine_num){
				switch_num++;
				
				for(map<string,int>::iterator mit = match.begin(); mit != match.end(); mit++){
					mit->second = 0;
				}
				mark = 1;
				match[*iter] = 1;
			}
		}
		
		res.insert(make_pair(i+1,switch_num));	
	}

	for(map<int,int>::iterator it = res.begin(); it != res.end(); it++){
		fout<<"Case #"<<it->first<<": "<<it->second<<endl;
	}
	
	return 0;
}
