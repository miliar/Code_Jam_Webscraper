#include <cstdio>
#include <string>
#include <vector>
using namespace std;

vector <char > res;
char comb[50][3],l;
char del[50][2];
int C,D,H;

void wypisz(int test)
{
	printf("Case #%d: [",test);
	for(int i=0;i<res.size();i++)
		{printf("%c",res[i]);
		 if(i<res.size()-1)
			 printf(", ");
		}
	printf("]\n");
return;	
}

void pchaj(char l)
{
	bool ojciec_pchac=true;
	if(res.size()>=1)
	{
		for(int i=0;i<C;i++)
			if(((comb[i][0]==l)&&(comb[i][1]==res[res.size()-1]))||((comb[i][1]==l)&&(comb[i][0]==res[res.size()-1])))
			{res.pop_back();pchaj(comb[i][2]);ojciec_pchac=false;break;}
		if(ojciec_pchac)for(int i=0;i<D;i++)
			for(int j=0;j<res.size();j++)
			if(((del[i][0]==l)&&(del[i][1]==res[j]))||((del[i][1]==l)&&(del[i][0]==res[j])))
				{res.clear();return;}
	}	
	if(ojciec_pchac)
		res.push_back(l);
	return;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
	res.clear();
	scanf("%d",&C);
    for(int i=0;i<C;i++)
		scanf(" %c%c%c",&comb[i][0],&comb[i][1],&comb[i][2]);
	scanf(" %d",&D);
	for(int i=0;i<D;i++)
		scanf(" %c%c",&del[i][0],&del[i][1]);
    scanf(" %d ",&H);
	for(int i=0;i<H;i++)
	{
		scanf("%c",&l);
		pchaj(l);
	}
	wypisz(test);
}
}
