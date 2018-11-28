#include <iostream>
#include <string>
#include <vector>
using namespace std;

inline long long mpow(const int &b, const int &t){
	long long rst=1;
	for(int i=1; i<=t; ++i)
		rst*=b;
	return rst;
}

vector<char> data;

bool apped[256];
int map[256];

int main(){
	int N;
	long long rst;
	string in;
	cin>>N;
	for(int n=0; n<N; ++n){
		rst=0;
		data.clear();
		cin>>in;
		for(string::iterator i=in.begin(); i!=in.end(); ++i){
			if(!apped[*i]){
				apped[*i]=1;
				data.push_back(*i);
			}
		}
		for(vector<char>::iterator i=data.begin(); i!=data.end(); ++i){
			map[*i]=i-data.begin();
			apped[*i]=0;
		}
		map[*(data.begin())]=1;
		if(data.size()>=2)
			map[*(data.begin()+1)]=0;
//		for(string::iterator i=in.begin(); i!=in.end(); ++i)
//			cout<<map[*i];
		int base=data.size()>1?data.size():2;
		for(string::iterator i=in.begin(); i!=in.end(); ++i){
			rst+=map[*i]*mpow(base, in.size()-(i-in.begin())-1);
		}
		cout<<"Case #"<<n+1<<": "<<rst<<'\n';
	}
	return 0;
}

