#include <iostream>
#include <fstream>

using namespace std;

int mysolve(istream &fi)  {
	char m[4][4]={0};
	bool completed(true);
	char c(0);
	int i(0),j(0),k(0),isx(0),iso(0);
	for (i=0;i<4;++i)
		for(j=0;j<4;++j) {
			fi>>c;
			switch(c) {
			case '.': m[i][j]='.'; completed=false; break;
			case 'T': m[i][j]='T'; break;
			case 'X': m[i][j]='X'; break;
			case 'O': m[i][j]='O'; break;
			default: cerr<<"Unknown char:"<<c<<endl; break;
			}
		}

	/*for (i=0;i<4;++i) {
		for (j=0;j<4;j++)
			cout<<m[i][j];
		cout<<endl;
	}*/
	for (i=0;i<4;++i)  {
		isx=0; iso=0;
		for(j=0;j<4;++j) {
			if (m[i][j]=='.') break;
			if (m[i][j]=='T') {isx++;iso++;}
			if (m[i][j]=='O') {iso++;}
			if (m[i][j]=='X') {isx++;}
		}
		if (isx==4) return 0;
		if (iso==4) return 1;
	}

	for (j=0;j<4;++j)  {
		isx=0; iso=0;
		for(i=0;i<4;++i) {
			if (m[i][j]=='.') break;
			if (m[i][j]=='T') {isx++;iso++;}
			if (m[i][j]=='O') {iso++;}
			if (m[i][j]=='X') {isx++;}
		}
		if (isx==4) return 0;
		if (iso==4) return 1;
	}

	isx=0; iso=0;
	for (i=0;i<4;++i)  {
			if (m[i][i]=='.') break;
			if (m[i][i]=='T') {isx++;iso++;}
			if (m[i][i]=='O') {iso++;}
			if (m[i][i]=='X') {isx++;}
		if (isx==4) return 0;
		if (iso==4) return 1;
	}
	isx=0; iso=0;
	for (i=0;i<4;++i)  {
			if (m[i][3-i]=='.') break;
			if (m[i][3-i]=='T') {isx++;iso++;}
			if (m[i][3-i]=='O') {iso++;}
			if (m[i][3-i]=='X') {isx++;}
		if (isx==4) return 0;
		if (iso==4) return 1;
	}
	return completed?2:3;
}

int main()  {
	int n(0);
	int res(0);
	ifstream fi("A-large.in");
	ofstream fo("output.txt");
	fi>>n;
	for (int i(0);i<n;++i)  {
		res=mysolve(fi);
		cout<<"Case #"<<i+1<<": ";
		fo  <<"Case #"<<i+1<<": ";
		switch(res)  {
		case 0: fo<<"X won\n"; break;
		case 1: fo<<"O won\n"; break;
		case 2: fo<<"Draw\n";  break;
		case 3: fo<<"Game has not completed\n"; break;
		}
	}
	cin>>n;
	return 0;
}
