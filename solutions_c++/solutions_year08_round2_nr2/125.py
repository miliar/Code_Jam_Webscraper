#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("output.txt");
ifstream fin("input.txt");


int dolis[1000000];
bool isp[1000000];
bool done[1000001];
vector <long long> plis;
bool pdone[1000000];

int divs[100001][15];
int divsz[100001];

void init(void)
{
	int i,j;
	for(i=2; i<1000000; i++)
	{
		for(j=2; j*j<=i; j++)
		{
			if((i%j)==0)
				break;
		}
		if(j*j>i)
		{
			plis.push_back(i);
			isp[i]=true;
		}
	}
	return;
}


int main(void)
{
	init();
	cout << "DONESTART" << endl;
	int ttt;
	cin >> ttt;
	int ct = 0;
	while(ttt>0)
	{
		
		ct++;
		ttt--;
		long long i,j,k,a,b,n,m,pmin;
		cin >> a >> b >> pmin;
		
		
		memset(done,0,sizeof(done));
		memset(pdone,0,sizeof(pdone));
		memset(divsz,0,sizeof(divsz));
		for(i=0; i<plis.size(); i++)
		{
			if(plis[i]<pmin)
			{
				continue;
			}
			if(a%plis[i]==0)
			{
				j=a;
			}
			else
			{
				j=a+(plis[i] - (a%plis[i]));
			}
			for( ;j<=b; j+=plis[i])
			{
				divs[j-a][divsz[j-a]]=i;
				divsz[j-a]++;
			}
		}
		int readfrom=0;
		int writeto=0;
		int ans =0;
		for(i=a; i<=b; i++)
		{
			if(!done[i-a])
			{
				dolis[0]=i;
				done[i-a]=true;
				ans++;
				readfrom=0;
				writeto=1;
				while(readfrom<writeto)
				{
					j=dolis[readfrom];
					//cout << j << endl;
					for(int kkk=0; kkk<divsz[j-a]; kkk++)
					{
						k=divs[j-a][kkk];
						if(!pdone[plis[k]] && (j%plis[k])==0)
						{
							
							pdone[plis[k]]=true;
							for(m=dolis[readfrom]-plis[k]-a; m>=0; m-=plis[k])
							{
								if(!done[m])
								{
									dolis[writeto]=m+a;
									writeto++;
									done[m]=true;
								}
							}
							for(m=dolis[readfrom]+plis[k]-a; m<=b-a; m+=plis[k])
							{
								if(!done[m])
								{
									dolis[writeto]=m+a;
									writeto++;
									done[m]=true;
								}
							}
						}
					}
					readfrom++;
				}
			}
		}
							
		
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
	}

	
	return 0;
}

