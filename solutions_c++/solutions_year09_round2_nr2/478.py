#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

char s[100];

vector<char> a;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
	int t,i,cn=0;
	scanf("%d",&t);
	while (t--)
	{
		cn++;
		scanf("%s",s);
		int l= strlen(s);
		a.clear();
		for (i=0;i<l;i++)
		{
			a.push_back(s[i]);
		}
		bool ans = next_permutation(a.begin(),a.end());
		printf("Case #%d: ",cn);
		if (ans==false)
		{
			sort(a.begin(),a.end());
			
			int non0;
			for (i=0;i<a.size();i++)
			{
				if (a[i]!='0') 
				{
					non0=i;
					break;
				}
			}
			printf("%c0",a[non0]);
			for (i=0;i<a.size();i++)
			{
				if (i!=non0)
				{
					printf("%c",a[i]);
				}
			}
			printf("\n");
		}
		else
		{
			for (i=0;i<a.size();i++) printf("%c",a[i]);
			printf("\n");
		}
	}
}
