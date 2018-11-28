#include <fstream>
#include <string>
#include <strstream>

using namespace std;

ifstream fin("c-small.in");
ofstream fout("c-small.out");

const string ori="welcome to code jam";
string src;
int n;
int ans = 0;

void sub(int o,int s) {
	if (o >= ori.size()) ans = (ans + 1) % 10000;
	else {
		for (int i = s; i < src.size(); i++)
		  if (src[i]==ori[o])
		    sub(o+1,i+1);
	}
}

int main() {
	fin>>n;
	getline(fin,src);
	for (int i = 0; i < n; i++) {
	  getline(fin,src);
	  ans = 0;
	  sub(0,0);
	  
	  fout<<"Case #"<<i+1<<": ";
		//<<ans<<
		if (ans<10) fout<<"0";
		if (ans<100) fout<<"0";
		if (ans<1000) fout<<"0";
		fout<<ans;
		fout<<endl;
	}

}
	  
	
	
