#include <string>
#include <cstdio>
#include <set>

using namespace std;

int main(void)
{
	int T;
	scanf("%d", &T);
	for(int caseN=1;caseN<=T;caseN++)
	{
		int a, b;
		scanf("%d %d", &a, &b);
		int ans=0;
		for(int i=a;i<=b;i++)
		{
			char temp[10];
			sprintf(temp, "%d", i);
			string base=temp;

			set <int> isExist;

			for(int j=1;j<base.size();j++)
			{
				if(base[j]=='0') continue;
				string tar = base.substr(j) + base.substr(0, j);
				int rotated;
				sscanf(tar.c_str(), "%d", &rotated);
				if(rotated>i && rotated <= b && !isExist.count(rotated)) 
				{
					isExist.insert(rotated);
					ans++;
				}
			}
		}

		printf("Case #%d: %d\n", caseN, ans);
	}

	return 0;
}
