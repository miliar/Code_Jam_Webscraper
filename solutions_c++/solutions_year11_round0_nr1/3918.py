#include <fstream>
#define forn(i,n) for(int i=0; i<(int)(n); i++)
using namespace std;

int main()
{
ifstream in("cj11a.in");
ofstream out("cj11a.out");

int T, N, k=0;
in>>T;

while(k<T)
{
	k++;
	char rob;
	char ultrob;
	int ulto=1, ultb=1, acum=0;
	int res=0;
	int pos;
	in>>N;
	in>>rob>>pos;
	res+=pos;
	ultrob=rob;
	if(rob=='O')ulto=pos;
	else ultb=pos;
	acum+=pos;
	
	forn(i,N-1)
	{
		in>>rob>>pos;
		if(rob==ultrob)
		{
			if(rob=='O'){res+=abs(pos-ulto)+1; acum+=abs(pos-ulto)+1; ulto=pos;}
			else {res+=abs(pos-ultb)+1; acum+=abs(pos-ultb)+1; ultb=pos;}
		}
		else
		{
			if(rob=='O')
			{
				res+=max(1, abs(pos-ulto)+1-acum);
				acum=max(1,abs(pos-ulto)+1-acum);
				ulto=pos;
			}
			else
			{
				res+=max(1, abs(pos-ultb)+1-acum);
				acum=max(1,abs(pos-ultb)+1-acum);
				ultb=pos;			
			}
		}
		ultrob=rob;
	}
	
	out<<"Case #"<<k<<": ";
	out<<res<<endl;
}
}
