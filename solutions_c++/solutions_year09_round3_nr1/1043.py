#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<math.h>   
#include<algorithm>
#include<vector>
#include<set>
#include<map>

using namespace std;
char a[66];
long long ans;

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i, j, tc;
	int cnt;
	int caseNum;
	double format;

	fscanf(fp, "%d", &caseNum);
	for(tc=1;tc<=caseNum;tc++)
	{
		if (tc==12)
			int alfd=tc;
		vector<char> vc;
		std::set<char> c;
		map<char,int> m;

		ans=0;
		memset(a,0,sizeof(a));

		fscanf(fp, "%s", a);

		//char max='0';
		for(i=0; a[i];i++)
		{
			c.insert(a[i]);
			vc.push_back(a[i]);
		}
		int j=1;
		for(i=0; a[i];i++)
		{
			if(m.count(a[i])==0)
			{
				m.insert(make_pair(a[i],j));
				if(j==1)
					j=0;
				else if(j==0)
					j=2;
				else
					j++;
			}


		}
		format=c.size();
		if(format==1)
			format=2;
		for(i=0; a[i];i++)
			;
		cnt=i--;

		cnt--;
		for(i=0; a[i];i++,cnt--)
		{
			ans+=m[a[i]]*pow(format,cnt);
		}
		//bool success=false;
		fprintf(ofp, "Case #%d: %d\n", tc, ans);
	}
	return 0;
}
