#include "iostream"
#include "string"
using namespace std;
int Max;
void DecToBin (unsigned int iDec, char *p) 
{ 
	unsigned int temp; 
	int i=31; 
	while(i>=0) 	
	{ 	
		temp=iDec; 	
		temp=temp>>i; 	
		temp=temp&1; 	
		p[32-1-i]=temp+'0'; 
		i--; 
	} 
} 
void DoXor(char str1[],char str2[],char *pStr)
{
	int i=0;
	for(i=31;i>=0;i--)
	{	
		int tmp=str1[i]-'0'+str2[i]-'0';
		if(tmp%2) pStr[i]='1';
		else pStr[i]='0';
	}
}
void init(char *str)
{
	int ii;
	for(ii=0;ii<33;ii++)	
	{ 
		str[ii]='\0'; 
	} 
}
void getn(int a[],int b[] , int n, int m, int index,int lastindex)
{
	char pBin[33]; 
	char pBin1[33];
	char pResult[33];
	char pResult2[33];
	int ii;
	int sum=0;
	init(pBin1);
	
	int i = lastindex + 1; 
	if(index == m )
	{
		int x;
		init(pResult);
		for(x = 0 ; x  < m ;x ++)
		{
			//cout<<a[b[x]]<<" ";
			sum+=a[b[x]];
			init(pBin);
			DecToBin(a[b[x]],pBin); 
			DoXor(pBin,pResult,pResult);
		}
	//	printf("%s\n",pResult); 
	//	int bb[256];
		int mm=n-m;
		int jj;
		init(pResult2);
		for (ii=0;ii<n;ii++)
		{
			for (jj=0;jj<m;jj++)
			{
				if(ii==b[jj])  break;
			}
			if(jj==m) 
			{
				init(pBin);
				DecToBin(a[ii],pBin); 
				DoXor(pBin,pResult2,pResult2);
			}
		}
		if(strcmp(pResult,pResult2)==0) 
		{
			if(sum>Max) Max=sum;
		}
	}
	while( i  < n)
	{
		b[index] = i;
		getn(a,b,n,m,index + 1,i);
		i++;
	}
} 

int main() 
{ 
	int T;
	int i,j,k;
	int n;
	int a1[256];
	//freopen("C-small-attempt0.in", "r", stdin);
    //freopen("output.out", "w", stdout);
	cin>>T;
	for (i=0;i<T;i++)
	{
		Max=0;
		cin>>n;
		for (k=0;k<n;k++)
		{
			cin>>a1[k];
		}

		int b1[256]={0};
		for(j=n-1;j>0;j--)
			getn(a1,b1,n,j,0,-1);
		if(Max)
			cout<<"Case #"<<i+1<<": "<<Max<<endl;
		else cout<<"Case #"<<i+1<<": NO"<<endl;
	}

	return 0;
} 
