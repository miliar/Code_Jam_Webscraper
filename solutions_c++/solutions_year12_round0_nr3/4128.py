#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<fstream>
#include<cmath>
#include<sstream>
using namespace std;
int A,B;
string rotator(string s){
	for(int i=1;i<s.length();i++)
		swap(s[i],s[i-1]);
	return s;

}

int cyclic(int i){
	string s;
	stringstream ss;
	ss<<i;
	ss>>s;
	vector<string> watchus;
	int count=0;
	for(int j=1;j<s.length();j++){
		s=rotator(s);
		int pivot=atoi(s.c_str());
		if(pivot>i && pivot<=B && s[0]!=0 ){
			bool adhim=true;
			for(int p=0;p<watchus.size();p++) if(s==watchus[p]) adhim=false;
			if(adhim==true){ count++; watchus.push_back(s);}
		}
	}
	return count;


}

int main(){
	ifstream in;
	ofstream out;
	in.open("C-small-attempt0.in");
	out.open("out.txt");
	int T;
	in>>T;
	for(int k=0;k<T;k++){
		in>>A>>B;
		int fcount=0;
		for(int i=A;i<=B;i++)
			fcount+=cyclic(i);

		out<<"Case #"<<k+1<<": "<<fcount<<endl;
	}
	return 0;


}