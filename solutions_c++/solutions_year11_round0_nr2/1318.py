									/* in the name of Allah */
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

//ifstream fin("B-smallarge.in");
//ofstream fout("B-smallarge.out");

//#define cin fin
//#define cout fout
/*
char arr[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
bool mat[10][10];
char ch[10][10];
int cnt[10];
vector <char> res;

int getId(char ch){
	for(int i = 0; i < 8; i++)
		if(arr[i] == ch)
			return i;
	return -1;
}*/

int main(){
	/*int T, test = 0, t;
	cin >> test;
	char a, b, c;
	string str;
	for(cin >> T; T--; ){
		res.clear();
		memset(mat, false, sizeof mat);
		memset(cnt, 0, sizeof cnt);
		memset(ch, 0, sizeof ch);
		cin >> t;
		for(int i = 0; i < t; i++){
			cin >> a >> b >> c;
			ch[getId(a)][getId(b)] = ch[getId(b)][getId(a)] = c;
		}
		cin >> t;
		for(int i = 0; i < t; i++){
			cin >> a >> b;
			mat[getId(a)][getId(b)] = mat[getId(b)][getId(a)] = true;
		}
		cin >> str;
		for(int i = 0; i < str.length(); i++){
			int id = getId(str[i]);
			if(!res.empty()){
				int pid = getId(res[res.size() - 1]);
				if(pid != -1 && ch[id][pid] != 0){
					cnt[pid]--;
					res[res.size() - 1] = ch[id][pid];
					continue;
				}
			}
			bool fl = false;
			for(int j = 0; j < 8; j++){
				if(cnt[j] > 0 && mat[id][j]){
					fl = true;
					res.clear();
					memset(cnt, 0, sizeof cnt);
				}
			}
			if(!fl){
				cnt[id]++;
				res.push_back(str[i]);
			}
		}
		cout << "Case #" << ++test << ": [";
		for(int i = 0; i < res.size(); i++){
			if(i > 0) cout << ", ";
			cout << res[i];
		}
		cout << "]" << endl;
	}*/
	int n;
	cout << "A" << endl;
	cin >> n;
	return 0;
}
