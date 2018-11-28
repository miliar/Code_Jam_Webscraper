#include <iostream>
#include <fstream>
using namespace std;

int R,K,n,g[1010],person[1010],end[1010];

int main()
{
	int i,j,st,en,t,t1,sum,ans;
	
	ifstream fin;
	ofstream fout;

	fin.open("input.txt");
	fout.open("output.txt");

	fin>>t;
	
	for(t1=1;t1<=t;t1++)
	{
		fin>>R>>K>>n;
		
		for(i=0;i<n;i++)
			fin>>g[i];

		for(st=0;st<n;st++)
		{
			for(en=(st+1)%n,sum=g[st]+g[en];sum<=K&&(en!=st);en=(en+1)%n,sum+=g[en]);
			sum-=g[en];
			en=(en+n-1)%n;
			person[st]=sum;
			end[st]=en;
		}
		
		ans=0;
		st=0;
		for(i=0;i<R;i++)
		{
			ans+=person[st];
			st=(end[st]+1)%n;
		}
		
		fout<<"Case #"<<t1<<": ";
		fout<<ans<<"\n";
		
	}
	fin.close();
	fout.close();

	return 0;
}