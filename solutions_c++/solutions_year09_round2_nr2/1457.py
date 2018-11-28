#include<fstream>
#include<string.h>
#define dmax 200
using namespace std;
ifstream in("next.in");
ofstream out("next.out");
int n;
char sir[dmax];
int main()
{	int i,l,j;
	in>>n;
	for(i=0;i<=n;i++)
	{	in.getline(sir,dmax,'\n');
		if(i)
		{	l=strlen(sir);
			if(next_permutation(sir,sir+l))
				out<<"Case #"<<i<<": "<<sir<<'\n';
			else if(sir[0]=='0')
			{	while(sir[0]=='0')
					next_permutation(sir,sir+l);
				out<<"Case #"<<i<<": ";
				for(j=0;j<l;j++)
				{	if(j==1)
						out<<"0"<<sir[j];
					else out<<sir[j];
				}	
				out<<'\n';
			}	
			else 
			{	out<<"Case #"<<i<<": ";
				for(j=0;j<l;j++)
				{	if(j==1)
						out<<"0"<<sir[j];
					else out<<sir[j];
				}
				if(l==1)out<<"0";	
				out<<'\n';
			}	
		}	
	}
	in.close();
	out.close();
	return 0;
}	