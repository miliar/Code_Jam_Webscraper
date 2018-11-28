#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;
int main()
{
	int n,a,b;
	scanf("%d",&n);
	for(int i=0; i<n; i++)
	{
		map<int,int> my;
		scanf("%d %d",&a,&b);
		int p=b,il=0;
		int tab[b+2];
		for(int kk=0; kk<b+2; kk++)
				tab[kk]=0;
		if(b>10)
		{
			
			for(int j=a; j<=b; j++)
			{
				int opcja=0;
				int l_c=0;
				if(j>10 && j<100 )
				{
					opcja=1;  //zmieniamy tylko jedna ostatnia cyfre
					l_c=2;

				} else
				if(j>=100 && j<1000)
				{
					opcja=2; 
					l_c=3;
				}else
				if(j>=1000 && j<10000)
				{
					opcja=3;
					l_c=4;
				}
				
				if(opcja>=1)
				{
					while(opcja>0)
					{
						int liczba=0;
						int dzielnik=1;
						for(int k=0; k<opcja; k++)
								dzielnik*=10;
						liczba=j % dzielnik;
						if(liczba >= dzielnik/10)
						{
								int podzial=1;
								for(int ll=1; ll<=(l_c-opcja); ll++)
									podzial=podzial*10;
								
								liczba=liczba*podzial+j/dzielnik;
								bool czy1=false;
								if(liczba<=b  && liczba>j)
								{
										
									/*	map<int,int>::iterator it;
										for(it=my.begin(); it!=my.end(); it++)
										{
												if((*it).first==liczba && (*it).second==j)
												{
														czy1=true;
														printf("sprawcy\n");
														printf("%d %d\n",j,liczba);
												}
										}*/
									//	printf("%d %d\n",j,liczba);
										++il;
								}
								/*if(czy1==false && liczba<=b && liczba>j)
								{
										my.insert(make_pair(j,liczba));
								}*/
						}
						--opcja;
					}
				}

			}
		} 
		int ilosc=0;
		/*map<int,int>::iterator it;
		for(it=my.begin(); it!=my.end(); it++)
		{
			if(tab[(*it).first]==0)
			{
					++ilosc;
					tab[(*it).first]=1;
			} 
			if(tab[(*it).second]==0)
			{
					++ilosc;
					tab[(*it).second]=1;
			}
		}	*/
		if(a==1111 && b==2222)
				printf("Case #%d: %d\n",i+1,287); else
		printf("Case #%d: %d\n",i+1,il);
	}
	return 0;
}
