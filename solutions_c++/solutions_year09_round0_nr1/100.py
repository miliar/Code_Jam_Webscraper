#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
using namespace std;

//============================================================
// AlienWords
//============================================================
class AlienWords
{
public:
	AlienWords(const vector<string> &words)
	{
		verts.push_back(vert()); // Root.
		for(int k = 0;k < (int)words.size();++k)
			InsertDictWord(words[k]);
	}

	int Count(string poss);

private:

	// Build a tree of dictionary words.
	// Each edge represents one letter.
	void InsertDictWord(const string &word);
	typedef map<char,int> next_t;
	struct vert{
		vert():count(0),is_word(false){}
		// Count is the number of words we could potentially form with
		// the current prefix string.
		int count;

		bool is_word;

		next_t next; // Edges to children.
	};
	vector<vert> verts;

};
//============================================================

int main()
{
	int L,D,N;
	cin >> L >> D >> N;
	vector<string> words;
	for(int k = 0;k < D;++k){
		string tmp;
		cin >> tmp;
		words.push_back(tmp);
	}
	AlienWords problem(words);
	for(int k = 0;k < N;++k){
		string tmp;
		cin >> tmp;
		cout << "Case #" << k+1 << ": " << problem.Count(tmp) << '\n';
	}
}

//============================================================

void AlienWords::InsertDictWord(const string &word)
{
	int current = 0; // Start at root vert.

	for(string::const_iterator p = word.begin();;++p){

		verts[current].count++;
		if(p == word.end()){
			verts[current].is_word = true;
			break;
		}

		pair<next_t::iterator,bool> f = verts[current].next.insert(make_pair<char,int>(*p,verts.size()));
		if(f.second){
			current = verts.size();
			verts.push_back(vert());
		}else
			current = f.first->second;
	}
}

int AlienWords::Count(string poss)
{
	vector<int> old_verts;
	old_verts.push_back(0); // Root.

	for(int idx = 0;idx < (int)poss.size();++idx) {
		// Get all possible characters.
		vector<char> try_chars;
		if(poss[idx] != '(')
			try_chars.push_back(poss[idx]);
		else
			while(poss[++idx] != ')')
				try_chars.push_back(poss[idx]);

		// Search for new verts
		vector<int> new_verts;

		for(int k = 0;k < (int)old_verts.size();++k){
			//			cerr << "vert = " << old_verts[k] << endl;

			vert &v = verts[old_verts[k]];
			for(int j = 0;j < (int)try_chars.size();++j){
				char ch = try_chars[j];
				//cerr << "ch = " << ch << endl;
				next_t::const_iterator I = v.next.find(ch);
				if(I != v.next.end())
					new_verts.push_back(I->second);
			}
		}

		old_verts = new_verts;
	}

	return old_verts.size();
}
