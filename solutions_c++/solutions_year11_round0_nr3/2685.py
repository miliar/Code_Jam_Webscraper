#include<iostream>
#include<vector>
#include<string>
#include<fstream>
#include<new>

using namespace std;

static int ps;
static int ss;

int solve(int n, int c[])
{
	int min = c[0];
	for(int i = 1; i < n; i++)
		if(c[i]<min)
			min = c[i];
	return ss - min;
}
int main()
{
	char input[]="C-large.in";
	char output[]="ldata.out";
	ifstream in(input);
	ofstream out(output);
	int T;
	in>>T;
	int c[1000];
	for(int i = 1; i <= T; i++){
		ps = 0;
		ss = 0;
		int n;
		int r;
		in>>n;
		for(int j = 0; j < n; j++){
			in>>c[j];
			ps=ps^c[j];
			ss+=c[j];
		}
		out<<"Case #"<<i<<": ";
		if(ps !=0 )
			out<<"NO"<<endl;
		else
			out<<solve(n, c)<<endl;
	}
	in.close();
	out.close();
}
