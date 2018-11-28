#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <fstream>
//#define fin cin
//#define fout cout
using namespace std;
const int maxn=1005;
ifstream fin("C-small.in");
ofstream fout("output.txt");
int Data[maxn];
bool M[maxn];
int main()
{
	int T,R,k,N,ans,Pt,sum;
	fin>>T;
	for(int i=1;i<=T;i++){
		fout<<"Case #"<<i<<": ";
		fin>>R>>k>>N;
		for(int j=0;j<N;j++)
			fin>>Data[j];
		Pt=0;
		ans=0;
		for(int j=0;j<R;j++){
			memset(M,0,sizeof(M));
			sum=0;
			while(!M[Pt]&&sum+Data[Pt]<=k){
				sum+=Data[Pt];
				M[Pt]=1;
				Pt=(Pt+1)%N;
			}
			//cout<<sum<<' ';
			ans+=sum;
		}
		fout<<ans<<endl;
	}
}
