#include <iostream>
#include <fstream>

using namespace std;
int n, l, h;
int a[10010];
bool ff;
int d;
int ans;


int main ()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("c.txt");
	int T;
	bool f;
	fin>>T; 
	for(int t=1; t<=T; ++t)
	{
		fin>>n>>l>>h;
		for(int i=0; i<n; ++i)
			fin>>a[i]; 
		f=false;
		if (l<=h){
		for(int i=l; i<=h; ++i)
		{
			ff=true;
			for(int j=0; j<n; ++j)
			{
				d=a[j];
				if (!((d/i)*i==d || (i/d)*d==i))
				{	
					ff=false; 
					//cout<<i<<j<<a[j]<<endl;
					break;
				}
			}
			if (ff){
				f=true;
				ans=i;
				break;	
			}
		}
		}
		
		fout<<"Case #"<<t<<": ";
		if (f)
		{
			fout<<ans<<endl;
		}
		else 
			fout<<"NO"<<endl;
	}
}	
