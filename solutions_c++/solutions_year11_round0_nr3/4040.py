#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<fstream>
#include<stdint.h>

using namespace std;
uint64_t match(vector<uint64_t>,vector<uint64_t>);
int main(int argc,char *argv[]) {


	if(argc != 2)
		return 0;
	string cases;
	int casenum;
	ifstream ifs(argv[1]);
	vector<string> full_seq;
	if(ifs.is_open()) {
		while(ifs.good()) {     
			string input;
			getline(ifs,input);
			full_seq.push_back(input);
		}
		ifs.close();  
	}

	casenum = atoi(&(full_seq[0].at(0)));
	int itr = 0; 
	while(itr < (2 * casenum)) {
		int pilenumber = atoi(&(full_seq[itr + 1].at(0)));
		vector<uint64_t> totalpile;
		totalpile.push_back(atoi(&full_seq[itr + 2].at(0))); 
		size_t space = full_seq[itr+2].find(" ",0); 
		while(space != string::npos) {
			int num_pos = int(space) + 1; 
			totalpile.push_back(atoi(&full_seq[itr+2].at(num_pos)));
			space = full_seq[itr+2].find(" ",num_pos);  
		}
                
		uint64_t max_val = 0;
		for(int i=0;i<pilenumber;i++) {
			vector<uint64_t> duplicate = totalpile;
			vector<uint64_t> check;
			check.push_back(duplicate[i]);
			duplicate.erase(duplicate.begin() + i);
			uint64_t inter = match(duplicate,check); 
			if(inter > max_val)
				max_val = inter;
			while(!duplicate.empty()) {
				for(int l=0;l<duplicate.size();l++) {
					vector<uint64_t> check_sub = check;
					vector<uint64_t> duplicate_sub = duplicate;
					check_sub.push_back(duplicate_sub[l]);
					duplicate_sub.erase(duplicate_sub.begin() +l); 
					if(!duplicate_sub.empty() && !check_sub.empty()) { 
						inter = match(duplicate_sub,check_sub);    
						if(inter > max_val)
							max_val = inter;
					}   

				}
				check.push_back(duplicate[0]);
				duplicate.erase(duplicate.begin());
				//inter = match(duplicate,check);
				//if(inter > max_val)
				//max_val = inter;

			}

		}

		itr += 2;
		if(max_val == 0)
			cout<<"Case #"<<itr/2<<": NO"<<endl;
		else
			cout<<"Case #"<<itr/2<<": "<<max_val<<endl;      

	}

	return 0; 
}

uint64_t match(vector<uint64_t> duplicate,vector<uint64_t> check) {
	uint64_t real_sum=0,dummy_sum=0,check_sum_real=0,check_sum_dummy=0;
	for(vector<uint64_t>::iterator r = duplicate.begin(); r < duplicate.end();r++) {
		real_sum += (*r);
		dummy_sum ^= (*r);  
	}
	for(vector<uint64_t>::iterator r = check.begin();r < check.end();r++) {
		check_sum_real += (*r);
		check_sum_dummy ^= (*r);  

	}
	if(dummy_sum == check_sum_dummy) {
                
		if(real_sum > check_sum_real)
			return real_sum;
		else
			return check_sum_real;
	}

	else
		return 0;  

}
