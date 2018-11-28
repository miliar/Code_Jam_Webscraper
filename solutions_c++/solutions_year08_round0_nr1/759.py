#include <fstream>
using namespace std;
#define MAX 99999
int n;
void main()
{
	int i,j,k;
	ifstream in ("A-small.in");
	ofstream out ("output.out");
	in >> n;
	for(int CASE=0;CASE<n;CASE++)
	{
		int s,q;
		char engine[100][100];
		int query[1000];
		int d[100][1000]={0,};
		in >> s; in.getline(engine[0],10,'\n');
		for(i=0;i<s;i++)
		{
			in.getline(engine[i],100,'\n');
		}
		char a[100];
		in >> q; in.getline(a,100,'\n');
		for(i=0;i<q;i++)
		{
			in.getline(a,100,'\n');
			for(j=0;j<s;j++)
			{
				if(strlen(a)!=strlen(engine[j])) continue;
				for(k=0;k<strlen(a);k++)
				{
					if(a[k]!=engine[j][k]) break;
				}
				if(k>=strlen(a)) break;
			}
			query[i]=j;
		}
		/*
		for(i=1;i<q;i++)
		{
			int min=MAX;
			for(j=0;j<s;j++)
			{
				if(query[i]==j) continue;
				if(d[j][i-1]<min)
					min=d[j][i-1];
				if(d[j][i-1]>d[query[i]][i-1]+1)
					d[j][i]=d[query[i]][i-1]+1;
				else
					d[j][i]=d[j][i-1];
			}
			d[query[i]][i]=min+1;
		}
		int min=MAX;
		if(q==0) min=0;
		else
		{
			for(i=0;i<s;i++)
				if(d[i][q-1]<min)
					min=d[i][q-1];
		}
		*/

		int count=0;
		bool visit[100]={0,};
		for(i=0;i<q;i++)
		{
			visit[query[i]]=true;
			for(j=0;j<s && visit[j];j++);
			if(j==s)
			{
				count++;
				for(j=0;j<s;j++)
					visit[j]=false;
				visit[query[i]]=true;
			}
		}
		out << "Case #" << CASE+1 << ": " << count << endl;
	}
	out.close();
	in.close();
}