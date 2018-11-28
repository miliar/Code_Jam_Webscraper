#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main()
{
	int l, d, n;
	char words[5200][20];
	char term[500];
	bool in[5200];

//	freopen("in.txt", "r", stdin);

	while(scanf("%d %d %d", &l, &d, &n) != EOF)
	{
		for(int i=0; i<d; ++i)
		{
			scanf("%s", words[i]);
		}
	
		for(int i=0; i<n;++i)
		{
			scanf("%s", term);
			int c = 0, idx=0;
			bool ma[26];
			memset(in, true, sizeof(bool)*d);

			while(c < l)
			{
				if(term[idx] == '(')
				{	
					memset(ma, false, sizeof(bool)*26);
					++idx;
					while(term[idx] != ')')
					{
						ma[term[idx] - 'a'] = true;
						++idx;
					}
					for(int j=0; j<d; ++j)
					{
						in[j] = in[j] && ma[words[j][c]-'a'];
					}
				}
				else
				{
					for(int j=0; j<d; ++j)
					{
						if(term[idx] != words[j][c])
							in[j] = false;
					}
				}
				++idx;
				++c;
			}
			int count=0;
			for(int j=0;j<d;++j)
				if(in[j]) ++count;
			printf("Case #%d: %d\n", i+1, count);
		}
	}



	return 0;
}
