#include<stdio.h>
#include<string.h>
#include<iostream.h>
int main()
{
	int n;
	cin>>n;
	char a[100][100]={"","","","",""},b[1000][100]={"","","","",""},cur[100]="";
	int flag[100],count,loc,maxl;
	int i,s,q,k,j;
	for(i=1;i<=n;i++)
	{
		count=loc=0;
		cin>>s;scanf("\n");
		for(k=0;k<s;k++)
		       cin.getline(a[k],100);
		cin>>q;scanf("\n");
		for(k=0;k<q;k++)
			cin.getline(b[k],100);
	  label:for(k=0;k<s;k++) flag[k]=1001;
		for(j=0;j<s;j++)
		     for(k=loc;k<q;k++)
			if(!strcmp(a[j],b[k])) { flag[j]=k; k=q;}
		maxl=0;
		for(j=1;j<s;j++)
		if(flag[maxl]<flag[j]) maxl=j;
		strcpy(cur,a[maxl]);
		for(k=loc;k<q;k++)
			if(!strcmp(cur,b[k]))
			{
				loc=k;
				count++;
				goto label;
			}
		cout<<"Case #"<<i<<": "<<count<<"\n";
	}
	return 0;
}
