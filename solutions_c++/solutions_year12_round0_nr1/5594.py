#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <queue>
#define pb(x) push_back(x)
#define rep(i,x,y) for(i=x;i<y;i++)
#define geti(x) scanf("%d",&x)

using namespace std;

int main()
{
	char map[30] = "yhesocvxduiglbkrztnwjpfmaq";
	char str[150],res[150];
	int n,len,i,cases=1;
	geti(n);
	cin.getline(str,150);
	while(n--)
	{
	    cin.getline(str,150);
	    len = strlen(str);
	    for(i=0;i<len;i++)
	    {
	        if(str[i]==' ')
	        res[i] = ' ';
	        else
	        {
	           res[i] = map[str[i]-'a'];
	        }
	    }
	    res[i] = '\0';
	    printf("Case #%d: %s\n",cases,res);
	    cases++;
	}
	return 0;
}
