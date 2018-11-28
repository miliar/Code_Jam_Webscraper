/*
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
y,h,e,s,o,c,v,x,d,u,i,g,l,b,k,r,z,t,n,w,j,p,f,m,a,q

*/
#include <STRING>
#include <FSTREAM>
using namespace std;
char as[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
	int n,i,j;
	string cs;

	ifstream infile;
	ofstream outfile("out.txt",ios::out);
	infile.open("A-small-attempt1.in",ios::in);
	infile>>n;
	getline(infile,cs,'\n');
	for(i=0;i<n;i++)
	{
		getline(infile,cs,'\n');
		if (cs=="")
		{
			continue;
		}
		outfile<<"Case #"<<i+1<<": ";
		for(j=0;j<cs.length();j++)
		{
			if (cs[j]==' ')
			{
				outfile<<" ";
			}
			else
			{
				outfile<<as[cs[j]-'a'];
			}
		}
		outfile<<endl;
	
	}
	return 0;
}