#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int L,D,N;
vector<string> words;
vector<string> tests;

int input_read(char * filename)
{
	ifstream ifs;
	ifs.open(filename, ios::in); // “Ç‚ÝŽæ‚èê—p‚ÅŠJ‚­
    
	while( !ifs.eof() ){

        ifs >> L >> D >> N;
		vector<char> buf(1000);

		words.reserve(D);
		for(int i = 0; i < D; ++i){
			ifs >> &buf[0];
			words.push_back(&buf[0]);
		}

		tests.reserve(N);
		for(int i = 0; i < N; ++i){
			ifs >> &buf[0];
			tests.push_back(&buf[0]);
		}
		return 0;
    }
	return -1;
}

void printlist(vector<string> &t){
	typedef vector<string> T;
	for(T::iterator i = t.begin(), e = t.end(); i != e; ++i){
		cout << *i << endl;
	}
}

struct dic_node{
	char letter;
	vector<dic_node> nexts;

	bool operator==(const dic_node &d){
		return (this->letter == d.letter);
	}
	dic_node():letter('@'), nexts(){}
	dic_node(char c):letter(c), nexts(0){}
};

int create_dict(dic_node &root)
{
	for(vector<string>::iterator i = words.begin(), e = words.end(); i != e; ++i){
		dic_node *focus = &root;
		string &w = (*i);
		for(int j = 0, len = w.length(); j < len; ++j){
			vector<dic_node> &n = focus->nexts;
			vector<dic_node>::iterator found = find(n.begin(), n.end(), dic_node(w[j]));
			if(found == n.end()){
				dic_node d(w[j]);
				n.push_back(d);
				focus = &*(n.end()-1);
			}
			else
			{
				focus = &*found;
			}
		}
	}
	return 0;
}

void print_dict(dic_node &root)
{
	cout << root.letter << "[";
	vector<dic_node> &n = root.nexts;
	for(vector<dic_node>::iterator i = n.begin(), e = n.end(); i != e; ++i){
		print_dict(*i);
	}
	cout << "]";
}

void parse(string &test, vector<string> &out)
{
	char cset[1000];
	for(int i = 0, len = test.length(); i < len; ++i){
		if(test[i] == '('){
			char *p=cset;
			++i;
			while(test[i] != ')'){
				*p = test[i];
				++p;
				++i;
			}
			*p='\0';
		}else{
			cset[0] = test[i];
			cset[1] = '\0';
		}
		out.push_back(cset);
	}
}

void count_pattern_sub(dic_node &root, vector<string> parsed, int &cand_count)
{
	if(parsed.empty()){++cand_count;return;}

	vector<dic_node> &n = root.nexts;
	for(int i = 0, len = parsed[0].length(); i < len; ++i){
		vector<dic_node>::iterator found = find(n.begin(), n.end(), dic_node(parsed[0][i]));
		if(found != n.end()){
			count_pattern_sub(*found, vector<string>(parsed.begin()+1,parsed.end()), cand_count);
		}
	}
}

int count_pattern(dic_node &root, string &test)
{
	vector<string> parsed;
	parse(test, parsed);
	int cand_count=0;
	count_pattern_sub(root,parsed,cand_count);
	return cand_count;
}

int main(){
	input_read("J:\\A-large.in");

//	cout << "L" << L << " D" << D << " N" << N << endl;
//	printlist(words);
//	printlist(tests);

	dic_node root;
	create_dict(root);

//	print_dict(root);

	ofstream o("J:\\A_large_ans");

	int n = 0;
	for(vector<string>::iterator i = tests.begin(), e = tests.end(); i != e; ++i){
		o << "Case #" << ++n << ": " <<
		count_pattern(root, *i)
		<< endl;
	}
}
