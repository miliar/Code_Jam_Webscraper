#include <fstream>
#include <algorithm>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

int L, D, N;
vector<string> A;
vector<vector<string> > Ws;
vector<int> counter;

class nod{
public:
	nod* next[26];
	nod() {
		for (int i=0; i<26; i++)
			next[i] = NULL;
	}
};

void build_tree(nod** root, int level, int start, int end) 
{
	if (level>= L) return;

	char previous='0';
	for (int i=start; i<end; i++) {
		char current =A[i][level];
		int new_start;
		int new_end;
		if (current != previous)  { 
			new_start =  i;
			new_end = i;
			while (A[new_end][level]==A[new_start][level]) {
				new_end++;
				if (new_end==end)
					break;
			}

			nod* newnod = new nod;
			(*root)->next[current-'a'] = newnod;
			build_tree(&newnod, level+1, new_start, new_end);

			i = new_end-1;
			previous = current;
		}
	}
}

void search_tree(nod* root, int level, int indx)
{
	if (level>=L) return;

	for (int i=0; i<Ws[indx][level].size(); i++) {
		char c = Ws[indx][level][i];
		if (root->next[c-'a']) {
			if (level==L-1) counter[indx]++; 
			search_tree(root->next[c-'a'], level+1, indx);
		}
	}

}



int main()
{
	string fn;
	fn = "A-large.in";
	ifstream infile;
	infile.open (fn.c_str(), ifstream::in);

	
	vector<string> inputs;

	infile>>L>>D>>N;
	A.resize(D);
	inputs.resize(N);
	string s;
	for (int i=0; i<D; i++)
		infile>>A[i];
	for (int i=0; i<N; i++)
		infile>>inputs[i];

	infile.close();

	sort(A.begin(), A.end());

	Ws.resize(N, vector<string>(L));
	for (int i=0; i<N; i++) {
		int l=0; 
		int pos = 0; 
		while (l<L) {
			int left, right;
			if (inputs[i][pos]!='(') {
				Ws[i][l] = inputs[i][pos];
				pos++;
			}
			else {
				left = inputs[i].find('(', pos);
				if (left<inputs[i].length()) { 
					right = inputs[i].find(')',pos); 
					Ws[i][l] = inputs[i].substr(left+1, right-left-1);
					sort(Ws[i][l].begin(), Ws[i][l].end());
					pos = right+1; 
				}
			}
			l++;
		}
	}

	
	nod* root = new nod;
	build_tree(&root,0, 0, D); 

	counter.resize(N, 0);
	for (int i=0; i<N; i++) 
		search_tree(root, 0, i);

	ofstream outfile;
	outfile.open (fn.append(".out").c_str(), ifstream::out);
	for (int i=0; i<N; i++)
		outfile<<"Case #"<<i+1<<": "<<counter[i]<<endl;
	outfile.close();

	return 0;

}