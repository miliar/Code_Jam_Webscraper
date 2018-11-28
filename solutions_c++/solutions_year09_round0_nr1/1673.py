#include<fstream>
using namespace std;

char S[5000][50], P[1000];
int main() {
	ifstream fin("A.in"); ofstream fout("A.out");
	int L,D,N,cnt=0;
	fin>>L>>D>>N;
	for(int i=0;i<D;++i)fin>>S[i];
	while(N--){
		fin>>P;
		int ans=0;
		for(int i=0;i<D;++i){
			int k=0,flag=1;
			for(int j=0;j<L&&flag;++j)
				if(P[k]!='(')flag=(P[k++]==S[i][j]);
				else {
					flag=0;
					for(++k;P[k]!=')';++k)
						flag|=(P[k]==S[i][j]);
					++k;
				}
			ans+=flag;
		}
		fout<<"Case #"<<++cnt<<": "<<ans<<endl;
	}
}
