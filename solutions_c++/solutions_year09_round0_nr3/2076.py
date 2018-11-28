#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const string phrase = "welcome to code jam";
const string letters = "welcom tdja";
string in;

bool is_valid(char c)
{
	return string::npos != letters.find(c);
}

string validate(string s)
{
	string r="";
	bool first_found=false;
	for(int i = 0; i < s.size(); ++i){
		if(first_found){
			if(is_valid(s[i]))
				r+=s[i];
		}
		else{
			if(s[i]=='w'){
				r+=s[i];
				first_found=true;
			}
		}
	}
	return r;
}

long long result;

void solve(int n, int i)
{
	if(n==phrase.size()){
		result++;
	}
	int pos = in.find(phrase[n],i);
	if(pos != string::npos){
		solve(n+1,pos+1);
		solve(n,pos+1);
	}
}

int main()
{
	int n;
	cin >> n;
	string trash;
	getline(cin,trash);
	for(int i = 0; i < n; ++i){
		string s;
		getline(cin,s);
		in = validate(s);
		result=0;
		solve(0,0);
		char num[4];
		num[3] = '0'+(result/1)%10;
		num[2] = '0'+(result/10)%10;
		num[1] = '0'+(result/100)%10;
		num[0] = '0'+(result/1000)%10;
		cout << "Case #" << i+1 << ": " << num[0] << num[1] << num[2] << num[3] <<  endl;
		clog << in << endl;
	}
}
