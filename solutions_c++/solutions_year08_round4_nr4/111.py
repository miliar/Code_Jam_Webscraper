#include <fstream>
using namespace std;
int k; char s[1001]; int p[5];
bool visit[5];
int size,minimum;
void rec(int depth)
{
	int i,j;
	char cpr[1001]={0,};
	if(depth==k)
	{
		for(i=0;i<strlen(s);i+=k)
		{
			for(j=0;j<k;j++)
			{
				cpr[i+j]=s[i+p[j]];
			}
		}
		char before=cpr[0];
		size=1;
		for(i=1;i<strlen(cpr);i++)
		{
			if(before!=cpr[i])
			{
				size++;
			}
			before=cpr[i];
		}
		if(size<minimum) minimum=size;
		return;
	}
	for(i=0;i<k;i++)
	{
		if(visit[i]) continue;
		visit[i]=true;
		p[depth]=i;
		rec(depth+1);
		visit[i]=false;
	}
}
void main()
{
	int n,CASE;
	ifstream in ("input.in");
	ofstream out ("output.out");
	in >> n;
	for(CASE=0;CASE<n;CASE++)
	{
		int ans;
		in >> k >> s;
		minimum=999999;
		memset(visit,0,sizeof(visit));
		rec(0);
		ans=minimum;
		out << "Case #" << CASE+1 << ": " << ans << endl;
	}
	out.close();
	in.close();
}