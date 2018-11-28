#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int t, tc;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		int i;
		int c, d;
		char cc[32][32]={0, };
		bool op[32][32]={false, };
		char a[128];
		char ans[128]; int len=0;
		int cnt[32]={0, };
		fscanf(fp, "%d", &c);
		for(i=1;i<=c;i++)
		{
			char buf[8];
			fscanf(fp, "%s", buf);
			cc[buf[0]-'A'][buf[1]-'A']=cc[buf[1]-'A'][buf[0]-'A']=buf[2];
		}
		fscanf(fp, "%d", &d);
		for(i=1;i<=d;i++)
		{
			char buf[8];
			fscanf(fp, "%s", buf);
			op[buf[0]-'A'][buf[1]-'A']=op[buf[1]-'A'][buf[0]-'A']=true;
		}
		fscanf(fp, "%*d%s", a);
		for(i=0;a[i];i++)
		{
			if(!len){ans[len++]=a[i]; cnt[a[i]-'A']++;}
			else if(cc[ans[len-1]-'A'][a[i]-'A'])
			{
				cnt[ans[len-1]-'A']--;
				ans[len-1]=cc[ans[len-1]-'A'][a[i]-'A'];
				cnt[ans[len-1]-'A']++;
			}
			else
			{
				char j;
				for(j='A';j<='Z';j++)
				{
					if(cnt[j-'A'] && op[j-'A'][a[i]-'A']){len=0; memset(cnt, 0, sizeof(cnt)); break;}
				}
				if(j>'Z'){ans[len++]=a[i]; cnt[a[i]-'A']++;}
			}
		}
		fprintf(ofp, "Case #%d: [", t);
		for(i=0;i<len;i++) fprintf(ofp, "%s%c", i?", ":"", ans[i]);
		fprintf(ofp, "]\n");
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
