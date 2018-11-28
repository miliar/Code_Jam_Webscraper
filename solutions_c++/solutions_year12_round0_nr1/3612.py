#include <iostream>
#include <fstream>
#include <cstdio>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
using namespace std;
ifstream in("A-small-attempt2.in");
ofstream out("A-small-attempt2.out");
string A = "yhesocvxduiglbkrztnwjpfmaq";
int N;
void solve()
{
	string str;
	int i,j;
	in >> N;
	getline(in,str);
	FOR2(i,N)
	{
		getline(in,str);
		out << "Case #" << i+1 << ": ";
		FOR2(j,str.size())
			if(str[j] == ' ')
				out << " ";
			else
			out << A[str[j]-'a'];
		out << endl;
	}
}
int main()
{
	solve();
	return 0;
}
