//

#include<vector>
#include<utility>
#include<cstring>
#include<iostream>
#include<algorithm>

using namespace std;

char com[200][200];
char opp[200][200];

char res[200];

int main() {
     freopen("test.in","r",stdin);
	 freopen("test.out","w",stdout);

	 int ca,c,d,n,i,j,last,tmp;
	 char str[10];
	 scanf("%d",&ca);
	 for(i=1;i<=ca;++i) {
		 memset(com,0,sizeof(com));
		 memset(opp,0,sizeof(opp));

		 scanf("%d",&c);
		 while( c-- ) {
			 scanf("%s",str);
			 com[str[0]][str[1]]=com[str[1]][str[0]]=str[2];
		 }

		 scanf("%d",&d);
		 while( d-- ) {
			 scanf("%s",str);
			 opp[str[0]][str[1]]=opp[str[1]][str[0]]=1;
		 }

		 scanf("%d%c",&n,&res[0]);
		 last=0;
		 while( n-- ) {
			 scanf("%c",&res[last++]);

			 if( last==1 ) continue;

			 if( com[res[last-1]][res[last-2]]!=0 ) {
				 res[last-2]=com[res[last-1]][res[last-2]];
				 --last;
			 }

			 tmp=last-2;
			 while( tmp>=0 ) {
				 if( opp[res[last-1]][res[tmp]]!=0 ) {
					 last=0;
					 break;
				 }
				 
				 --tmp;
			 }
		 }

		 printf("Case #%d: [",i);
		 for(j=0;j<last-1;++j) printf("%c, ",res[j]);
		 if( last!=0 ) printf("%c",res[last-1]);
		 printf("]\n");
	 }








		 
     
     return 0;
}