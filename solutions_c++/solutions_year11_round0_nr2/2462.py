#include <iostream>
#include <vector>
#include <string>
using namespace std;


int main(){
	int t_case;
	cin >> t_case ;
	for(int t_i = 0 ; t_i < t_case ; t_i++){
		vector <string> compose;
		vector <string> opposite;
		vector <char>   result;
		int c_num, d_num, num;
		cin >> c_num;
		string temp;
		for(int i = 0; i < c_num; i++){
			cin >> temp;
			compose.push_back(temp);
		}
		cin >> d_num;
		for(int i = 0 ; i < d_num; i++){
			cin >> temp;
			opposite.push_back(temp);
		}
		cin >> num;
		char c_chr = ' ', l_chr;
		for(int i_n = 0; i_n < num; i_n++){
			cin >> c_chr;
			if(result.empty()){
				result.push_back(c_chr);
				continue;
			}
			l_chr = result.back();
			int j = 0;
			for(j = 0; j < compose.size(); j++){
				if(compose[j][0]==l_chr && compose[j][1] == c_chr || compose[j][1]==l_chr && compose[j][0] == c_chr){
					result.pop_back();
					result.push_back(compose[j][2]);
					break;
				}
			}
			if(j<compose.size()){
				continue;
			}
			bool erased = false;
			for(j = 0; j < opposite.size() ; j++){
				if(opposite[j][1]==c_chr){
					int k;
					for(k = result.size()-1; k >=0; k--){
						if(result[k] == opposite[j][0]) break;
					}
					if(k >= 0){
						erased = true;
						result.clear();
						break;
					}
				}
				if(opposite[j][0]==c_chr){
					int k;
					for(k = result.size()-1; k >=0; k--){
						if(result[k] == opposite[j][1]) break;
					}
					if(k >= 0){
						erased = true;
						result.clear();
						break;
					}
				}
			}
			if(!erased) result.push_back(c_chr);
		}
		cout << "Case #" << t_i+1 <<": [";
		if(result.size() > 1){
		  for(int i = 0; i < result.size()-1 ; i++){
			  cout << result[i]<<", ";
		  }
	  } 
		if(!result.empty()) cout << result.back() << "]" << endl;
		else cout <<"]" << endl;
	}
}