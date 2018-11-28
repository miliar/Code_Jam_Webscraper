#include <cstdio>
#include <cstring>
#include <string>

using namespace std;
int a[20000];
char c[200][20], d[200][20], st[20000];
int T,I;
int cn,dn,n;

int main()
{
	scanf("%d",&T);
	for (I=1;I<=T;++I)
	{
		scanf("%d",&cn);
		for (int i=0;i<cn;++i)
			scanf("%s",&c[i]);
		scanf("%d",&dn);
		for (int i=0;i<dn;++i)
			scanf("%s",&d[i]);
		scanf("%d",&n);
		scanf("%s", st);

		string ans="";
		for (int i=0;i<strlen(st);++i)
		{
			char ch=st[i],chp=st[i];
						bool comb=false;
			if (ans!="")
			{
				chp=ans[ans.length()-1];

			for (int j=0;j<cn;++j)
				if (c[j][0]==ch && c[j][1]==chp || c[j][0]==chp && c[j][1]==ch)
				{
					ans[ans.length()-1]=c[j][2];
					comb=true;
					break;
				}
				}
			if (!comb) ans=ans+ch;
		//	puts(ans.c_str());
			for (int j=0;j<(int)ans.length()-1;++j)
			{
				bool f=true;
				char c1=ans[(int)ans.length()-1];
				char c2=ans[j];
				for (int k=0;k<dn;++k)
					if (c1==d[k][0] && c2==d[k][1] || c1==d[k][1] &&c2==d[k][0])
					{
						ans="";
						f=false;
						break;
					}
				if (!f) break;
			}
		}
		printf("Case #%d: [", I);
		for (int i=0;i<ans.length();++i)
			if (i==0) printf("%c", ans[i]);
		else printf(", %c", ans[i]);
		printf("]\n");
	}
	return 0;
}
			
