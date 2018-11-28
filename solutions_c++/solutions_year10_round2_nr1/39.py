#include <stdio.h>
#include <string>
#include <set>
using namespace std;

main(){
	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		int m,n;
		int i,j,k,l;
		scanf("%d%d ",&n,&m);
		set<string> dirs;
		dirs.insert(string("/"));
		int siz0,siz1;
		for(i=0;i<n+m;i++){
			if(i==n)siz0=dirs.size();
			char buf[300];
			gets(buf);
			while(buf[strlen(buf)-1]<32)buf[strlen(buf)-1]='\0';
			l=strlen(buf);
			buf[l]='/';buf[l+1]='\0';
			l++;
			//printf("%s\n",buf);
			string str;
			for(j=0;j<l;j++){
				str=str+buf[j];
				if(buf[j]=='/'){dirs.insert(str);}//printf("%s\n",str.c_str());}
			}
		}
		siz1=dirs.size();
		printf("Case #%d: %d\n",t,siz1-siz0);
	}
}