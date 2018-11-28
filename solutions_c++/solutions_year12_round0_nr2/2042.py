#include<fstream>
using namespace std;

int get(int x)
{
	if(x%3==0)
		return x/3;
	if((x-1)%3==0)
		return (x-1)/3+1;
	return (x-2)/3+1;
}

int valid(int s, int n)
{
	int dif=s-n;
	
	int nr1=dif/2;
	int nr2=s-n-nr1;
	if(n-nr1<=2 && n-nr2<=2)
		return 1;
	return 0;
}

int main()
{
	int t;

	ifstream in("B.in");
	ofstream out("B.out");

	in>>t;
	for(int i=0;i<t;++i)
	{
		int n,s,p;
		in>>n>>s>>p;
		int nr,count=0;
		for(int j=0;j<n;++j)
		{
			in>>nr;
			int r=get(nr);
			if(r>=p)
				++count;
			else
			{
				if(r+1>=p && r+1<=nr && s>=1 && valid(nr,r+1))
				{
					--s;
					++count;
				}
			}
		}
		out<<"Case #"<<i+1<<": ";
		out<<count<<"\n";
	}
	in.close();
	out.close();
}
