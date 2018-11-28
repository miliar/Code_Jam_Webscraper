#include <vector>
#include<fstream>
#include<iostream>
#include<string>

using namespace std;

#if 1
//ifstream fin("A-small-attempt0.in");
//ofstream fout("A-small-attempt0.out");
//ifstream fin("A-small-attempt1.in");
//ofstream fout("A-small-attempt1.out");
ifstream fin("A-large.in");
ofstream fout("A-large.out");
#define cin fin
#define cout fout
#endif

int main(){
	int cases;  cin>>cases;
	for(int cid=1; cid<=cases; cid++){
		cout<<"Case #"<<cid<<": "; //<<endl;
		
		string input;
		cin>>input;
		long long res = 0LL;
		int base = 0;
		int mp[256];  memset(mp, -1, sizeof(mp));
		mp[int(input[0])] = 1;
		for(int i=1; i<input.length(); i++){
			if(base==1) base++;
			if(mp[int(input[i])]<0)
				mp[int(input[i])] = base++;
		}
		if(base<2) base = 2;
		for(int i=0; i<input.length(); i++){
			res = res*base + mp[int(input[i])];
		}
		cout<<res<<endl;
	}
	return 0;
}