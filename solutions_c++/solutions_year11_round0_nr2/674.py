#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

int main(){
	int i=0,n;
	cin >> n;
	while(++i<=n){
		int C,D,N;
		string buf;
		typedef pair<char,char> cpair;
		typedef pair<cpair,char> cpairpair;
		map<cpair, char> com_map;
		multimap<char, char> opp_map;
		vector<char> result_vec;
		cin >> C;
		while(C-->0){
			cin >> buf;
			com_map.insert(cpairpair(cpair(buf[0], buf[1]), buf[2]));
			com_map.insert(cpairpair(cpair(buf[1], buf[0]), buf[2]));
		}
		cin >> D;
		while(D-->0){
			cin >> buf;
			opp_map.insert(cpair(buf[0],buf[1]));
			opp_map.insert(cpair(buf[1],buf[0]));
		}
		cin >> N;
		cin >> buf;
		int iN = -1;
		while(++iN<N){
			if(result_vec.size()==0){
				result_vec.push_back(buf[iN]);
				continue;
			}
			char now_c = buf[iN];
			map<cpair, char>::iterator com_it = com_map.find(cpair(now_c, result_vec.back()));
			if(com_it!=com_map.end()){
				now_c = com_it -> second;
				result_vec.pop_back();
			}else{
				vector<char>::iterator res_it = result_vec.end();
				vector<char>::iterator res_end = result_vec.begin();
				pair<multimap<char, char>::iterator, multimap<char, char>::iterator> opp_range = opp_map.equal_range(now_c);
				while(1){
					res_it--;
					multimap<char, char>::iterator opp_it = opp_range.first;
					for(;opp_it != opp_range.second; opp_it++){
						if(opp_it->second==*res_it){
							result_vec.clear();
							goto END;
						}
					}
					if(res_it==res_end)break;
				}
			}
			result_vec.push_back(now_c);
			END:
		}
		cout << "Case #" << i << ": [";
		if(result_vec.size()>0){
			int k = 0;
			while(1){
				 cout << result_vec[k];
				 k++;
				 if(k >= result_vec.size())
				 	break;
				 cout << ", ";
			}
		}
		cout << "]" << endl;
	}
	return 0;
}