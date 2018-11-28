#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream infile("B-large.in");
	ofstream outfile("output.txt");
	int t,s,p,n;
	int total;
	int ans;
	infile>>t;
	for (int i=0;i<t;i++)
	{
		ans=0;
		outfile<<"Case #"<<i+1<<": ";
		infile>>n>>s>>p;
		for (int j=0;j<n;j++)
		{
			infile>>total;
			if ((total>=3*p-2)) ans++;
			else if ((total>=3*p-4)&&(s>0)&&(p-2>=0)) 
			{
				ans++;
				s--;
			}
		}
		outfile<<ans<<endl;
	}
	infile.close();
	outfile.close();
	return 0;
}