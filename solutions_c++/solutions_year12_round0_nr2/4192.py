#include<cstdio>
#include<cstdlib>

using namespace std;

int t,n,s,p;
int specdn,standn;
int tab[107];
int lstan, lspec;

int main()
{
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("%d %d %d",&n,&s,&p);
		printf("Case #%d: ",i+1);
			specdn=3*p-4;
			standn=3*p-2;
		if (p==1){ standn=1; specdn=1;}
		for(int j=0;j<n;j++){
			scanf("%d",&tab[j]);
			//printf("tab[j] = %d | 3*p = %d\n", tab[j], 3*p);
			if(tab[j]>=specdn){
				if(tab[j]>=standn)
					lstan++;
				else
					lspec++;
			}
		}
		int wyn;
		//printf("!!!!!!!!!!!! lspec = %d lstan = %d\n",lspec,lstan);
		if(lspec>=s)
			wyn=lstan+s;
		else
			wyn=lstan+lspec;
		printf("%d\n",wyn);
		lstan=0;
		lspec=0;
	}
	return 0;
}
