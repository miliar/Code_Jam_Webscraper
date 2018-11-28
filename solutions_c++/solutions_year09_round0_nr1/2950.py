#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

vector<string> words;

int main(){
	int l, d, n;
	cin >> l >> d >> n;
	string temp;
	for(int i=0;i<d;++i){
		cin >> temp;
		words.push_back(temp);
	}
	sort(words.begin(), words.end());
	vector<int> results;
	for(int i=0;i<n;++i){
		set<int> candidates;
		for(int j=0;j<d;++j) candidates.insert(j);
		string input;
		cin >> input;

		for(int j=0, now=0;j<input.size();++j,++now){
			// ()の間は面倒を見る
			if(input[j] == '('){
				set<char> this_can;
				++j;
				while(true){
					if(input[j] == ')') break;
					this_can.insert(input[j++]);
					continue;
				}
				for(set<int>::iterator it = candidates.begin(); it != candidates.end();){
					set<char>::iterator char_it = this_can.find(words[*it][now]);
					if(char_it == this_can.end()) candidates.erase(it++);
					else ++it;
				}
			//それ以外
			}else{
				for(set<int>::iterator it = candidates.begin(); it != candidates.end();){
					if(words[*it][now] != input[j]) candidates.erase(it++);
					else ++it;
				}
			}
		}
		results.push_back(candidates.size());
	}
	for(int i=0;i<n;++i){
		cout << "Case #" << i+1 << ": " << results[i] << endl;
	}

	return 0;
}
