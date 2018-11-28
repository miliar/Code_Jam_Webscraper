#include <iostream>
#include <vector>
#include <set>
using namespace std;
typedef struct combine{
	char a;
	char b;
	char c;
}combine;
typedef struct oppose{
	char a;
	char b;
}oppose;
int main(void){
	int T;
	cin >> T;
	for(int test_case = 1; test_case <= T; ++test_case){
		int C, D, N;
		cin >> C;
		vector<combine> c;
		vector<oppose> o;
		vector<char> input;
		set<char> rules;
		for(int i = 0; i < C; ++i){
			char a,b,t;
			cin >> a >> b >> t;
			combine x;
			x.a = a;
			x.b = b;
			x.c = t;
			c.push_back(x);
			rules.insert(a);
			rules.insert(b);
		}
		cin >> D;
		for(int i = 0; i < D; ++i){
			char a,b;
			cin >> a >> b;
			oppose x;
			x.a = a;
			x.b = b;
			o.push_back(x);
			rules.insert(a);
			rules.insert(b);
		}
		cin >> N;
		for(int i = 0; i < N; ++i){
			char in;
			cin >> in;
			if(rules.find(in) != rules.end() and input.size()>0){
				bool comb = false;
				for(int j = 0; j < c.size(); ++j){
					if(in == c[j].a){
						if(input[input.size()-1] == c[j].b){
							input[input.size()-1] = c[j].c;
							comb = true;
						}
						break;
					}if(in == c[j].b){
						if(input[input.size()-1] == c[j].a){
							input[input.size()-1] = c[j].c;
							comb = true;
						}
						break;
					}
				}
				if(!comb){
					for(int i = 0; i < o.size(); ++i){
						if(in == o[i].a){
							for(int j = 0; j < input.size(); ++j){
								if(input[j] == o[i].b){
									input.clear();
									goto END;
								}
							}
						}else if( in == o[i].b){
							for(int j = 0; j < input.size(); ++j){
								if(input[j] == o[i].a){
									input.clear();
									goto END;
								}
							}
						}
					}
					input.push_back(in);
					END:;
				}
			}else{
				input.push_back(in);
			}
		}
		cout << "Case #" << test_case << ": [";
		for(int i = 0; i < input.size();++i){
			cout << input[i];
			if(i < input.size() -1)
				cout << ", ";
		}
		cout << "]" << endl;
	}
}
