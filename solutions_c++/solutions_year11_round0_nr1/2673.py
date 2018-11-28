#include<iostream>
#include<vector>
#include<string>
#include<fstream>
#include<new>

using namespace std;
int abs(int t)
{
	if(t > 0)
		return t;
	if(t < 0)
		return -t;
}
int main()
{
	int T;
	char s[]="A-small-attempt0.in";
	char t[]="data.out";
	ifstream in(s);
	ofstream out(t);
	in>>T;
	for(int k = 1; k <= T; k++){
		int n;
		int p[100];
		char r[100];
		int f[100];
		in>>n;
		p[0] = 1;
		r[0] = 'A';
		f[0] = 0;
		for(int q = 1; q <= n; q++) {
			in>>r[q];
			in>>p[q];
		}
		for(int q = 1; q <= n; q++) {
			int i, j;
			if(r[q] == 'B'){
				for(i = q-1; i >= 0; i--)
					if(r[i] == 'A' || r[i] == 'O')
						break;
				for(j = q -1; j >=0; j--)
					if(r[j] == 'A' || r[j] == 'B')
						break;
				f[q] = (f[i] - f[j])>abs(p[q]-p[j])?\
					f[i]+1:f[j]+abs(p[q]-p[j])+1;
			}
			if(r[q] == 'O'){
				for(i = q-1; i >= 0; i--)
					if(r[i] == 'A' || r[i] == 'B')
						break;
				for(j = q -1; j >=0; j--)
					if(r[j] == 'A' || r[j] == 'O')
						break;
				f[q] = ((f[i] - f[j])>abs(p[q]-p[j]))?(f[i]+1):(f[j]+abs(p[q]-p[j])+1);
			}
		}
		out<<"Case #"<<k<<": "<<f[n]<<endl;
	}
	return 0;
}
