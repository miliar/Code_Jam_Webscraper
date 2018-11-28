#include<iostream>
#include<cstdio>
#include<memory.h>
#include<iostream>
using namespace std;

char p[3][256];
char q[3][256];
char s[256];
char a[256];
char str[256];
int main()
{
	freopen("A-small-attempt3.in","r",stdin);
	freopen("out.out","w",stdout);
    strcpy(p[0],"ejp mysljylc kd kxveddknmc re jsicpdrysi");
	strcpy(p[1],"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	strcpy(p[2],"de kr kd eoya kw aej tysr re ujdr lkgc jv");
	strcpy(q[0],"our language is impossible to understand");
	strcpy(q[1],"there are twenty six factorial possibilities");
 	strcpy(q[2],"so it is okay if you want to just give up");
	s['z'] = 'q';
	s['q'] = 'z';
	for(int i=0;i<3;i++)
	{
		int siz = strlen(p[i]);
		for(int j=0;j<siz;j++)
			s[p[i][j]] = q[i][j];
	}
    int T;
    scanf("%d",&T);
    gets(str);
    for(int i=0;i<T;i++)
    {
        gets(str);
        cout<<"Case #"<<i+1<<':'<<' ';
        for(int j=0;j<strlen(str);j++)
        cout<<s[str[j]];
        if(i!=T-1) cout<<endl;
    }
	return 0;
}


