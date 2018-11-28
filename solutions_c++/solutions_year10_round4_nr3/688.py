#include <iostream>
#include <fstream>
#include <list>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream fin("C-small-attempt3.in");
	ofstream fout("C-small-attempt3.out");
	int cc;
	fin>>cc;
	const int mucho=10000;
	int cb;
	char **m=new char*[mucho];
	for (int i=0;i<mucho;i++)
		m[i]=new char[mucho];
	list<int> px,py;
	list<int>::iterator ix1,ix2,iy1,iy2;
	for (int cn=0;cn<cc;cn++) {
		cerr<<cn<<endl;
		px.clear();
		py.clear();
		for (int i=0;i<mucho;i++)
			memset(m[i],0,mucho);
		int r,x1,x2,y1,y2;
		fin>>r;
		for (int k=0;k<r;k++) {
			fin>>x1>>y1>>x2>>y2;
			for (int i=x1;i<=x2;i++)
				for (int j=y1;j<=y2;j++) {
					if (m[j+1][i+1]==0) {
						m[j+1][i+1]=1;
						px.push_back(j+1);
						py.push_back(i+1);
					}
				}
		}
		
		
		int res=0;
		char a,b;
		int x,y;
		while (px.size()) {
			
//			for (int i=0;i<mucho;i++) {
//				for (int j=0;j<mucho;j++) {
//					cout<<char(m[i][j]+'0');
//				}
//				cout<<endl;
//			}
//				cout<<endl;
			
			
			res++;
			ix1=px.begin(); iy1=py.begin();
			while (ix1!=px.end()) {
				x=*ix1; y=*iy1;
				if (!m[x-1][y] && !m[x][y-1]) {
					m[x][y]=2;
				}
				ix1++;iy1++;
			}
			
			ix1=px.begin(); iy1=py.begin();
			while (ix1!=px.end()) {
				x=*ix1; y=*iy1;
				if (
					(m[x+1][y]==0) &&
					(m[x][y]==1 || m[x][y]==2) &&
					(m[x+1][y-1]==1 || m[x+1][y-1]==2) ) {
						px.push_back(x+1);
						py.push_back(y);
						if (x+1==mucho) cout<<"MUUCHO\n";
						m[x+1][y]=3;
					}
				ix1++;iy1++;
			}
			
			ix1=px.begin(); iy1=py.begin();
			while (ix1!=px.end()) {
				x=*ix1; y=*iy1;
				if (m[x][y]==2) {
					m[x][y]=0;
					ix1=px.erase(ix1);
					iy1=py.erase(iy1);
				} else if (m[x][y]==3) {
					m[x][y]=1;
					ix1++;iy1++;
				} else {
					ix1++;iy1++;
				}
			}
			
			
		}
		
		fout<<"Case #"<<cn+1<<": "<<res<<endl;
	}
	fout.close();
	fin.close();
}
