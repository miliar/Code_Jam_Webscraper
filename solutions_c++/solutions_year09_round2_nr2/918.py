#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

int N;
vector<string> tests;

int input_read(char * filename)
{
	ifstream ifs;
	ifs.open(filename, ios::in);
    
    ifs >> N;

	vector<char> buf(1000);
	ifs.getline(&buf[0],1000); //empty line read
	for(int i = 0; i < N; ++i){
		ifs.getline(&buf[0],1000);
		tests.push_back(&buf[0]);
	}

	return 0;
}

string solve(string num){
	vector<int> count(10);
	int len = num.size();

	int max=0;
	int i=len-1;
	for(;i>=0;i--){
		if(num[i]>=max){
			max=num[i];
			count[num[i]-'0']++;
		}else{
			break;
		}
	}

	if(i==-1){
		i=0;
		num="0"+num;
		len++;
		count[0]++;
	}else{
		count[num[i]-'0']++;
	}

		int j=num[i]-'0'+1;
		for(;j<=9;j++){
			if(count[j]>0){
				count[j]--;
				break;
			}
		}
		num[i]=j+'0';


	int now=0;
	for(int k=i+1;k<len;k++){
		while(count[now]==0){now++;}
		num[k]=now+'0';
		count[now]--;
	}

	return num;
}


#define INFILE "B-large.in"

int main(){
	input_read(INFILE);
	ofstream o(INFILE ".out");

	int n = 0;
	for(vector<string>::iterator i = tests.begin(), e = tests.end(); i != e; ++i){
		o << "Case #" << ++n << ": " << solve(*i) << endl;
	}
}
