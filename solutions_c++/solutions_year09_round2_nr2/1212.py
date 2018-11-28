#include<iostream>
#include<map>
#include<vector>
#include<sstream>

using namespace std;

map<int, int> m;

string itos(int input){
        stringstream ss;
        ss << input;
        return ss.str();
}


//inputの次を求める
string calc(string input){
	string out = input;
	//全部昇順だったらfalse
	bool flag = false;
	int size = input.size();
	if(size == 1) return itos(atoi(input.c_str()) * 10);
	int right;//最初は一番右
	//右からみていく
	for(int i=size-2;i>=0;--i){
		right = input[i+1] - '0';
		if((input[i] - '0') < right){
			flag = true;

			//cout << i << endl;

			//右側に何があるかmapにつっこむ
			for(int j=i;j<size;++j){
				if(m[input[j] - '0'] == 0) m[input[j] - '0'] = 1;
				else m[input[j] - '0']++;
			}

			//for(map<int,int>::iterator it = m.begin(); it != m.end(); ++it){
			//	cout << it->first << ":" << it->second << endl;
			//}

			map<int, int>::iterator it = ++(m.find(input[i] - '0'));
			out[i] = it->first + '0';

			if(m[it->first] == 1) m.erase(it);
			else m[it->first]--;

			//for(map<int,int>::iterator it = m.begin(); it != m.end(); ++it){
			//	cout << it->first << ":" << it->second << endl;
			//}

			for(int j=i+1;j<size;++j){
				it = m.begin();
				out[j] = it->first + '0';	
				//cout << out[j] << endl;
				if(m[it->first] == 1) m.erase(it);
				else m[it->first]--;
			}

		}
		if(flag) break;
	}

	if(!flag){
		return calc("0" + out);
	}

	return out;
}

int main(){
	int num;
	cin >> num;
	vector<string> results;
	for(int i=0;i<num;++i){
		string input;
		cin >> input;
		results.push_back(calc(input));
		//for(map<int,int>::iterator it = m.begin(); it != m.end(); ++it){
		//	cout << it->first << ":" << it->second << endl;
		//}
		m.clear();
		//cout << endl;
	}

	for(int i=0;i<num;++i){
		cout << "Case #" << i+1 << ": " << results[i] << endl;
	}
	return 0;
}
