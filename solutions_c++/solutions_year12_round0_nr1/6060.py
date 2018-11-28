#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

char solve(char ch)
{
	string A="zqejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
	string B="qzourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
	
	for(int i=0;i<(int)A.length();i++)
		if(A[i]==ch)
			return B[i];
	return ' ';
	
}
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	string line;
	int n,ca=1;
	cin>>n;
	getline(cin,line);
	while(n--)
	{
		getline(cin,line);
		//cout<<line<<endl;
		
		cout<<"Case #"<<ca++<<": ";
		for(int i=0;i<(int)line.length();i++)
			cout<<solve(line[i]);
		cout<<endl;
		
	}
	return 0;
}
