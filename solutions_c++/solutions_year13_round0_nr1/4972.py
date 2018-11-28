#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
#define Xwon 0
#define Owon 1
#define Draw 2
#define NC   3

ifstream fin("A-large.in");
ofstream fout("A-large.out");

string ans[5]={": X won\n",": O won\n",
	": Draw\n",": Game has not completed\n",
	"Case #"};
bool
chk(vector<string> &record , char type){
	string ans;
	for(int i = 0 ; i < 4 ; i++)
		ans += type;

	for(int i = 0 ; i < 4 ; i++){
		if(record[i].compare(ans) == 0)
			return true;
	}
	string tmp;
	for(int j = 0 ; j < 4 ; j++){
		tmp = "";
		for(int i = 0 ; i < 4 ; i++){
			tmp += record[i][j];
		}
		if(tmp.compare(ans) == 0)
			return true;
	}

	tmp = "";
	for(int i = 0 ; i < 4 ; i++)
		tmp += record[i][i];
	if(tmp.compare(ans) == 0)
		return true;

	tmp = "";
	for(int i = 0 ; i < 4 ; i++)
		tmp += record[i][3-i];
	if(tmp.compare(ans) == 0)
		return true;

	return false;

}

int 
solve(){
	vector<string>record;
	int Tx = -1;
	int Ty = -1;
	bool hasT = false;
	bool is_NC = false;
	string tmp;
	for(int i = 0 ; i < 4 ; i++){
		tmp = "";
		for(int j = 0 ; j < 4 ; j++){
			char ch;
			fin>>ch;
			if(ch == '.')
				is_NC = true;
			if(ch == 'T'){
				Tx = i;
				Ty = j;
				hasT = true;
				ch = 'O';
			}
			tmp += ch;
		}
		record.push_back(tmp);
		fin.get();
	}
	if(chk(record,'X'))
		return Xwon;
	if(chk(record,'O'))
		return Owon;
	if(hasT){
		record[Tx][Ty] = 'X';
		if(chk(record,'X'))
			return Xwon;
		if(chk(record,'O'))
			return Owon;
	}
	if(!is_NC)
		return Draw;
	else
		return NC;
}
int
main(){
	int NUM;
	fin >> NUM;

	for(int i = 0 ; i <NUM ; i++){
		fout<<ans[4]<<i+1<<ans[solve()];
	}

	return 0;
}
