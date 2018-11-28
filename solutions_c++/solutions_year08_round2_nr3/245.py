#include <fstream>
using namespace std;
#define MAX 5000
int index[MAX];
void main()
{
	ifstream in ("input.in");
	ofstream out ("output.out");
	int n,CASE;
	in >> n;
	for(CASE=0;CASE<n;CASE++)
	{
		int k;
		in >> k;
		memset(index,0,sizeof(index));
		int i,pos=0,cnt=0;
		for(i=1;i<=k;)
		{
			if(index[pos]!=0)
			{
				pos++; if(pos==k) pos=0;
				continue;
			}
			if(cnt+1==i)
			{
				index[pos]=i;
				cnt=-1; i++;
			}
			pos++; cnt++;
			if(pos==k) pos=0;
		}
		out << "Case #" << CASE+1 << ": ";
		int t;
		in >> t;
		for(i=0;i<t;i++)
		{
			int d;
			in >> d;
			out << index[d-1] << ' ';
		}
		out << endl;
	}
	out.close();
	in.close();
}