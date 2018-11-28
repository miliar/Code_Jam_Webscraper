#include <iostream>
#include<fstream>
#include <string>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include<math.h>
#include<sstream>
#include <algorithm>
using namespace std;
char szdis[5005][16];
char str[1000];
char temp[16][30];
int tn[16];
int len,dis,num;
long find()
{
	int i,j,ij,ok;
	long k=0;
	for (i=0;i<dis;i++)
	{
		ok=0;
		for (j=0;j<len;j++)
		{
			ok=1;
			for (ij=0;ij<tn[j];ij++)
				if (szdis[i][j]==temp[j][ij])
				{
					ok=0;
					break;
				}
			if (ok==1)
				break;

		}
		if (ok==0)
			k++;
	}
	return k;
}
int main()
{
	//ofstream fo("G:\\ASmallAns.txt",ios_base::out);
	int i,j,k,n;
	scanf("%d%d%d",&len,&dis,&num);
	for (i=0;i<dis;i++)
		scanf("%s",&szdis[i]);
	for (n=1; n<=num;n++)
	{
		scanf("%s",&str);
		k=0;
		memset(tn,0,sizeof(tn));
		i=0;
		int l = strlen(str);
		for (j=0;j<l; j++)
		{
			if (str[j]=='(')
			{
				j++;
				while(str[j]!=')')
				{
					temp[i][tn[i]]=str[j];
					j++;
					tn[i]++;
				}
			}
			else
			{
				temp[i][tn[i]]=str[j];
				tn[i]++;				
			}			
			i++;
		}
		//fo<<"Case #"<<n<<": "<<find()<<endl;
		printf("Case #%d: %ld\n",n,find());
	}

	//fo.close();
	//cin>>i;


	return 0;
}