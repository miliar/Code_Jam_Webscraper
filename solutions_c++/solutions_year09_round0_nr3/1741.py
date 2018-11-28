#include<fstream>
using namespace std;
const char STR[]="welcome to code jam";
char S[600];
int f[600][19];
int main() {
	ifstream fin("C.in"); ofstream fout("C.out");
	int N,cnt=0;
	fin>>N;
	fin.getline(S,1000);
	while(N--){
		fin.getline(S,1000);
		int L=strlen(S), ans=0;
		memset(f,0,sizeof(f));
		for(int i=0;i<L;++i){
			f[i][0]=(S[i]==STR[0]);
			for(int j=1;j<19;++j)
				if(S[i]==STR[j])
					for(int k=0;k<i;++k) f[i][j]=(f[i][j]+f[k][j-1])%10000;
			ans=(ans+f[i][18])%10000;
		}
		fout<<"Case #"<<++cnt<<": ";
		fout.width(4); fout.fill('0'); fout<<ans<<endl;
	}
}
