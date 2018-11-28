#include <fstream>

using namespace std;

int main(){
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int t,it;
	fin>>t;
	for(it=0;it<t;++it){
		int i,n,minx,a,sum,xor;
		minx=10000000;
		sum=0;
		xor=0;
		fin>>n;
		for(i=0;i<n;++i){
			fin>>a;
			minx=min(minx,a);
			sum+=a;
			xor^=a;
		}

		fout<<"Case #"<<it+1<<": ";
		if(xor==0){
			fout<<sum-minx;
		}
		else{
			fout<<"NO";
		}
		fout<<endl;
	}
	return 0;
}