#include<stdio.h>
char trans[128];
char a1[100]="our language is impossible to understand";
char a2[]="there are twenty six factorial possibilities";
char a3[]="so it is okay if you want to just give up";
char b1[]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
char b2[]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char b3[]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
main()
{
	int i,j,t;
	for(i=0;i<128;i++) trans[i]=0;
	trans['q']='z';
	trans['z']='q';
	for(i=0;b1[i];i++) trans[b1[i]]=a1[i];
	for(i=0;b2[i];i++) trans[b2[i]]=a2[i];
	for(i=0;b3[i];i++) trans[b3[i]]=a3[i];
	scanf("%d",&t);
	gets(a1);
	for(j=1;j<=t;j++)
	{
		gets(a1);
		printf("Case #%d: ",j);
		for(i=0;a1[i];i++) putchar(trans[a1[i]]);
		putchar('\n');
	}
}
