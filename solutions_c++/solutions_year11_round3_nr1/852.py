#include<iostream>
#include<map>
#include<vector>
#include<list>
#include<sstream>
#include<fstream>
#define fori(a,b,c) for(int a=b; a<c; a++)
using namespace std;

char grid[51][51]={0};
int r,c;

void prg(){
	fori(i,0,r){
		fori(j,0,c){
			cerr<<grid[i][j];
		}
		cerr<<endl;
	}
}

bool solve()
{
	fori(i,0,r){
		fori(j,0,c){
//			cerr<<"\tgrid["<<i<<"]["<<j<<"]: ";
			if(grid[i][j]=='#'){
				if(		i+1<r&&j+1<c
					&&	grid[i+1][j]=='#'
					&&	grid[i][j+1]=='#'
					&&	grid[i+1][j+1]=='#'
				){

					grid[i][j]='/';
					grid[i+1][j]='\\';
					grid[i][j+1]='\\';
					grid[i+1][j+1]='/';
				}
				else {
//					cerr<<"fails rect\n";prg();
					return false;
				}
			}
//			cerr<<"fails #\n";
		}
	}
	return true;
}

int main(int argc, char *argv[]){
//	cout.setf(ios::fixed,ios::floatfield);
//	cout.precision(6);
	int t;
//	istream& in = cin;ostream&out=cout;
	ifstream fin(argv[1]);istream& in=fin;ofstream fout("a.out");ostream&out = fout;
//	ostream&out=cout;istringstream in("3\n\
//2 3\n\
//###\n\
//###\n\
//1 1\n\
//.\n\
//4 5\n\
//.##..\n\
//.####\n\
//.####\n\
//.##..\n");
#define cin blahewlarujhesdofi
#define cout blahewlarujhesdofi
	in>>t;
	fori(i,0,t){
		in>>r>>c;
		
		fori(j,0,r)
			in>>grid[j];

		out<<"Case #"<<(i+1)<<":\n";

		if(!solve())
			out<<"Impossible"<<endl;
		else{
			fori(j,0,r)
				out<<grid[j]<<endl;
		}

	}
	system("PAUSE >void.out");
	return 0;
}
