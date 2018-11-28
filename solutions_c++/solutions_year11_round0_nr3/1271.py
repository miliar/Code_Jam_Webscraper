#include<fstream>
using namespace std;
ifstream fin("C-large.in");
ofstream fout("c-small.out");
int a[1001],n,i,t,mn,j,v[1001];
int main()
{
	fin>>t;
	for(j=1;j<=t;j++){
		fin>>n; mn=1000001; int s=0,s2=0;
		for(i=1;i<=n;i++){
			fin>>a[i];
			if(mn>a[i])mn=a[i];
			s+=a[i];
			s2^=a[i];
		}
		if(s2==0)v[j]=s-mn;
		else v[j]=-1;
	}
	for(j=1;j<=t;j++){
		if(v[j]!=-1)fout<<"Case #"<<j<<": "<<v[j];
		else fout<<"Case #"<<j<<": NO";
		fout<<'\n';
	}
	fin.close();
	fout.close();
	return 0;
}