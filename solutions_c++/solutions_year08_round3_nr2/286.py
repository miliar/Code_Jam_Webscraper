#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <numeric>
#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
#define FORC(x) for(int i=0;i<(int)(x).size();++i)
#define SHOW(v,t,sep) copy((v).begin(),(v).end(),ostream_iterator<t>(cout,sep));cout << endl;
#define MSG(X) cout << #X << "=" << X << endl
#define COPY(s,v) copy((s),(s+sizeof(s)/sizeof(s[0])),back_inserter(v));
//template <class T> struct Max : public binary_function<T,T,T>{T operator()(T lhs,T rhs)const{return max(lhs,rhs);}};
//template <class T> struct Min : public binary_function<T,T,T>{T operator()(T lhs,T rhs)const{return min(lhs,rhs);}};
typedef vector<long long> VL;

int counter;
bool ugly(long long n){
	if(n%2==0 || n%3==0 || n%5==0 || n%7==0)return true;
	return false;
}
void make(string str,int pos,int end,long long sum){
	long long n;
	if(end>=str.size()){
		if(pos==end){
//			MSG(sum);
			if(ugly(sum))++counter;
		}
		else{
			istringstream is(str.substr(pos,end-pos));
			is >> n;
//			MSG(sum+n);
			if(ugly(sum+n))++counter;
			if(pos!=0){
//				MSG(sum-n);
				if(ugly(sum-n))++counter;
			}
			return;
		}
	}
	istringstream is(str.substr(pos,end-pos));
	is >> n;
	//{|‚Í‚³‚Ü‚È‚¢
	make(str,pos,end+1,sum);
	//{‚ğ‹²‚Ş
	make(str,end,end+1,sum+n);
	//-‚ğ‹²‚Ş
	if(pos!=0)
	make(str,end,end+1,sum-n);
}
int main(int argc,char**argv){
	if(argc<=1){cout << "input arg\n";return 1;}
	ifstream ifs;
	ifs.open(argv[1],ios_base::in);
	if(!ifs){cout << "fstream error\n";return 1;}
	char str[255];
/*
	while(!ifs.eof()){
		ifs.getline(str,255);
		cout << str << endl;
	}
	ifs.close();
*/
	if(!ifs.eof()){ifs.getline(str,255);}
	int n;
	istringstream is(str);
	is >> n;
	for(int i=0;i<n;++i){
		ifs.getline(str,255);
		istringstream iss(str);
		string s(str);
		counter=0;
		make(s,0,1,0);
		cout << "Case #" << i+1 << ": " << counter << endl;
	}
	return 0;
}
