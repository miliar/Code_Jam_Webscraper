#include<vector>
#include<iostream>
#include<fstream>
#include<set>
#include<map>
#include<iomanip>
#include<algorithm>
#include<stdio.h>

using namespace std;

struct charpair
{
	char first, last;
};

double getAnswer(vector<int> &A)
{
	vector<int>_A=A;
	sort(_A.begin(), _A.end());
	vector<int> correct, reverse, others;
	for(size_t i=0;i<A.size();i++){
		int pos, left=0, right=A.size();
		while(left<right){
			pos = (right+left)/2;
			if(_A[pos] < A[i])
				left = pos;
			else if(A[i] < _A[pos])
				right = pos;
			else
				break;
		}
		if(pos == i)
			correct.push_back(A[i]);
		else if(_A[i] == A[pos])
			reverse.push_back(A[i]);
		else
			others.push_back(A[i]);
	}
	double x = 0;
	x += (reverse.size() / 2) * 2.0;
	if(others.size() > 1)
		x += (others.size()-1) * 2.0;
	return x;
}

vector<char> invoke(map<pair<char,char>, char> &combiner, set<pair<char,char>> &eraser, vector<char> &elements)
{
	vector<char> result;
//	multiset<char> chars;
	for(size_t i=0; i<elements.size(); i++){
		result.push_back(elements[i]);
//		chars.insert(elements[i]);
		if(result.size() > 1){
			if(combiner.find(make_pair(result[result.size()-2],result.back())) != combiner.end()){
				char c1 = result[result.size()-2], c2 = result.back();
//				chars.erase(c1);
//				chars.erase(c2);
//				chars.insert(combiner[make_pair(c1, c2)]);
				result.pop_back();
				result.pop_back();
				result.push_back(combiner[make_pair(c1, c2)]);
			}
			else{
				set<char> chars;
				for(size_t j=0;j<result.size();j++)
					if(chars.count(result[j]) == 0)
						chars.insert(result[j]);
				for(set<pair<char,char>>::iterator j=eraser.begin(); j!=eraser.end();++j){
					if(chars.count(j->first)>0 && chars.count(j->second) > 0){
						result.clear();
//						chars.clear();
						break;
					}
				}
			}
		}
	}

	return result;
}

int main(int argc, char *argv[])
{
	ifstream ifs(argv[1]);
	int T;
	ifs >> T;
	for(int i=0;i<T;i++){
		int C;
		ifs >> C;
		map<pair<char,char>, char> combiner;
		for(int j=0; j<C; j++){
			pair<char,char> temp;
			char result;
			ifs >> temp.first;
			ifs >> temp.second;
			ifs >> result;
			combiner[temp] = result;
			swap(temp.first, temp.second);
			combiner[temp] = result;
		}

		int D;
		ifs >> D;
		set<pair<char,char>> eraser;
		for(int j=0; j<D; j++){
			pair<char,char> temp;
			ifs >> temp.first;
			ifs >> temp.second;
			eraser.insert(temp);
		}

		int N;
		ifs >> N;
		vector<char> elements(N);
		for(int j=0; j<N; j++)
			ifs >> elements[j];

		cout << "Case #" << i+1 << ": [";
		vector<char> result = invoke(combiner, eraser, elements);
		for(size_t j=0; j<result.size(); j++){
			cout << result[j];
			if(j < result.size() - 1)
				cout << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}