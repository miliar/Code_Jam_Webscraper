#include <fstream>
#include <string>

using namespace std;
ifstream fin("A-large.in");
ofstream fout("A-large.out");
const int MNAX=5000;

int main(){
	string s;
	int a[MNAX+2][22];
	int l,d,test,t,i,j;
	fin>>l>>d>>test;
	for (i=1;i<=d;++i){
		fin>>s;
		for (j=0;j<l;++j){
			a[i][j+1]=s[j]-'a'+1;
		}
	}

	for (t=1;t<=test;++t){
		int b[22][50];
		memset(b,0,sizeof(int)*50*22);
		int ans=0;
		fin>>s;int ii=0;
		for (j=0;j<l;++j){
			if (s[ii]!='('){
				b[j+1][s[ii]-'a'+1]=1;
				++ii;
			}
			else{
				++ii;
				while (s[ii]!=')'){
					b[j+1][s[ii]-'a'+1]=1;
					++ii;
				}
				++ii;
			}
		}
		for (i=1;i<=d;++i){
			j=1;
			while (j<=l && b[j][a[i][j]]==1) ++j;
			if (j==(l+1)) ++ans;
		}

		fout<<"Case #"<<t<<": "<<ans<<"\n";
	}
	return 0;
}