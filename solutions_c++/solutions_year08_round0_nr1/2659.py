#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
using namespace std;

#define CONST 100
int main()
{
	FILE *pin;
	FILE *pout;	
	pin  = fopen("e:\\in.txt", "r");
	pout = fopen("e:\\out.txt", "w");

	int cases,times;
	string strs[CONST], strq[CONST];
	int qq[CONST];
	int dp[CONST][CONST];
	char ch;
	int i,j,k,tota,totb,flag,s,q;

	fscanf(pin,"%d",&cases);
	for (times=0;times<cases;times++)
	{
		//Init
		for (i=0;i<CONST;i++)
		{
			strs[i]="";
			strq[i]="";
			qq[i]=0;
			for (j=0;j<CONST;j++)
				dp[i][j]=-1;
		}
		fscanf(pin,"%d",&s);
		fscanf(pin,"%c",&ch);
		for (i=0;i<s;i++)
		{
			ch=0;
			while (ch!='\n')
			{
				fscanf(pin,"%c",&ch);
				if (ch!='\n') strs[i]+=ch;
			}
		}
		fscanf(pin,"%d",&q);
		fscanf(pin,"%c",&ch);
		for (i=0;i<q;i++)
		{
			ch=0;
			while (ch!='\n')
			{
				fscanf(pin,"%c",&ch);
				if (ch!='\n') strq[i]+=ch;
			}
			for (j=0;j<s;j++)
				if (strq[i]==strs[j]) qq[i]=j;
		}
		ch=0;
		
		//Solve
		for (i=0;i<s;i++) dp[0][i]=0;
		dp[0][qq[0]]=1;
		for (i=1;i<q;i++)
			for (j=0;j<s;j++)
			{
				for (k=0;k<s;k++)
				{
					if (qq[i]==k) continue;
					if (j==k)
					{
						if (qq[i]==k) continue;
						if (dp[i][j] == -1 || dp[i][j]>dp[i-1][j]) dp[i][j]=dp[i-1][j];
						continue;
					}
					if (dp[i][j] == -1 || dp[i][j]>dp[i-1][k]+1)
						dp[i][j]=dp[i-1][k]+1;
				}
			}
		int min=-1;
		for (i=0;i<s;i++)
			if (min==-1 || min>dp[q-1][i]) min=dp[q-1][i];
		if (q==0) fprintf(pout,"Cases #%d: %d\n",times+1,0);
		else fprintf(pout,"Cases #%d: %d\n",times+1,min);
	}
	fclose(pin);
	fclose(pout);
	return 0;
}