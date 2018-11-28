#include<fstream>
#include<cmath>
using namespace std;
int n,c[1000],v;
bool crying(int s) {
	int i,a=0,b=0;
	v=0;
	for(i=0;i<n;i++)
		if (s&(1<<i)) {
			a^=c[i];
			v+=c[i];
			}
		else
			b^=c[i];
	return (!(a==b));
	}

int main() {
	ifstream fin("C.in");
	ofstream fout("C.out");
	int t,s,sm;
	int m,i,j,k;
	fin>>t;
	for(i=1;i<=t;i++) {
		fout<<"Case #"<<i<<": ";
		fin>>n;
		m=0;
		for(j=0;j<n;j++) 
			fin>>c[j];
		sm=1<<n;
		for(s=1;s<sm-1;s++) 
			if (!crying(s))
				m=max(m,v);
		if (m==0)
			fout<<"NO"<<endl;
		else
			fout<<m<<endl;
		}
	fin.close();
	fout.close();
	return 0;
	}
			
		
