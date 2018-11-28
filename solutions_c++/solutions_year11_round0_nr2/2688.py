#pragma warning(disable:4786)

#include <stdio.h>
#include <vector>
#include <string.h>

using namespace std;


int main()
{
	freopen("1.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int t, c, d, n, i, j, k, l;
	char str[105];
	vector<string> vc;
	vector<string> vo;
	string cstr;
	
	scanf("%d", &t);
	for(i=1; i<=t; i++)
	{
		vc.clear();
		vo.clear();
		cstr = "";

		scanf("%d", &c);
		for(j=0; j<c; j++) {
			scanf("%s", str);
			vc.push_back(str);
		}

		scanf("%d", &d);
		for(j=0; j<d; j++) {
			scanf("%s", str);
			vo.push_back(str);
		}

		scanf("%d %s", &n, str);
		cstr = str;

		for(j=1; j<cstr.length(); j++)
		{
			char a=cstr[j-1], b=cstr[j];
			for(k=0; k<vc.size(); k++)
			{
				if((a==vc[k][0] && b==vc[k][1]) ||
					(a==vc[k][1] && b==vc[k][0]) )
				{
					cstr[j-1]=vc[k][2];
					cstr.erase(&cstr[j], &cstr[j+1]);
					j=0;
					goto TT;
				}
			}

			for(k=j-1; k>=0; k--)
			{
				for(l=0; l<vo.size(); l++)
				{
					if((cstr[j]==vo[l][0] && cstr[k]==vo[l][1]) ||
						(cstr[j]==vo[l][1] && cstr[k]==vo[l][0]) )
					{
						cstr.erase(&cstr[0], &cstr[j+1]);
						j=0;
						goto TT;
					}
				}
			}
TT:;
		}		
		
		printf("Case #%d: [", i);
		if(cstr.length()==0)
		{
		}
		else if (cstr.length()==1)
		{
			printf("%c", cstr[0]);
		}
		else
		{
			for(j=0; j<cstr.length()-1; j++)
				printf("%c, ", cstr[j]);
			printf("%c", cstr[j]);
		}
		printf("]\n");		
	}
	
	return 0;
}