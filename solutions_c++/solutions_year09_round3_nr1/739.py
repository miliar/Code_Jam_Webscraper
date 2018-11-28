#include <fstream>
#include <string>
#include <math.h>

using namespace std;
ifstream fin("A-large.in");
ofstream fout("A-large.out");
//ifstream fin("input.txt");
//ofstream fout("output.txt");
const int MNAX=100;

long long step(long long a,int b){
	long long res=1;
	for (int i=1;i<=b;++i){
		res*=a;
	}
	return res;
}


int main(){
	int test,t,i,j;
	fin>>test;

	for (t=1;t<=test;++t){
		long long ans=0;
		string s="";
		long long a[MNAX+2];
		for (i=0;i<=MNAX;++i){a[i]=-1;}
		fin>>s;
		int l = s.length();
		int kol=1;
		for (i=0;i<l;++i){
			if (a[i]==-1){
				for (j=i;j<l;++j){
					if (s[j]==s[i]){
						a[j]=kol;
					}
				}
				if (kol==1){kol=0;}
				else if (kol==0){kol=2;}
				else{++kol;}
			}
		}
		if (kol==0 || kol==1){kol=2;}
		for (i=0;i<l;++i){
			ans+=a[i]*step(kol,l-i-1);
		}
		
		fout<<"Case #"<<t<<": "<<ans<<"\n";
	}
	return 0;
}