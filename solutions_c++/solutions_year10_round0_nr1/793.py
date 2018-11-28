#include <fstream>
#define ll long long
using namespace std;
ll mass[31];
int main(){
	ifstream f("input.txt");
	ofstream f2("output.txt");
	int t;
	f>>t;
	t++;
	ll n,k;
	k=1;
	for(n=0;n!=31;n++){
		mass[n]=k;
		k<<=1;
	}
	for(int i=1;i!=t;i++){
		f>>n>>k;
		if (k!=0){
			if ((k+1)%(mass[n])){
				f2<<"Case #"<<i<<": OFF"<<endl;
			} else f2<<"Case #"<<i<<": ON"<<endl;
		} else f2<<"Case #"<<i<<": OFF"<<endl;
	}
	f.close();	
	f2.close();
	return 0;
}