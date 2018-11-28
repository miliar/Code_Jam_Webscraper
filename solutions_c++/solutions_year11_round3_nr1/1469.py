#include <fstream>
#include <string.h>

using namespace std;

int main() {
	int __T;
	fstream r0("A-large.in",fstream::in);
	fstream w0("test.out",fstream::out);
	r0>>__T;
	for(int T=1;T<=__T;T++) {
		int r,c;
		r0>>r>>c;
		char a[50][50];
		int count=0;
		for(int i=0;i<r;i++) {
			while( r0.get()!='\n' );
			for(int j=0;j<c;j++) {
				a[i][j]=r0.get();
				if(a[i][j]=='#')
					count++;
			}
		}

		bool impo=false;
		if(count%4!=0)
			impo=true;

		for(int i=0;i<r;i++) {
			for(int j=0;j<c;j++) {
				if(impo) {
					i=r;
					break;
				}
				if(a[i][j]!='#')
					continue;
				if(i+1>=r || j+1>=c
					||a[i+1][j]!='#' || a[i][j+1]!='#'
					||a[i+1][j+1]!='#') {
					impo=true;
					continue;
				}
				a[i][j]=a[i+1][j+1]='/';
				a[i+1][j]=a[i][j+1]='\\';
			}
		}

		w0<<"Case #"<<T<<":\n";
		if(impo)
			w0<<"Impossible\n";
		else
			for(int i=0;i<r;i++) {
				for(int j=0;j<c;j++)
					w0<<a[i][j];
				w0<<endl;
			}
	}
}
