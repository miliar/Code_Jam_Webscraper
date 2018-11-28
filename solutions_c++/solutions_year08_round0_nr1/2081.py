#include <stdio.h>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

map <string,bool>my;
map <string,bool>go;

int main(void)
{
     char str[105];
	 char s[105];
	 freopen("A-large.in","r",stdin);
	 freopen("baoer.out","w",stdout);
	 int t,n,m,i,j,k,sign;
	 scanf("%d",&t);
	 for(k=1;k<=t;k++)
	 {
	     scanf("%d",&n);
		 gets(str);
		 my.clear();
		 go.clear();
		 for(i=0;i<n;i++)
		 {
		     gets(str);
			 if(my[str]==false)
			 my[str]=true;
		 }
		 sign=0;
		 scanf("%d",&m);
		 gets(str);
		 for(i=0;i<m;i++)
		 {
		     gets(str);
			 if(go[str]==false&&my[str]==true)
			 {
			    go[str]=true;
			 }
			 if(go.size()>=my.size())
			 {
			     sign++;
				 go.clear();
				 go[str]=true;
			 }
		 }
		 printf("Case #%d: %d\n",k,sign);
	 }
	 return 0;
}