#include <fstream>
#include <string>

using namespace std;

string word[5001];
string parsed[16];
int l,d,n;

void parse(string in){
	for(int i=0;i<l;i++){
		if(in[0]=='('){
			int j;
			for(j=0;;j++)
				if(in[j]==')') break;
			parsed[i] = in.substr(1, j-1);
			in = in.substr(j+1);
		}
		else{
			parsed[i] = in[0];
			in = in.substr(1);
		}
	}
}

int main(){
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("A-large.out");
	//입력	
	fin>>l>>d>>n;
	for(int i=0;i<d;i++)
		fin>>word[i];
	for(int ci=1;ci<=n;ci++){
		string in;
		fin>>in;
		parse(in);
		//실행
		int cnt=0;
		for(int di=0;di<d;di++){
			//word[di]가 외계인어냐?
			bool iscnt = true;
			for(int i=0;i<l;i++){
				//word[di][i]가 parsed[i]에 존재하나?
				bool find=false;
				for(int j=0;j<parsed[i].size();j++){
					if(parsed[i][j] == word[di][i]){
						find=true;
						break;
					}
				}
				//못찾았으면 외계인 아니야 no cnt!
				if(!find){
					iscnt = false;
					break;
				}
			}
			if(iscnt) cnt++;
		}
		//출력
		fout<<"Case #"<<ci<<": "<<cnt<<endl;
	}
}