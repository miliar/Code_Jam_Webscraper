#include <iostream>
#include <cstdlib>
#include <fstream>
#include <random>
#include <time.h>
#include <algorithm>

using namespace std;

char a[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char b[]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};

int main()
{
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int t;
	cin >> t;
	char ans[250];
	gets(ans);
	for (int i=0; i<t; i++)
	{
		gets(ans);
		for (int j=0; ans[j]!='\0'; j++)
		{
			for (int i=0; i<26; i++)
				if (b[i]==ans[j])
				{
					ans[j]=a[i];
					break;
				}
		}
		cout << "Case #" << i+1 << ": " << ans << endl;;
	}
}