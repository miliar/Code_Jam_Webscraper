#include<fstream>
#include<iomanip>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("a.out");
int t,i,j,n,a[101][102];
char c;
double wp[101],owp[101],oowp[101];
int main()
{
	fin>>t;
	for(i=1;i<=t;i++){
		fin>>n;
		for(j=1;j<=n;j++){
			int k=0,x=0;
			for(int l=1;l<=n;l++)
			{
				fin>>c; 
				if(c=='1'){
					k++;
					x++;
					a[j][l]=1;
				}
				else if(c=='0'){x++;a[j][l]=0;}
				else a[j][l]=-1;
			}
			wp[j]=(double)k/x;
			a[j][0]=x;
			a[j][101]=k;
		}
		for(j=1;j<=n;j++){
			owp[j]=0;
			for(int l=1;l<=n;l++)
				if(a[j][l]==1)owp[j]+=(double)a[l][101]/(a[l][0]-1);
				else if(a[j][l]==0)owp[j]+=(double)(a[l][101]-1)/(a[l][0]-1);
			owp[j]=(double)owp[j]/a[j][0];
		}
		for(j=1;j<=n;j++){
			oowp[j]=0;
			for(int l=1;l<=n;l++)
				if(a[j][l]!=-1)oowp[j]+=owp[l];
			oowp[j]=(double)oowp[j]/a[j][0];}
		fout<<"Case #"<<i<<":\n";
		for(j=1;j<=n;j++)fout<<fixed<<setprecision(6)<<(double)0.25*wp[j]+0.5*owp[j]+0.25*oowp[j]<<'\n';
	}
	fin.close();
	fout.close();
	return 0;
}