#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream in;
	ofstream out;
	int t,r,k,n,*m,s,ds,dx;
	in.open("C-small-attempt3.in");
    out.open("COUT.TXT");
	in >> t;
	for(int i=1;i<=t;i++){
		in >> r;
		in >> k;
		in >> n;
		m=new int [n];
		for(int j=0;j<n;j++)
			in >> m[j];
		s=0;
		for(int j=0;j<r;j++){
			ds=0;
			for(int x=0;x<n;x++){
				if((ds+m[x])<=k){
					ds+=m[x];
					dx=x;
				}
				else x=n;
			}
			s+=ds;
			int *g=new int [dx+1];
			for(int x=0;x<=dx;x++)
				g[x]=m[x];
			for(int x=0;x<n-dx-1;x++)
				m[x]=m[x+dx+1];
			for(int x=0;x<=dx;x++)
				m[n-dx-1+x]=g[x];
		}
		out << "Case #" << i << ": " << s << endl;
	}
	in.close();
    out.close();
	return 0;
}