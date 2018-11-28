#include <cstdio>
#include <cmath>
#include <map>
#include <string>
#define max(a,b) (((a)>(b))?(a):(b))
using namespace std;

int main()
{
	freopen("inp.txt", "r", stdin);
	freopen("outp.txt", "w", stdout);
	int c,t,d,n;
	char x[100][100], y[100][100], z[110];
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{		
		map< string, string > st, ht;
		scanf("%d", &c);
		for (int j=0;j<c;j++)
		{
			char ff[3];
			ff[1] = 0;
			scanf("%s", x[j]);
			ff[0]=x[j][2];
			x[j][2]=0;
			st[x[j]]=ff;
			x[j][2]=x[j][1];
			x[j][1]=x[j][0];
			x[j][0]=x[j][2];
			x[j][2]=0;
			st[x[j]]=ff;
		}
		scanf("%d", &d);
		for (int j=0;j<d;j++)
		{
			char ff[3];
			ff[1] = 0;
			scanf("%s", y[j]);
			ff[0]=y[j][2];
			y[j][2]=0;
			ht[y[j]]=ff;
			y[j][2]=y[j][1];
			y[j][1]=y[j][0];
			y[j][0]=y[j][2];
			y[j][2]=0;
			ht[y[j]]=ff;
		}
		scanf("%d %s", &n, z);
		string res = "";
		for (int j=0;j<n;j++)
		{
			res+=z[j];
			if (res.size()>=2)
			{
				if (st.find(res.substr(res.size()-2, 2))!=st.end())
					res = res.substr(0, res.size()-2)+st[res.substr(res.size()-2, 2)];
				else
				{
					for (int h=0;res.size()>0 && h<res.size()-1;h++)
					{
						char ff[3];
						ff[2]=0;
						ff[0]=res[h];
						ff[1]=res[res.size()-1];
						if (ht.find(ff)!=ht.end())
							res="";
					}
				}
			}
		}
		printf("Case #%d: [", i);
		for (int j=0;j<res.size();j++)
		{
			printf("%s", res.substr(j, 1).c_str());
			if (j+1<res.size())
				printf(", ");				
		}
		printf("]\n");
	}
	return 0;
}