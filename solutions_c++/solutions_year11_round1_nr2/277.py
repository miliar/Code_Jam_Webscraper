#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int N = 100;
const int L = 10;
const int A = 26;

class Word
{
	public:
		int l;
		char w[L+1];
		int use[A];
		
		Word(const char *w)
		{
			for (int i=0;i<A;i++)
				use[i] = 0;
			strcpy(this->w, w);
			l = strlen(this->w);
			for (int i=0;i<l;i++)
				use[this->w[i]-'a']++;
			return;
		}
};

int main()
{
	int t, n, m;
	int point, pos;
	char get[A+1];
	Word *w[N];
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{
		scanf("%d%d", &n, &m);
		for (int j=0;j<n;j++)
		{
			scanf("%s", get);
			w[j] = new Word(get);
		}
		printf("Case #%d:", i);
		for (int j=0;j<m;j++)
		{
			scanf("%s", get);
			point = -1;
			pos = -1;
			for (int k=0;k<n;k++)
			{
				int nextP = 0, l = w[k]->l, reveal = 0;
				int exist[A] = {};
				for (int p=0;p<A && reveal<l;p++)
				{
					bool guess = false;
					for (int q=0;q<n;q++)
						if (w[q]->l==l && w[q]->use[get[p]-'a'])
						{
							bool tw = true;
							for (int r=0;r<A;r++)
								if (exist[r]==-1 && w[q]->use[r])
								{
									tw = false;
									break;
								}
								else if (exist[r]==1)
								{
									for (int s=0;s<l;s++)
										if ((w[k]->w[s]==r+'a' && w[q]->w[s]!=r+'a') || (w[k]->w[s]!=r+'a' && w[q]->w[s]==r+'a'))
										{
											tw = false;
											break;
										}
								}
							if (tw)
							{
								guess = true;
								break;
							}
						}
					if (guess)
					{
						if (w[k]->use[get[p]-'a'])
						{
							reveal += w[k]->use[get[p]-'a'];
							exist[get[p]-'a'] = 1;
						}
						else
						{
							nextP++;
							exist[get[p]-'a'] = -1;
						}
					}
				}
				if (nextP>point)
				{
					point = nextP;
					pos = k;
				}
			}
			printf(" %s", w[pos]->w);
		}
		printf("\n");
		for (int j=0;j<n;j++)
			delete w[j];
	}
	return 0;
}
