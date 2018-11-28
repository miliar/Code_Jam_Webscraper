#include <iostream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>
#include <vector>
#include <set>

using namespace std;

char s[ 1 << 15 ];
int main()
{
   

	int z,zz;
	freopen("A-large.in","r",stdin);
	freopen("result.txt","w",stdout);

	
	for (scanf("%d",&zz),z=1;z<=zz;++z) 
    {
	    set<string> save;
		int i,n,m,ans;
		//save.clear();
		for (scanf("%d%d",&i,&m);i;--i)
	   {
			scanf("%s",s);
			save.insert(s);
		}
		char *p;
		for (ans=0;m;--m)
	    {
			scanf("%s",s);
			i=strlen(s);
			s[i]='/';
			s[++i]=0;
			for (p=s;;)
		    {
				p=strstr(p+1,"/");
				if (p==0) 
			    {
					break;
				}
				*p=0;
				if (save.find(s)==save.end()) {
					save.insert(s);
					++ans;
				}
				*p='/';
			}
		}

		printf("Case #%d: %d\n",z,ans);
	}
	return 0;




	

}