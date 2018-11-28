#include<fstream>
#include<iomanip>
using namespace std;
ifstream fin("D-small-attempt0.in");
ofstream fout("d.out");
int t,n,i,j,v[1000],k,viz[1000];
double x;
int main()
{
	fin>>t;
	for(j=1;j<=t;j++){
		fin>>n;
		x=0;
		for(int l=1;l<=n;l++)viz[l]=0;
		for(i=1;i<=n;i++)fin>>v[i];
		for(int l=1;l<=n;l++){
			if(viz[l]==0&&v[l]!=l){
				int l2=l;
				k=1; viz[l2]=1;
				while(viz[v[l2]]==0){
					l2=v[l2];
					viz[l2]++;
					k++;
				}
				for(l2=k;l2>=2;l2--)x+=double(l2/(l2-1));
			}
		}
		fout<<fixed<<"Case #"<<setprecision(0)<<j<<": "<<setprecision(6)<<(double)x<<'\n';
	}
	fin.close();
	fout.close();
	return 0;
}