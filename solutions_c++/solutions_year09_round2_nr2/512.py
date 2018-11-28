//Jakub Sygnowski
#include <cstdio>
#include <string>
#include <cstdlib>
#include <algorithm>
#define REP(I,N) for(int I=0;I<(N);I++)
using namespace std;
int t,best,gdzie;
char tab[1000];
string lic;

void change(int ind){
	best=10+'0';
	for(int i=ind+1;i<lic.size();i++){
		if (lic[i]<best&&lic[i]>lic[ind]){
			best=lic[i];
			gdzie=i;
		}
	}
	swap(lic[ind],lic[gdzie]);
	sort(lic.begin()+ind+1,lic.end());
/*	for(int i=lic.size()-1;i>ind+1;i--)
		swap(lic[i],lic[i-1]);*/
}
int main(){
	scanf("%s",tab);
	t=atoi(tab);
	REP(nr,t){
		scanf("%s",tab);
		lic=tab;
		lic.insert(lic.begin(),'0');
		lic.insert(lic.begin(),'0');
		lic.insert(lic.begin(),'0');
		for(int i=lic.size();i>0;i--){
			if (lic[i]>lic[i-1]){
				change(i-1);
				break;
			}
		}
		while(lic[0]=='0') lic.erase(lic.begin());
		printf("Case #%d: %s\n",nr+1,lic.c_str());
	}
}
