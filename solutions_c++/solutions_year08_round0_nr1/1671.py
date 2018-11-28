#include<iostream>
#include<map>
#include<vector>
#include<string>
using namespace std;
int main(){
	char in[1024];
	map<string, int> seq;
	map<int, int> se;
	vector<int> query;
	int N, S, Q;
	cin >> N;
	for(int times = 1; times <= N; times++){
		cin >> S;
		cin.getline(in, 1023);
		for(int i = 0; i < S; i++){
			cin.getline(in, 1023);
			seq.insert(pair<string, int>(in, i));
		}
		cin >> Q;
		cin.getline(in, 1023);
		for(int i = 0; i < Q; i++){
			cin.getline(in, 1023);
			string key = in;
			query.push_back(seq[key]);
		}
		int begin = 0;
		int out = 0;
		if(Q == 0){
			cout << "Case #" << times << ": " << 0 << endl;
		}
		else{
			while(begin != Q){
				for(int i = 0; i < S; i++){
					se.insert(pair<int, int>(i, -1));
				}
				int fit = 0;
				for(int i = begin; i < Q; i++){
					if(se[query[i]] == -1){
						se[query[i]] = i;
						fit++;
					}
					if(fit == S){
						break;
					}
				}
				if(fit != S){
					break;
				}
				else{
					int max = 0;
					int para = -1;
					for(map<int, int>::iterator i = se.begin(); i != se.end(); i++){
						if(max < i->second){
							para = i->first;
							max = i->second;
						}
					}
					begin = max;

					out++;
				}
				se.clear();
			}
			cout << "Case #" << times << ": " << out << endl;
		}
		
		seq.clear();
		se.clear();
		query.clear();
	}
}
