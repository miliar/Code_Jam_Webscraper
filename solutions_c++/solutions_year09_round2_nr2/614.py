#include <iostream> 
#include <algorithm> 
#include <string>
using namespace std; 

bool compare (char a[],char b[])
{
	int i;

	if (strlen(a)>strlen(b)) return true;
	else if (strlen(a)<strlen(b)) return false;
	else
	{
		for (i=0;i<strlen(a);i++)
		{
			if (a[i]<b[i]) return false;
			else if (a[i]>b[i]) return true;
		}
		if (i==strlen(a)) return false;
	}
	return true;

}
int main()
{
	freopen("B_small.in","r",stdin);
	freopen("tt.txt","w",stdout);
	int T,i,p;
	char str[40];
	char temp[40];
	scanf("%d",&T);
	for (int w=1;w<=T;w++)
	{
		scanf("%s",str);
		for (i=0;i<strlen(str);i++)
			temp[i] = str[i];
		temp[i] = '\0';
		next_permutation(str,str+strlen(str));
		char tt[40];
		for (i=0;i<strlen(str)&&str[i]=='0';i++);
		p = 0;
		for (;i<strlen(str);i++)
			tt[p++] = str[i];
		tt[p] = '\0';
		while (!compare(tt,temp))
		{
			str[0] = tt[0];
			str[1] = '0';
			p = 2;
			for (i=1;i<strlen(tt);i++)
				str[p++] = tt[i];
			for (i=0;i<p;i++)
				tt[i] = str[i];
			tt[i] = '\0';

		}
		printf("Case #%d: %s\n",w,tt);
	}
	return 0;
}
