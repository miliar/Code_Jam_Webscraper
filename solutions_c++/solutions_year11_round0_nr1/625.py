#include <iostream>
#include <string>
#include <sstream>
#include <queue>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

void eval(){
	queue<int> bq, oq;
	queue<char> r;
	int N;
	cin>>N;
	for(int i=0; i<N; i++){
		char c;
		int p;
		cin>>c>>p;
		if(c=='B')
			bq.push(p);
		else
			oq.push(p);
		r.push(c);
	}
	int bp=1, op=1, elapsed=0;
	for(; !r.empty(); elapsed++){
		char baction=0, oaction=0;
		if(r.front()=='B' && bp==bq.front()){
			r.pop();
			bq.pop();
			baction=1;
		}else if(r.front()=='O' && op==oq.front()){
			r.pop();
			oq.pop();
			oaction=1;
		}
		if(!baction && !bq.empty()){
			if(bp<bq.front())
				bp++;
			else if(bp>bq.front())
				bp--;
		}
		if(!oaction && !oq.empty()){
			if(op<oq.front())
				op++;
			else if(op>oq.front())
				op--;
		}
	}
	cout<<elapsed<<endl;
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}
