#include<fstream>
#include<iostream>
#include<vector>
#include<set>
#include<string>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("bout.txt");

#if 1
#define cin fin
#define cout fout
#endif

bool des(string input){
	for(int i=1; i<input.size(); i++) 
		if(input[i]>input[i-1]) return false;
	return true;
}

string mini(string input, bool leading){
	string ret;
	vector<int> num(10, 0);
	for(int i=0; i<input.size(); i++)  num[input[i]-'0']++;
	if(leading)
	for(int i=1; i<10; i++) if(num[i]>0){ ret.push_back(char('0'+i)); num[i]--; break; }
	for(int i=0; i<10; i++) while(num[i]-->0) ret.push_back(char('0'+i)); 
	return ret;
}

int main(){
	int n;  cin>>n;
	for(int i=1; i<=n; i++){
		string input;  cin>>input;
		cout<<"Case #"<<i<<": ";
		if(des(input)){
			input.push_back('0');  cout<<mini(input, true)<<endl;
		}else{
			int len;
			for(len=input.size()-1; len>0; len--){
				if(!des(input.substr(len))) break;
			}
			string res = input.substr(len);
			int ii, pos=-1;
			for(ii=1; ii<res.size(); ii++) if(res[ii]>res[0] && (pos<0 || res[ii]<res[pos])){ pos = ii; }
			swap(res[0], res[pos]);
			cout<<string(input.begin(), input.begin()+len)+res[0]+mini(res.substr(1),false)<<endl;
		}
	}
}