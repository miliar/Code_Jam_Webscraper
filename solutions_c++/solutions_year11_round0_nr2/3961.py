#include "stdafx.h"
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

int T,C,D,N;
vector<char> combine_base1,combine_base2,combine_none_base;
vector<char> oppo_1,oppo_2;
vector<char> result;
vector<string> ans;



char combine(char a, char b)
{
	for (int i = 0 ; i < C ; ++i)
		if ((combine_base1[i] == a && combine_base2[i] == b) || (combine_base1[i] == b  && combine_base2[i] == a))
			return combine_none_base[i];
	return '\0';
}

bool is_opposed(char a, char b)
{
	for (int i = 0 ; i < D ; ++i)
		if ((oppo_1[i] == a && oppo_2[i] == b) || (oppo_1[i] == b && oppo_2[i] == a))
			return true;
	return false;
}


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream input("input.txt");
	ofstream out("out.txt");
	input >> T;
	for (int k = 1; k <= T ; ++k){

		combine_base1.clear();
		combine_base2.clear();
		combine_none_base.clear();
		oppo_1.clear();
		oppo_2.clear();
		result.clear();

		input >> C;
		for (int i = 0 ; i < C ; ++i){		//combine
			char temp;
			input >> temp;
			combine_base1.push_back(temp);
			input >> temp;
			combine_base2.push_back(temp);
			input >> temp;
			combine_none_base.push_back(temp);
		}

		input >> D;
		for (int i = 0 ; i < D ; ++i){
			char temp;
			input >> temp;
			oppo_1.push_back(temp);
			input >> temp;
			oppo_2.push_back(temp);
		}

		input >> N;
		for (int i = 0 ; i < N ; ++i){
			char element;
			input >> element;
			int size = result.size();
		
			//first check combine
			if (size >= 1){
				char last_element = result[size-1];
				char com = combine(last_element,element);
				if (com != '\0'){
					result[size-1]= com;
					continue;
				}
			}

			bool stop = false;
			for (int j = 0 ; j < size ; ++j)
				if (is_opposed(result[j],element)){
					result.clear();
					stop = true;
					break;
				}
			if (!stop)
				result.push_back(element);
		}
		
	/*	string this_ans = "Case #";
		this_ans += char(k+48);
		this_ans += ": [";
		if (result.size() > 0){
			for (int i = 0 ; i < result.size()-1; ++i){
				this_ans += result[i];
				this_ans += ", ";	
			}
			this_ans += result[result.size()-1];
			this_ans += "]";
		}
		else {
				this_ans += "]";
			}
		this_ans += "\n";
		ans.push_back(this_ans);*/
			

	out << "Case #" << k << ": [" ;
		if (result.size() > 0){
			for (int i = 0 ; i < result.size()-1; ++i)
				out << result[i] << ", ";
			out << result[result.size()-1] << "]" << endl;
		}
		else 
			out << "]" << endl;
	}


	return 0;
}

