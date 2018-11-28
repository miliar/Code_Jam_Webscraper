#include <cmath>
#include <algorithm>
#include <sstream>
#include <queue>
#include<iostream>
#define FALSE 0
#define TRUE 1
using namespace std;
typedef long long ll;
typedef pair<int,int> ipair;
#define SIZEARRAY(x) (sizeof(x)/sizeof(x[0]))

const int maxnum = 105;
int mm[260];

int main()
{

	freopen("F:\\code\\topcoder\\B-large (1).in","r",stdin);
	freopen("F:\\code\\topcoder\\compete\\compete\\test2.out","w",stdout);
	int caseNum;
	cin>>caseNum;
	int caseIndex;
	caseIndex = 1;
	int data[maxnum];
	while(caseIndex<=caseNum)
	{
		cerr<<caseIndex<<endl;
		int D,I,M,N;
		int tempValue;
		cin>>D>>I>>M>>N;
		for (int i = 0;i<N;i++)
		{
			cin>>data[i];
		}
		for (int i = 0;i<256;i++)
		{
			mm[i] = I;
		}
		mm[256] = 0;
		int tempMin[260];
		memset(tempMin,0,sizeof(tempMin));
		for (int i = 0;i<N;i++)
		{
			for (int j = 0;j<256;j++)
			{
				tempValue = mm[j];
				for (int st = max(0,j-M);st<=min(255,j+M);st++)
				{
					tempValue = min(tempValue,mm[st]);
				}
				tempValue = min(tempValue,mm[256]);
				tempMin[j] = tempValue;
			}
			for (int j = 0;j<256;j++)
			{
				tempValue = mm[j]+D;
				tempValue = min(abs(j-data[i])+tempMin[j],tempValue);
				mm[j] = tempValue;
			}
			mm[256]+=D;
			int nmm[260];
			memcpy(nmm,mm,sizeof(nmm));
			if(M != 0)
			{
				for (int j = 0;j<256;j++)
				{
					nmm[j] = mm[j];
					for (int st = 0;st<=255;st++)
					{
						if (j == st)
						{
							continue;
						}
						tempValue = ((abs(j-st)-1)/M+1)*I+mm[st];
						nmm[j] = min(nmm[j],tempValue);
					}
					nmm[j] = min(mm[256]+I,nmm[j]);
				}
				memcpy(mm,nmm,sizeof(nmm));
			}
			
		}
		tempValue = mm[0];
		for (int i = 0;i<=256;i++)
		{
			if (tempValue>mm[i])
			{
				tempValue = mm[i];
			}
		}
		cout<<"Case #"<<caseIndex<<": "<<tempValue<<endl;
		caseIndex++;
	}
}