#include<fstream>
using namespace std;
ifstream fin("A-small-attempt2.in");
ofstream fout("a-out.out");
int p1,p2,n,i,j,sw,t,x1,x2;
int main()
{	
	fin>>t;
	for(i=1;i<=t;i++){
		fin>>n>>p1>>p2; x1=x2=100;
		for(j=2;j<=100;j++){
			while(x1%j==0&&p1%j==0){
				x1/=j;
				p1/=j;
			}
			while(x2%j==0&&p2%j==0){
				x2/=j;
				p2/=j;
			}
		}
		if(x1>n)fout<<"Case #"<<i<<": Broken\n";
		else if(p2==0&&p1!=0)fout<<"Case #"<<i<<": Broken\n";
		else if(p1==0&&p2!=0&&x2==1)fout<<"Case #"<<i<<": Broken\n";
		else if(x2==1&&x1!=1)fout<<"Case #"<<i<<": Broken\n";
		else fout<<"Case #"<<i<<": Possible\n";
	}
	fin.close();
	fout.close();
	return 0;
}