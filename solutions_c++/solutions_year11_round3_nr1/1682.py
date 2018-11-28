#include<fstream>
using namespace std;
ifstream fin("a.in");
ofstream fout("x.out");
int a[51][51],r,c,t,i,j,l;
char ch;
int main()
{
	fin>>t;
	for(i=1;i<=t;i++){
		fin>>r>>c;
		fout<<"Case #"<<i<<':';
		for(j=1;j<=r;j++)
			for(l=1;l<=c;l++){
				fin>>ch;
				if(ch=='#')a[j][l]=1;
				else a[j][l]=0;
			}
		int sw=1;
		for(j=1;j<=r&&sw==1;j++)
			for(l=1;l<=c&&sw==1;l++)
				if(a[j][l]==1){
					if(a[j][l+1]==1&&a[j+1][l]==1&&a[j+1][l+1]==1){
						a[j][l]=2;
						a[j][l+1]=3;
						a[j+1][l]=4;
						a[j+1][l+1]=5;
					}
					else {fout<<"\nImpossible\n";sw=0;}
				}
		if(sw==1){
			for(j=1;j<=r;j++){fout<<'\n';
				for(l=1;l<=c;l++)
					if(a[j][l]==0)fout<<'.';
					else if(a[j][l]==2)fout<<'/';
					else if(a[j][l]==3)fout<<'\\';
					else if(a[j][l]==4)fout<<'\\';
					else if(a[j][l]==5)fout<<'/';
			}
			fout<<'\n';
		}
	}
	fin.close();
	fout.close();
	return 0;
}