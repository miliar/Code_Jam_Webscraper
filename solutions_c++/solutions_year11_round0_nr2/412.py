#include <iostream>
#include <vector>
#define pb push_back

using namespace std;

vector<char> res;
char map[255][255];
bool mark[255][255];

inline void printArray(vector<char> data){
	cout << "[";
	for (int i=0 ; i<(int)data.size()-1 ; i++)
		cout << data[i] << ", ";
	if (data.size()>0)
		cout << data[ data.size()-1 ];
	cout << "]";
	
}
int main(){
	int test;
	cin >> test;
	for (int t=1 ; t<=test ; t++){
		memset(map, 0, sizeof map);
		memset(mark, 0, sizeof mark);
		
		int tmp;
		cin >> tmp;
		while(tmp--){
			string s;
			cin >> s;
			map[ s[0] ][ s[1] ]= map[ s[1] ][ s[0] ]= s[2];
		}
		cin >> tmp;
		while(tmp--){
			string s;
			cin >> s;
			mark[ s[0] ][ s[1] ]= mark[ s[1] ][ s[0] ]= true;
		}
		int n;
		cin >> n;
		res.clear();
		for (int i=0 ; i<n ; i++){
			char ch;
			cin >> ch;
			if (res.empty()){
				res.pb(ch);
				continue;
			}
			if (map[ ch ][ res.back() ]!=0){
				char now= map[ ch ][ res.back() ];
				res.pop_back();
				res.pb( now );
				continue;
			}
			bool cleared= false;
			for (unsigned int i=0 ; i<res.size() ; i++)
				if (mark[ ch ][ res[i] ]){
					res.clear();
					cleared= true;
					break;
				}
			if (!cleared)
				res.pb(ch);
		}
		cout << "Case #" << t << ": ";
		printArray( res );
		cout << endl;
		
	}
	return 0;
}