#include <fstream>
#include <vector>

#define ll long long
using namespace std;
inline ll sabs(ll a) {return a<0?-a:a;}
inline ll nod(ll a, ll b){
	while((a!=0)&&(b!=0)){
		if(a>b) a%=b; else b%=a;
	}
	return a+b;
}
ll chisl[3];
int main(){
	ifstream f("input.txt");
	ofstream f2("output.txt");
	ll c,n,answ,tmp;
	f>>c;
	c++;
	for(int i=1;i!=c;i++){
		f>>n;
		for(int k=0;k!=n;k++){
			f>>chisl[k];
		}
		answ=sabs(chisl[n-2]-chisl[n-1]);
		for(int j=0;j!=n-2;j++){
			for(int h=j+1;h!=n;h++){
				tmp=sabs(chisl[j]-chisl[h]);
				answ=nod(tmp,answ);
			}
		}
		if (answ==1) f2<<"Case #"<<i<<": 0"<<endl; else 
		{
			if (chisl[0]%answ!=0)
			f2<<"Case #"<<i<<": "<<answ-chisl[0]%answ<<endl; else
			f2<<"Case #"<<i<<": 0"<<endl;
		}
	}
	f2.close();
	f.close();
	return 0;
}