#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
#include <queue>
#include <map>
using namespace std;
#define MAX 2000

int   Radix(char *toStr, char *fromStr) 
{
int i = 0, j = 0;
int len;

while (fromStr[i] != '.' && fromStr[i] != '\0')
{
   toStr[j++] = fromStr[i++];
}
len = i++;
while (fromStr[i] != '\0')
{
   toStr[j++] = fromStr[i++];
}

return i - len - 1;
}

void IntAddition(char *augend, char *addend, char *sum)
{
int cAug[MAX] = {0};
int cAdd[MAX] = {0};
int cSum[MAX] = {0};
int lenAug = strlen(augend), lenAdd = strlen(addend);¶È
int lenMin = lenAug < lenAdd ? lenAug : lenAdd;
int i;


for (i=0; i<lenAug; i++)
   cAug[i] = augend[lenAug-1-i] - '0';
for (i=0; i<lenAdd; i++)
   cAdd[i] = addend[lenAdd-1-i] - '0';

int carry = 0;
int s = 0; 

for (i=0; i<lenMin; i++)
{
   s = cAug[i] + cAdd[i] + carry; 
   cSum[i] = s % 10;
   carry = s / 10; 
}


while (i < lenAug)
{
   s = cAug[i] + carry;
   cSum[i] = s % 10;
   carry = s / 10;
   i++;
}

while (i < lenAdd)
{
   s = cAdd[i] + carry;
   cSum[i] = s % 10;
   carry = s / 10;
   i++;
}

if (carry > 0)
   cSum[i++] = carry;


int j;
for (j=0; j<i; j++)
   sum[j] = cSum[i-1-j] + '0';
sum[i] = '\0';
}


void IntMultiplication(char *multiplicand, char *multiplier, char *product)
{
int cD[MAX] = {0}; 
int cR[MAX] = {0};
int cP[MAX] = {0};
char tcP[MAX] = "";
int lenD = strlen(multiplicand), lenR = strlen(multiplier);
int i, j, k;

 
for (i=0; i<lenD; i++)
   cD[i] = multiplicand[lenD-1-i] - '0';
for (i=0; i<lenR; i++)
   cR[i] = multiplier[lenR-1-i] - '0';

int carry;
int mul = 0; 

strcpy(product, "0"); 
for (i=0; i<lenR; i++)
{
   carry = 0;
   for (j=0; j<lenD; j++)
   {
    mul = cD[j] * cR[i] + carry;
    cP[j] = mul % 10;
    carry = mul / 10;
   }
   if (carry > 0)
    cP[j++] = carry;
  
   while (cP[j-1] == 0)
    --j;
  

   for (k=0; k<j; k++)
    tcP[k] = cP[j-1-k] + '0';
   for (j=0; j<i; j++) 
    tcP[k++] = '0';
   tcP[k] = '\0';
  
   IntAddition(product, tcP, product);
} 
}


void FloatMultiplication(char *multiplicand, char *multiplier,char *product)
{
char cD[MAX] = {0};
char cR[MAX] = {0};
char cP[2*MAX] = {0};
int lenD, lenR, lenP;


lenD = Radix(cD, multiplicand);
lenR = Radix(cR, multiplier);
lenP = lenD + lenR;

IntMultiplication(cD, cR, cP);

int i = strlen(cP) - 1;
while (lenP > 0 && cP[i] == '0') 
{
   i--;
   lenP--;
}
cP[i+2] = '\0';

while (lenP > 0 && i >= 0) 
{
   cP[i+1] = cP[i];
   i--;
   lenP--;
}
cP[i+1] = '.';

if (i == -1)
{
   for (i=strlen(cP); i>0; --i)
    cP[i+1+lenP] = cP[i];
   for (i=0; i<lenP; ++i)
    cP[i+2] = '0';
   cP[1] = '.';
   cP[0] = '0';
}

strcpy(product, cP);
}

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
freopen("C-small-attempt1.out","w",stdout);

	char a[MAX]="5.2360679774997896964091736687313";
	int n;
	int k;
    int d=1;
	int j;
	int i,t;
	cin>>t;
	while(t--)
	{
		k=0;
		char ans[MAX*2]="1.0";
		cin>>n;
		for(i=1;i<=n;i++)
		{
			FloatMultiplication(ans,a,ans);
		}
		for(i=0;i<400;i++)
		{
			if(ans[i]=='.')break;
		}
		j=i;
		int y=1;
		for(i--;i>=j-3&&i>=0;i--)
		{
			k=k+(ans[i]-'0')*y;
			y*=10;
		}
		printf("Case #%d: ",d++);
		if(k<10)printf("00%d\n",k);
		else if(k<100)printf("0%d\n",k);
		else printf("%d\n",k);
	}





	return 0;
}

/*power by gdut_chc*/