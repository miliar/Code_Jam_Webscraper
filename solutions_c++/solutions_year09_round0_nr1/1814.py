#include <cstdio>
#include <cstdlib>
#include <vector>
#include <bitset>

using namespace std;

int main(void)
{
	int l, d, n;
	scanf("%d %d %d", &l, &d, &n);
	
	char words[d][20];
	for(int i=0;i<d;i++)
		scanf("%s\n", words[i]);
	
	for(int i=0;i<n;i++)
	{
		vector<bool> left(d, true);
		
		for(int j=0;j<l;j++)
		{
			char c = getchar();
			
			if (c != '(')
			{
				for(int k=0;k<d;k++)
					if (left[k])
						if (words[k][j] != c)
							left[k] = false;
			}
			else
			{
				vector<char> letters;
				
				while((c = getchar()) != ')')
					letters.push_back(c);
				
				for(int k=0;k<d;k++)
				{
					if (left[k])
					{
						bool found = false;
						for(int m=0;m<(int)letters.size();m++)
							if (words[k][j] == letters[m])
							{
								found = true;
								break;
							}
						
						left[k] = found;
					}
				}
			}
		}
		
		scanf("\n");
		
		int sum = 0;
		for(int j=0;j<(int)left.size();j++)
			if (left[j])
				sum++;
		
		printf("Case #%d: %d\n", i+1, sum);
	}
	
	return 0;
}