#include <fstream>
using namespace std;
int prime[168],group[1000],d[168][1000];
bool visit[1000];
void main()
{
	ifstream fp("prime.txt");
	for(int pcnt=0;pcnt<168;pcnt++)
		fp >> prime[pcnt];
	fp.close();
	ifstream in ("input.in");
	ofstream out ("output.out");
	int n,CASE;
	in >> n;
	for(CASE=0;CASE<n;CASE++)
	{
		memset(visit,0,sizeof(visit));
		int a,b,p;
		int answer=0;
		int i,j;
		in >> a >> b >> p;
		for(i=a;i<=b;i++)
			group[i-a]=i-a;
		for(j=0;j<168 && prime[j]<=b-a;j++)
		{
			if(prime[j]<p) continue;
			for(i=a;i<b;i++)
			{
				if(i%prime[j]!=0) continue;
				for(int k=i+2;k<=b;k++)
				{
					if(k%prime[j]==0 && group[i-a]!=group[k-a])
					{
						for(int l=a;l<=b;l++)
						{
							if(l==k) continue;
							if(group[l-a]==group[k-a]) group[l-a]=group[i-a];
						}
						group[k-a]=group[i-a];
					}
				}
			}
		}
		for(i=a;i<=b;i++)
			visit[group[i-a]]=true;
		for(i=a;i<=b;i++)
			if(visit[i-a])
				answer++;
		out << "Case #" << CASE+1 << ": " << answer << endl;
	}
	out.close();
	in.close();
}