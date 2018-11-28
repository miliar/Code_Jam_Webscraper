#include <fstream>

using namespace std;

const int NMAX=100;

int main(){
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int t,ti,mas[NMAX];
	fin>>t;
	for(ti=1;ti<=t;++ti){
		int i,ans;
		int n,l,h,il;
		bool fl;
		fl=false;

		fin>>n>>l>>h;
		for(i=0;i<n;++i){
			fin>>mas[i];
		}

		for(il=l;il<=h;++il){
			for(i=0;i<n;++i){
				if(il%mas[i]!=0&&mas[i]%il!=0){
					break;
				}
			}
			if(i<n){
				continue;
			}
			else{
				ans=il;
				fl=true;
				break;
			}
		}
		fout<<"Case #"<<ti<<": ";
		if(fl){
			fout<<ans<<endl;
		}
		else{
			fout<<"NO"<<endl;
		}
	}
	return 0;
}