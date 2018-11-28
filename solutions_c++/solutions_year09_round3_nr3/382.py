#include <fstream>
using namespace std;
int t,p,q;
bool mass[200];
int mass2[10];
bool mass3[10];
int mn;
int coins=0;
void rec(int kol){
	if (kol==q) {
		if (coins<mn) mn=coins;
		return;
	}
	for(int i=0;i<q;i++){
		if (!mass3[i]){
			mass3[i]=true;
			mass[mass2[i]]=false;
			int tmp=0;
			int j=mass2[i]+1;
			while (mass[j++]){
				tmp++;
			}
			j=mass2[i]-1;
			while (mass[j--]){
				tmp++;
			}
			coins+=tmp;
			rec(kol+1);
			coins-=tmp;
			mass3[i]=false;
			mass[mass2[i]]=true;
		}
	}
}
int main(){
	ifstream f("input.txt");
	ofstream f2("output.txt");
	f>>t;
	mass[0]=false;
	for(int i=1;i<=t;i++){
		mn=2000000000;
		f>>p>>q;
		for(int j=1;j<=p;j++){
			mass[j]=true;
		}
		mass[p+1]=false;
		for(int j=0;j<q;j++){
			f>>mass2[j];
			mass3[j]=false;
		}
		rec(0);
		f2<<"Case #"<<i<<": "<<mn<<endl;
	}
	f.close();
	f2.close();
	return 0;
}