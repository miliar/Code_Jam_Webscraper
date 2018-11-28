#include <iostream>
#include <string>
#include <map>

using namespace std;

int main(){
	int N;
	int S, Q;
	cin >> N;
	bool arr[100];
	map<string, int> list;
	string str;
	for(int I = 1; I <= N; I++){
		list.clear();
		cin >> S;
		cin.get();
		for(int i = 0; i < S; i++){
			getline(cin, str);
			list[str] = i;
			arr[i] = false;
		}
		cin >> Q;
		cin.get();
		int c = 0;
		int shift = 0;
		for(int j = 0; j < Q; j++){
			getline(cin, str);
			if(!arr[list[str]]){
				arr[list[str]] = true;
				c++;
			}
			if(c == S){
				shift++;
				c = 1;
				int t = list[str];
				for(int k = 0; k < S;k++){
					if(k != t) arr[k] = false;
				}
			}
		}
		cout <<"Case #"<<I<<": "<<shift<<"\n";		
	}
	return 0;
}
