//============================================================================
// Name        : alien_numbers.cpp
// Author      : muramasa
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <vector>
#include <numeric>
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <boost/lexical_cast.hpp>
using namespace std;
using boost::lexical_cast;
int main() {
	ifstream ifs("A-small.in");
	ofstream ofs("A-small.out", std::ios::out | std::ios::trunc);
	string buf;
	getline(ifs, buf);
	int cases = lexical_cast<int> (buf);
	cout << cases << endl;
	for (int j = 0; j < cases; j++) {
		getline(ifs, buf);
		//サーチエンジン数
		int engens = lexical_cast<int> (buf);
		cout << engens << endl;
		vector<string> engens_name;
		for (int i = 0; i < engens; i++) {
			getline(ifs, buf);
			engens_name.push_back(buf);
		}
		//キーワード数
		getline(ifs, buf);
		int keywords = lexical_cast<int> (buf);
		cout << keywords << endl;
		vector<int> hits(engens_name.size(),0);
		int count = 0;
		for (int i = 0; i < keywords; i++) {
			getline(ifs, buf);
			for(size_t k=0;k<engens_name.size();++k){
				if(engens_name[k]==buf){
					hits[k]=1;
					bool all_flag=true;
					for(int h_n=0;h_n < hits.size();h_n++){
						if(hits[h_n]==0){
							all_flag=false;
						}
					}
					if(all_flag){
						//もしhitsがぜんぶ１であれば
						count++;
						hits.assign(engens_name.size(),0);
					}
					hits[k]=1;
				}
			}
		}
		cout << "Case #" << j+1 << ": " << count << endl;
		ofs << "Case #" << j+1 << ": " << count << endl;
	}
	//	string n;
	//	ifs >> n;
	//	cout << "number" << n << endl;
	//	size_t case_num = 1;
	//	while( !ifs.eof() ) {
	//		string alien_number,source_language,target_language;
	//	    ifs >> alien_number >> source_language >> target_language;
	//	    cout << alien_number << " " << source_language << " " << target_language << endl;
	//
	//	    size_t src_number_sys = source_language.size();
	//	    size_t trg_number_sys = target_language.size();
	//	    size_t src_digi = alien_number.size();
	//	    //10進数に変換
	//	    int number = 0;
	//	    int digi_cross=1;
	//	    //cout << src_number_sys << " " << trg_number_sys<< " " <<src_digi << endl;
	//	    for(int j=0;j<src_digi;++j){
	//	    	for(int i=0;i<src_number_sys;++i){
	//	    		if(alien_number[src_digi-1-j] == source_language[i]){
	//	    			number += digi_cross * i;
	//	    		}
	//	    	}
	//	    	digi_cross *= src_number_sys;
	//	    }
	//	    vector<size_t> answer_num;
	//	    do{
	//	    	int newstr_num = number%trg_number_sys;
	//	    	number = number/trg_number_sys;
	//	    	answer_num.push_back(newstr_num);
	//	    }while(number>0);
	//
	//	    ofs << "Case #" << case_num << ": ";
	//	    cout << "Case #" << case_num << ": ";
	//	    for(size_t i=0;i<answer_num.size();++i){
	//	    	ofs << target_language[answer_num[answer_num.size()-1-i]];
	//	    	cout << target_language[answer_num[answer_num.size()-1-i]];
	//	    }
	//	    ofs << endl;
	//	    cout << endl;
	//	    ++case_num;
	//	}
	return 0;
}
