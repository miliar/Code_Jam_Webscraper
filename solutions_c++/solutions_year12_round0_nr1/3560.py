#include<cstdio>
#include<map>
#include<algorithm>
using namespace std;
map<char,char> M;
char x[]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
char xt[]="our language is impossible to understand";
char y[]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char yt[]="there are twenty six factorial possibilities";
char z[]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
char zt[]="so it is okay if you want to just give up";
const int MAX=110;
char s[MAX];
int main()
{
	int i;
	for(i=0;i<sizeof(x);i++)
	{
		if(M.count(x[i])==0)
		M[x[i]]=xt[i]; 
		else {
			if(M[x[i]]!=xt[i])
				printf("conflict :%c:%c\n",x[i],xt[i]);
		}
	}

	for(i=0;i<sizeof(y);i++)
	{
		if(M.count(y[i])==0)
		M[y[i]]=yt[i]; 
		else {
			if(M[y[i]]!=yt[i])
				printf("conflict :%c:%c\n",y[i],yt[i]);
		}
	}

	for(i=0;i<sizeof(z);i++)
	{
		if(M.count(z[i])==0)
		M[z[i]]=zt[i]; 
		else {
			if(M[z[i]]!=zt[i])
				printf("conflict :%c:%c\n",z[i],zt[i]);
		}
	}
	M['z']='q';
	M['q']='z';

	/*
	for(i='a';i<='z';i++) {
		printf("%c:%c\n",i,M[i]);
	}
	*/
	int no,j;
	fgets(s,MAX,stdin);
	sscanf(s,"%d",&no);
	for(i=1;i<=no;i++)
	{
		printf("Case #%d: ",i);
		fgets(s,MAX,stdin);
		for(j=0;s[j] && (s[j]!='\n');j++)
		{
			if(M.count(s[j]))
				printf("%c",M[s[j]]);
			else printf("%c",s[j]);
		}
		printf("\n");
	}
	

	return 0;
}
