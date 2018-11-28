#include<iostream>
#include<vector>
#include<cmath>
#include<sstream>
#define for(a,b,c) for(int a=b; a<c; a++)
using namespace std;

typedef vector<int>vi;
typedef vector<char>vc;

char base[8]={'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};

vector<string> ov;//opposed

vector<string> cv;//combine

char cb(char a, char b){
//cerr<<"\n\tCOMBINECHECK for "<<a<<b<<"\n";
	for(i, 0, cv.size()){
//		cerr<<"\t\tCHECKING AGAINST "<<cv[i][0]<<cv[i][1]<<endl;
		if((a == cv[i][0]&& b == cv[i][1])||
			(a == cv[i][1] && b ==cv[i][0] ))
			return cv[i][2];
//cerr<<"\t\tFAIL\n";
	}
	return 0;
}

bool oppose(vc&el){
//cerr<<"\n\tOPCHECK "<<el.back();
	for(i,0, ov.size()){
		for(j, 0, el.size()-1){
//cerr<<"\t\tCHECKING AGAINST "<<ov[i][0]<<ov[i][1]<<endl;
			char a=el.back();
			char b=el[j];
			if((a == ov[i][0]&& b == ov[i][1])||
			(a == ov[i][1]&& b ==ov[i][0] ))
				return true;
		}
	}
	return 0;
}

bool combine(vc& el){
	char c=cb(el[el.size()-2], el.back());
	if(c){
//cerr<<"COMBINING "<<el.back();
		el.pop_back();
//cerr<<"AND "<<el.back();
		el.pop_back();
		el.push_back(c);
//cerr<<"FOR "<<el.back()<<endl;
		return true;
	}
	else return 0;
}

string solve(string in){
	vc el;
	el.push_back(in[0]);
	for(i,1,in.size()){
		char c=in[i];
//cerr<<c;
		el.push_back(c);
		while(combine(el));
		if(oppose(el))
			el.clear();
	}
	ostringstream out;
	out<<'[';
	if(el.size()){
		out<<el[0];
		for(i,1,el.size()){
			out<<", "<<el[i];
		}
	}
	
	out<<']';
	return out.str();
}

int main(){
	int t;
	istream& in = cin;
//istringstream in("10\n0 0 2 EA\n1 QRI 0 4 RRQR\n1 QFT 1 QF 7 FAQFDFQ\n1 EEZ 1 QE 7 QEEEERA\n0 1 QW 2 QW");
	in>>t;
	for(i,0,t){
		cv.clear();
		int c;
		int d;
		int n;
		in>>c;
		cv.resize(c);
		string temp;
		for(j,0,c){
			in>>cv[j];
//cerr<<cv[j]<<' ';
		}
		ov.clear();
		in>>c;
		ov.resize(c);
		for(j,0,c){
			in>>ov[j];
		}
		in>>n;
		in>>temp;

		cout<<"Case #"<<(i+1)<<": "<<solve(temp)<<endl;
	}
//	system("PAUSE");
	return 0;
}
