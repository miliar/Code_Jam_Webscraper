#include <set>
#include <string>
#include <cstring>
#include <cstdio>
#include <iostream>
using namespace std;

set <string> sstr;

int main ()
{
	FILE *fin=fopen ("File Fix-it.in","r");
	FILE *fout=fopen ("File Fix-it.out","w");
	
	int t,T;
	int n,m;
	char c[110];
	//string str;
	int i,j,sz;
	int ans,size;
	
	fscanf (fin,"%d",&T);
	
	for(t=1;t<=T;t++)
	{
		sstr.clear ();
		fscanf (fin,"%d %d",&n,&m);
		
		for(i=0;i<n;i++)
		{
			fscanf (fin," %s ",c);
			
			sz=strlen (c);
			for(j=1;j<sz;j++)
				if(c[j]=='/')
				{
					c[j]='\0';
					//str=c;
					sstr.insert (c);
					c[j]='/';
				}
			//str=c;
			sstr.insert (c);
		}
		
		size=sstr.size ();
		ans=0;
		
		for(i=0;i<m;i++)
		{
			fscanf (fin," %s ",c);

			sz=strlen (c);
			for(j=1;j<sz;j++)
				if(c[j]=='/')
				{
					c[j]='\0';
					//str=c;
					sstr.insert (c);
					if(size!=sstr.size ())
					{
						size++;
						ans++;
					}
					c[j]='/';
				}
			//str=c;
			sstr.insert (c);
			if(size!=sstr.size ())
			{
				size++;
				ans++;
			}
		}
		
		fprintf (fout,"Case #%d: %d\n",t,ans);
	}
	return 0;
}
