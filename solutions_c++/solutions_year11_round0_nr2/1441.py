#include<fstream>
#include<iostream>
#include<string>

using namespace std;

char com[256][256];
bool opp[256][256];

int main(){

	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	cin.rdbuf(fin.rdbuf());
	cout.rdbuf(fout.rdbuf());	

	char ch;
	string s,res;
	int c,d;

	int ntc;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){

		memset(com,0,sizeof(com));
		memset(opp,0,sizeof(opp));

		cin >> c;
		while(c--){
			cin >> s;
			com[s[0]][s[1]] = com[s[1]][s[0]] = s[2];
		}
		cin >> d;
		while(d--){
			cin >> s;
			opp[s[0]][s[1]] = opp[s[1]][s[0]] = true;
		}
		cin >> d >> s;
		res = "";
		for (int i=0;i<d;i++){
			if (res.empty())
				res+=s[i];
			else if (ch = com[s[i]][res[res.length()-1]]){
				res[res.length()-1]=ch;
			}
			else{
				res+=s[i];
				for (int k=0;k<res.length();k++){
					if (opp[s[i]][res[k]]){
						res = "";
						break;
					}
				}
			}
		}
		cout << "Case #" << tc << ": [";
		if (!res.empty()){
			for (int i=0;i<res.length()-1;i++)
				cout << res[i] << ", ";
			cout << res[res.length()-1];
		}
		cout << "]" << endl;


	}


	

	return 0;
}