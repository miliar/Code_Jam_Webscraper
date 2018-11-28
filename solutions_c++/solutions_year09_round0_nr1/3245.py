#include<iostream>
#include<fstream>
#include<set>
#include<string>
#include<vector>

using namespace std;

vector<string> get_words(string Case);
int check(const string& s);

	set<string> vocab;

int main(){

	int L, D, N;

	cin >> L;
	cin >> D;
	cin >> N;


	string word;
	for(int i = 0; i < D; i++){
		cin >> word;
		vocab.insert(word);
	}


	for(int j = 0; j < N; j++){
		string Case;
		cin >>  Case;
		vector<string> comb = get_words(Case);
		//cout <<  Case << " " << comb.size() << endl;
		int valid = 0;
		for(int k = 0; k < comb.size(); k++) {
		//	cout << comb[k] << " " ;
			if(vocab.count(comb[k]) != 0) {
			//cout << comb[k] << " " ;
				valid++;
			}
		}
		cout << "Case #" << (j+1) << ": " << valid << endl;
	}
}


vector<string> get_words(string Case){

	//cout << "Case: " << Case << endl;

	vector<string> combinations;
	if(Case.size() == 0){
		string w;
		combinations.push_back(w);
		//cout << "Case2: " << Case << endl;
		return combinations;
	}

	if(Case[0] != '('){
		vector<string> post = get_words(Case.substr(1, Case.size() - 1));
		//cout << "Case3: " << Case << endl;
		for(int i = 0; i < post.size(); i++) {
			if(check(post[i]) != 1)
				continue;
//			cout << post[i] << " " << check(post[i]) << endl;
			char t[2];
		       	t[0] = Case[0];
		       	t[1] = 0;
			string w(t);
//			cout << "Case4: " << Case <<  ":" << w.append(post[i]) << endl;
			combinations.push_back(w.append(post[i]));
		}
		return combinations;
	}

	int term = Case.find_first_of(')');
	vector<string> post = get_words(Case.substr(term + 1, Case.size() - (term +1)));
	for(int i = 0; i < post.size(); i++){
		if(check(post[i]) != 1)
			continue;
	//	cout <<  post[i] << " " << check(post[i]) << endl;
		for(int j = 1; j < term ; j++){
			char t[2];
		       	t[0] = Case[j];
			t[1] = 0;
			string w(t);
			//cout << post[i] << " " << w.append(post[i]) << endl;
			//cout << "Case4: " << Case <<  ":" << w.append(post[i]) << endl;
			combinations.push_back(w.append(post [i]) );
//			cout << "RESULT : "<< " " << w << endl;
		}
	}
	return combinations;
}

int check(const string& s){
	if(s.size() == 0)
		return 1;
	set<string>::iterator iter;
	iter = vocab.begin();
	while(iter != vocab.end()){
		//cout << *iter << " " << s <<  " " << (*iter).rfind(s)<< endl;
		if((*iter).rfind(s) == (*iter).size() -1 - s.size() + 1)
			return 1;
		iter++;
	}
	return 0;
}
