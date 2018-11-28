#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;

int L, D, N;
vector<string> dict;
vector<vector<string> > words;
vector<int> matches;

class NODE{
public:
	NODE* next[26];
	NODE() {
		for (int i=0; i<26; i++)
			next[i] = NULL;
	}
};

void build_tree(NODE** root, int level, int start, int end) 
{
	if (level>= L) return;

	char pre='0'; //non-letter intial value
	for (int i=start; i<end; i++) {
		char cur = dict[i][level];
		int new_start;
		int new_end;
		if (cur != pre)  { //need to modify a child
			new_start =  i;
			new_end = i;
			while (dict[new_end][level]==dict[new_start][level]) {
				new_end++;
				if (new_end==end) //reach the end of the array
					break;
			}

			// insert a new child
			NODE* newnode = new NODE;
			(*root)->next[cur-'a'] = newnode;
			build_tree(&newnode, level+1, new_start, new_end);

			//jump to new_start
			i = new_end-1;
			pre = cur;
		}
	}
}

bool is_next(NODE* root, char c)
{
	if (root->next[c-'a']) 
		return true;
	else 
		return false;
}

void search_tree(NODE* root, int level, int indx)
{
	if (level>=L) return;

	for (int i=0; i<words[indx][level].size(); i++) {
		char c = words[indx][level][i];
		if (is_next(root, c)) {//current level is a match, go to next level
			if (level==L-1) matches[indx]++; //if the current level is the last letter, one match found
			search_tree(root->next[c-'a'], level+1, indx);
		}
	}

}



int main()
{
	string filename;
	//cout<<"Please input the file name of your input (e.g. A-small.in):  "<<endl;
	//cin>>filename;
	filename = "A-large.in";
	//read input
	ifstream infile;
	infile.open (filename.c_str(), ifstream::in);

	
	//vector<string> dict;
	vector<string> testcases;

	infile>>L>>D>>N;
	dict.resize(D);
	testcases.resize(N);
	string s;
	for (int i=0; i<D; i++)
		infile>>dict[i];
	for (int i=0; i<N; i++)
		infile>>testcases[i];

	infile.close();

	//sort dict
	sort(dict.begin(), dict.end());

	//sort words
	//vector<vector<string> > words(N, vector<string>(L));
	words.clear();
	words.resize(N, vector<string>(L));
	for (int i=0; i<N; i++) {
		int l=0; //looking for the l-th sub-string in ()
		int pos = 0; //initial serach pos
		while (l<L) {
			int left, right;
			if (testcases[i][pos]!='(') {
				words[i][l] = testcases[i][pos];
				pos++;
			}
			else {
				left = testcases[i].find('(', pos);
				if (left<testcases[i].length()) { //'(' found
					right = testcases[i].find(')',pos); //assume the input is correct, so right>left and right<L
					words[i][l] = testcases[i].substr(left+1, right-left-1);
					sort(words[i][l].begin(), words[i][l].end());
					pos = right+1; //next time, search '(' from righ+1
				}
			}
			l++;
		}
	}

	
	//construct a search tree
	NODE* root = new NODE;
	build_tree(&root,0, 0, D); 

	// find matches
	//vector<int> matches(N, 0);
	matches.resize(N, 0);
	for (int i=0; i<N; i++) 
		search_tree(root, 0, i);

	//output
	//Case #1: 2
	ofstream outfile;
	outfile.open (filename.append(".out").c_str(), ifstream::out);
	for (int i=0; i<N; i++)
		outfile<<"Case #"<<i+1<<": "<<matches[i]<<endl;
	outfile.close();

	return 0;

}