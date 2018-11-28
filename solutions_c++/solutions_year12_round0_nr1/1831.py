#include <iostream>
#include <cstdio>
#include <cstring>
#define MOD 100000007
#define M 1026
using namespace std;

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	
	char ca[26][3]= {"ay","bh","ce","ds","eo","fc","gv","hx","id","ju","ki","lg","ml","nb","ok","pr","qz","rt","sn","tw","uj","vp","wf","xm","ya","zq"};

	int cas;
	scanf("%d",&cas);
	getchar();
	for(int i=1;i<=cas;i++)
	{
		char temp[300];
		gets(temp);
		int len=strlen(temp);
	        for(int j=0; j<len; j++)
	        {
	            if(temp[j] != ' ')
	            {
	                temp[j] = ca[temp[j]-'a'][1];
	            }
	        }
		printf("Case #%d: ",i);
		printf("%s\n",temp);
	}
	return 0;
}
