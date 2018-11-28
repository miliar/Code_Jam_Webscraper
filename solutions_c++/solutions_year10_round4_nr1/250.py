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

ofstream fout("../../output.txt");
ifstream fin("../../input.txt");

int vals[200][200];

int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k;
		int l,m;
		
		fin >> n;
		memset(vals,0,sizeof(vals));
		
		for(i=0; i<n; i++)
		{
			j= n-1 - i;
			for(k=0; k<i+1; k++,j+=2)
			{
				fin >>l;
				vals[i][j]=l+1;
			}
		}
		for(i=n; i<2*n-1; i++)
		{
			j = i-(n-1);
			for(k=0; k<2*n-i-1; k++,j+=2)
			{
				fin >> l;
				vals[i][j]=l+1;
			}
		}
		
		int ans = 100*k;
		
		/*for(i=0; i<2*n-1; i++)
		{
			for(j=0; j<2*n-1; j++)
			{
				cout << vals[i][j];
			}
			cout << endl;
		}*/
		
		bool isokr[200];
		bool isokc[200];
		
		for(i=0; i<2*n-1; i++)
		{
			isokr[i]=true;
			
			for(j=0; j<2*n-1 && isokr[i]; j++)
			{
				k=l=i;
				while(k>=0 && l<2*n-1)
				{
					if(vals[k][j]!=vals[l][j] && vals[k][j]>0 && vals[l][j]>0)
					{
						isokr[i]=false;
						break;
					}
					k--;
					l++;
				}
			}
			cout << isokr[i];
		}
		cout << endl;
		
		for(i=0; i<2*n-1; i++)
		{
			isokc[i]=true;
//			cout << i << endl;
			for(j=0; j<2*n-1 && isokc[i]; j++)
			{
				k=l=i;
				while(k>=0 && l<2*n-1)
				{
				//	cout << j << " " << k << " " << l << " " << vals[k][j] << " " << vals[l][j] << endl;

					if(vals[j][k]!=vals[j][l] && vals[j][k]>0 && vals[j][l]>0)
					{
						isokc[i]=false;
						break;
					}
					k--;
					l++;
				}
			}
			cout << isokc[i];
		}
		cout << endl;
		
		for(i=0; i<2*n-1; i++)
		{
			for(j=0; j<2*n-1; j++)
			{
				if(!isokr[i] || !isokc[j])
					continue;
				/*k=i;
				if(2*n-2-i > k)
					k=2*n-2-i;
				l=j;
				if(2*n-2-j>l)
					l=2*n-2-j;
				k+=abs(n-1-i);
				l+=abs(n-1-j);
				k++;
				l++;
				m=k;
				if(l>m)
					m=l;
				cout << i << " " << j << " " <<k << " " << l << " " << m << endl;*/
				m=0;
				
				k = abs(n-1-i)+abs(2*n-2-j);
				if(k>m)
					m=k;
				k = abs(n-1-i)+abs(j);
				if(k>m)
					m=k;
				k = abs(n-1-j)+abs(2*n-2-i);
				if(k>m)
					m=k;
				k = abs(n-1-j)+abs(i);
				if(k>m)
					m=k;
				
				
				
				m++;
				if(m<ans)
					ans=m;
			}
		}
		cout << ans << endl;
		
		cout << "Case #" << ct << ":" << " " << ans*ans-n*n << endl;
		fout << "Case #" << ct << ":" << " " << ans*ans-n*n << endl;
		
	}
	
	
	return 0;
}

