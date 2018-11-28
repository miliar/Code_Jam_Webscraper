#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int main() {
	int case_num, L, D;
	scanf("%d %d %d\n", &L, &D, &case_num);
	
	vector<string> dictionary;
	char d[20];
	for (int i = 0; i < D; i++)
	{
		scanf("%s\n", d);
		dictionary.push_back(d);
	}

	char p_buffer[2000];
	for (int cas = 0; cas < case_num; cas++)
	{
		vector<string> dd(dictionary);
		scanf("%s\n", p_buffer);
		string pattern(p_buffer);
		int pattern_size = pattern.size();
		
		string choices;
		bool c = false;

		int search_index = 0;
		for (int i = 0; i < pattern_size; i++)
		{
			if (dd.size() == 0){
				break;
			}

			char letter = pattern[i];
			
			if (letter == '(') {
				c = true;
				continue;
			}
			
			if (letter == ')') {
				for(vector<string>::iterator word = dd.begin(); word != dd.end(); ) {
					bool isThisWordMatch = false;
					for (int j = 0; j < choices.size(); j++) {
						if (choices[j] == word->at(search_index)) {
							isThisWordMatch = true;
							break;
						}
					}

					if (!isThisWordMatch) {
						word = dd.erase(word);
					} else {
						++word;
					}
				}

				choices.clear();
				c = false;
				search_index++;
				continue;
			}
			
			if (c) {
				choices.push_back(letter);
				continue;
			}

			for(vector<string>::iterator word = dd.begin(); word != dd.end(); ) {
				if (letter != word->at(search_index)) {
					word = dd.erase(word);
				} else {
					++word;
				}
			}
			search_index++;
		}
		
		int answer = dd.size();
		cout << "Case #" << cas+1 << ": " << answer << endl;
	}
}
