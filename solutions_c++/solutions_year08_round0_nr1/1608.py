#include <iostream>
#include <map>
#include <string>
#include <stdlib.h>
using namespace std;

const int INF = 100000000;
const int MAX_EL = 1010;

map<string, int> mp;
int a[MAX_EL], b[MAX_EL];
char chrs[MAX_EL];
int els[MAX_EL];


string loadString()
{
    gets(chrs);
    string str(chrs);
	return str;
}

int main()
{
	int i, j, k, n, s, q;
	int z = 1;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	scanf("%d", &n);
	
	for(;n--;z++)
	{
		int res = 0;
		mp.clear();
		
		scanf("%d", &s);
		gets(chrs);
		for(i=0; i<s; i++)
		{
			string str = loadString();
			mp[str]=i;
		}
		
		scanf("%d", &q);
		gets(chrs);
		if(q != 0)
		{
			for(i=0; i<q; i++)
			{
				els[i] = mp[loadString()];
			}
		
			for(i=0; i<s; i++)
			{
			    a[i] = 0;
			}
			a[els[q-1]] = INF;
		
			for(k=q-2; k>=0; k--)
			{
				for(i=0; i<s; i++)
				{
					if(els[k] == i)
					{
						b[i] = INF;
					}
					else
					{
                    	int mn = INF;
                    
	                   	for(j=0; j<s; j++)
    	               	{
							int sum = a[j] + (i==j?0:1);
							if(mn > sum)
							{
								mn = sum;
							}
						}
                        b[i] = mn;
					}
				}
				for(i=0; i<s; i++)
			    a[i] = b[i];
			}
			
		   res = INF;
			for(i=0; i<s; i++)
			{
				if(res>a[i])
				    res = a[i];
			}
		}
		
		printf("Case #%d: %d\n", z, res);
		
	}
	
    return 0;
}
