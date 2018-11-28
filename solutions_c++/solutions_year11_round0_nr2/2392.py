#include <iostream>
#include <fstream>

using namespace std;

struct E1 {
	char A;
	char B;
	char C;
};

struct E2 {
	char A;
	char B;
};
E1 R1s[40];
E2 R2s[30];
E1 R1;
E2 R2;

int f(char a, char b) {
	for(int k1=0;k1<40;++k1) {
		R1 = R1s[k1];
		if(R1.A == a && R1.B == b) {
			return R1.C;
		}
		if(R1.A == b && R1.B == a) {
			return R1.C;
		}
	}

	return 0;
}

int g(char a, char b) {
	for(int k1=0;k1<30;++k1) {
		R2 = R2s[k1];
	
		if(R2.A == a && R2.B == b) {
			return 1;
		}
		if(R2.A == b && R2.B == a) {
			return 1;
		}
	}
	return 0;
}


ifstream fin("file.in");
ofstream fout("file.out");

int T, C, D, N;	
int c, d, n;
int main() {
	char cs[5];
	char cd[4];
	char cn[200];
	char *out = new char[200];
	int o=0;
	char s;
	int k;

	fin>>T;
	for(int t=1; t<=T; ++t) {
		fin>>C;

		for(int k1=0;k1<40;++k1) {
			R1s[k1].A= 0;
			R1s[k1].B= 0;
			R1s[k1].C= 0;
		}
		for(int k1=0;k1<30;++k1) {
			R2s[k1].A= 0;
			R2s[k1].B= 0;
		}

		for(c=0;c<C;++c) {
			fin>>cs;
			R1s[c].A= cs[0];
			R1s[c].B= cs[1];
			R1s[c].C= cs[2];
		}
	

		fin>>D;
		for(d=0;d<D;++d) {
			fin>>cd; 
			R2s[d].A= cd[0];
			R2s[d].B= cd[1];
		}

		fin>>N;
		fin>>cn;
		o=0;
		out[0] = cn[0];
		for(n=1;n<N;++n) {
			o++;
			out[o] = cn[n];
			if(o>0) {
				s = f(out[o], out[o-1]);
				if(s) {
					o--;
					out[o] = s;
				}
				else {
					for(k=0;k<o;++k)
					if(g(out[o] , out[k]))
						o=-1;
				}
			}
		}
		o++;
		out[o] = '\n';
		fout<<"Case #"<<t<<": [";
		if(o==0) 
			fout<<"]"<<endl;
		else {
			fout<<out[0];
			for(k=1;k<o;++k) {
				fout<<", "<<out[k];
			}
			fout<<"]"<<endl;
		}
	}

	return 0;
}