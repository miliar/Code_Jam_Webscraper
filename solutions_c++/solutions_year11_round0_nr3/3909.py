#include <iostream>
#include <string> 
#include <fstream>
#include <cmath>
#include <vector>
#include <bitset>

using namespace std;

typedef bitset<1000> KBits;
KBits bits(0);
int len;
int maxval = -1;
vector<int> arr;

void select(int first, int last, int sel)
{

	if (!sel) {
		int s1, s2, v1, v2;
		s1 = s2 = 0;
		v1 = v2 = 0;
		for (int i = 0; i<len; i++) {
			//cout<<bits[i];
			if (bits[i]) {
				s1 ^= arr[i];
				v1 += arr[i];
			}
			else {
				s2 ^= arr[i];
				v2 += arr[i];
			}
		}
		//cout<<endl;
		//cout<<"   ("<<s1<<", "<<s2<<")"<<"   ("<<v1<<", "<<v2<<")"<<endl;
		if (s1==s2) {
			if (v1>maxval) maxval = v1;
			if (v2>maxval) maxval = v2;
		}
		return;
	}

	if (first>=last) return;

	bits[first] = 1;
	select(first+1, last, sel-1);
	bits[first] = 0;
	select(first+1, last, sel);
}

int divide() 
{
	int ret = -1;
	len = arr.size();
	

	for (int l = 1; l<=len/2; l++) {
		maxval = -1;
		select(0, len, l); 
		if (maxval>ret) ret = maxval;
	}

	return ret;
}

int main(int argc, char* argv[]) 
{
	ifstream infile;
	ofstream out;

	infile.open (argv[1], ifstream::in);
	out.open (argv[2], ifstream::out);

	int T, N;

	infile>>T;
	
	for (int t=0; t<T; t++) {

		arr.clear();

		infile>>N;
		for (int i = 0; i<N; i++) {
			int v;
			infile>>v;
			arr.push_back(v);
		}
		
		int val = divide();
		
		cout<<"Case #"<<t+1<<": ";
		if (val>0) cout<<val<<endl;
		else cout<<"NO"<<endl;

		out<<"Case #"<<t+1<<": ";
		if (val>0) out<<val<<endl;
		else out<<"NO"<<endl;

	}


	infile.close();
	out.close();

    return 0;
}

