#include<stdio.h>
#include<bitset>
using namespace std;
#define L 20
#define D 5005
#define N 505
int l,d,n;
char c[L];
short alfa[D][L];
bitset<405> pat;
inline void citire()
{
	scanf("%d%d%d\n",&l,&d,&n);
	for(int i=0; i<d; ++i)
	{
        	fgets(c,20,stdin);
		for(int j=0,aux=0; j<l; ++j,aux+=26)
			alfa[i][j]=c[j]-'a'+aux;	
	}
}
inline void rezolva()
{
	char c[500]={0};
	fgets(c,500,stdin);
	pat.reset();
	bool are=false;
	for(int i=0,j=0,aux=0; j<l; ++i)
	{
        	if(c[i]=='(')
		{
			are=true;
			continue;
		}
		if(c[i]==')')
		{
			aux+=26;
			++j;
			are=false;
			continue;
		}
		pat[c[i]-'a'+aux]=1;
	       // printf("aici %d -> char=%c   aux=%d\n",c[i]-'a'+aux,c[i],aux);
		if(are==false)
		{
			++j;
			aux+=26;
		}
	}

	int rez=0;
	bool ok;
	for(int i=0; i<d; ++i)
	{
		ok=true;
        	for(int j=0; j<l; ++j)
		{
                	if(pat[alfa[i][j]]==1)
				continue;
			ok=false;
			j=l;
		}
		if(ok)
			++rez;
	}
	printf("%d\n",rez);
}				
int main()
{
      	freopen("pa.in","r",stdin);
	freopen("pa.out","w",stdout);
       	citire();
	for(int i=1; i<=n; ++i)
	{
		printf("Case #%d: ",i);
		rezolva();
	}
	return 0;
}

