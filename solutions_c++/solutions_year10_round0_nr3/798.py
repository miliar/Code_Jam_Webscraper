#include <fstream>
#include <vector>
#define ll long long
using namespace std;
#define kols 1005
ll vc[kols];
int mass[kols];
ll shags[kols];
int main(){
	ifstream f("input.txt");
	ofstream f2("output.txt");
	int t;
	f>>t;
	t++;
	ll r,k,n,rez,sum,answ,tmp;
	for(int i=1;i!=t;i++){		
		f>>r>>k>>n;
		sum=0;
		for(int j=0;j!=n;j++){
			f>>vc[j];
			sum+=vc[j];
			mass[j]=-1;
		}		
		if (sum>k){
			int x=0;
			rez=0;
			int j;
			for(j=0;j!=r;j++){
				sum=0;
				while (sum+vc[x]<=k) {
					sum+=vc[x++];
					if(x==n) x=0;
				}
				if (mass[x]!=-1) {
					rez+=sum;
					shags[j]=rez;
					break;
				} else
				{
					rez+=sum;
					mass[x]=j;
					shags[j]=rez;
				}
			}			
			if (j!=r){
				tmp=r-j-1;
				tmp/=j-mass[x];
				answ=rez;
				answ+=(shags[j]-shags[mass[x]])*tmp;
				tmp*=j-mass[x];
				tmp=r-j-1-tmp;
				answ+=shags[tmp+mass[x]]-shags[mass[x]];
			} else answ=rez;
			f2<<"Case #"<<i<<": "<<answ<<endl;
		} else{
			f2<<"Case #"<<i<<": "<<sum*r<<endl;
		}
	}
	f.close();	
	f2.close();
	return 0;
}