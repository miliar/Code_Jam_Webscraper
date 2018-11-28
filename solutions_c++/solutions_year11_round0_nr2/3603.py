#include <cstdio>
#include <cstring>
#include <fstream.h>
#include <iostream>
#define INF 999999999

ifstream f("in.in");
ofstream g("out.txt");
using namespace std;
int last[200];
string s;
char cod[]={'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};

int main()
{
	int n,i,j,c,d,t,it,o;
	
	char gr[50][5],op[50][4];
//	freopen("in","r",stdin);
	freopen("out.txt","w",stdout);
	f>>t;
	for (it=1;it<=t;++it)
	{
		
		f>>c;
		for (i=1;i<=c;++i)
			f>>gr[i];
		f>>o;
		for (i=1;i<=o;++i)
			f>>op[i];
		f>>n;
		f>>s;
		d=-1;
		for (j=0;j<8;++j) last[cod[j]]=0;
		for (i=0;i<n;++i)
			{
				int p=d+1,ok=0,mi=INF;
				s[d+1]=s[i];
				if (p>0)
					for (j=1;j<=c;++j)
							if ((gr[j][0]==s[p]) && (gr[j][1]==s[p-1]))
								--last[s[d]],ok=1,s[d]=gr[j][2],j=c,p=d; else
									if ((gr[j][1]==s[p]) && (gr[j][0]==s[p-1]))
										--last[s[d]],ok=1,s[d]=gr[j][2],j=c,p=d;
				if ((p>0) && (!ok))
					for (mi=INF,j=1;j<=o;++j)
					if ((op[j][0]==s[p]) && (last[op[j][1]]))
						{mi=0;break;} else
							if ((op[j][1]==s[p]) && (last[op[j][0]]))
								{mi=0;break;}
				if (!mi)
					{ok=1,d=-1;
					for (j=0;j<8;++j) 
						last[cod[j]]=0;
					}	
				if (!ok) ++d;	
				if (d>=0)	
				++last[s[d]];
			}
		g<<"Case #"<<it<<": [";
		for(i=0;i<d;++i)
			g<<s[i]<<", ";
		if (d>=0)
		g<<s[d]<<"]\n"; else
			g<<"]\n";
		
	}
	return 0;
}
	