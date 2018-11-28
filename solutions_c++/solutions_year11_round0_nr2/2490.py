#include <vector>
#include <iostream>
#include <string> 

using namespace std;

int main()
{
	int T;
	cin>>T;
	for (int t = 0; t < T; ++t) {
		vector<string> combos;
		vector<string> opposed;
		
		int C;
		cin>>C;
		for (int i = 0; i< C;++i) {
			string combo;
			cin>>combo;
			combos.push_back(combo);
		}
		int D;
		cin>>D;
		for(int i = 0; i<D;++i) {
			string op;
			cin>>op;
			opposed.push_back(op);
		}
		int N;
		cin>>N;
		string input;
		cin>>input;
		string list = "";
		for (int j = 0; j<N;++j) {
			if(list.size() == 0) {
				list.append(1, input[j]);
			}
			else {
				bool processed = false;
				for (int i = 0; i< C;++i) {
					if((combos[i][0] == input[j] && combos[i][1] == list[list.size()-1])||(combos[i][0] == list[list.size()-1] &&combos[i][1] == input[j])) {
						list[list.size()-1] = combos[i][2];
						processed = true;
						break;
					}
				}
				if(!processed) {
					for(int i = 0; i<D && !processed; ++i) {
						if(opposed[i][0] == input[j] || opposed[i][1] == input[j]){
							for(int k = 0; k<list.size();++k) {
								if(list[k] != input[j] && (list[k] == opposed[i][0] || list[k] == opposed[i][1])) {
									list = "";
									processed = true;
									break;
								}
							}
						}
					}
					if(!processed) {
						list.append(1, input[j]);
					}
				}
			}
		}
		cout<<"Case #"<<t+1<<": [";
		for(int i = 0; i<list.size();++i) {
			if(i>0) {
				cout<<", ";
			}
			cout<<list[i];
		}
		cout<<"]"<<endl;
	}
}
