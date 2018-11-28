#include <fstream>
using namespace std;
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define fori(i,n) for(int i=0;i<n;i++)
long long answ;
int nom[256];
int t,ttt;
long long kol;
char str[70];
int main(){
	ifstream f("input.txt");
	ofstream f2("output.txt");
	f>>t;
	fori(i,t){
		for(int ff=0;ff<256;ff++){
			nom[ff]=0;
		}
		f>>str;
		kol=0;
		int j;
		for(j=0;str[j]>0;j++){
			if (!nom[str[j]]){
				nom[str[j]]=++kol;
			}
		}
		if (kol==1) kol=2;
		answ=0;
		fori(x,j){
			answ*=kol;
			ttt=nom[str[x]];
			if (ttt>2) answ+=ttt-1; else if (ttt==1) answ+=1;
		}
		f2<<"Case #"<<i+1<<": "<<answ<<endl;
	}
	f2.close();
	f.close();
	return 0;
}