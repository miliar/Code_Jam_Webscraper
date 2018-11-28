#include<iostream>
#include<string.h>
#include<math.h>
#include<algorithm>
#define MAXN 15
#define binbits 32
using namespace std;
void dec2bin(int n,char bin[])
{
	int b=binbits-1;
	bin[binbits]='\0';
	for(int i=0;i<=b;i++)
		bin[i]='0';
    while (n)
    {
        bin[b]=((n & 1) + '0');
        n >>= 1;
        b--;
    }
}
int bin2dec(char *bin)
{
    int  b, k, m, n;
    int  len, sum = 0;

    len = strlen(bin) - 1;
    for(k = 0; k <= len; k++)
    {
		n = (bin[k] - '0'); // char to numeric value
		if ((n > 1) || (n < 0))
		{
	        return (0);
		}
		for(b = 1, m = len; m > k; m--)
		{
	        // 1 2 4 8 16 32 64 ... place-values, reversed here
	        b *= 2;
		}
		// sum it up
		sum = sum + n * b;
		//printf("%d*%d + ",n,b);  // uncomment to show the way this works
    }
    return(sum);
}
int correctsum(int a[],int n)
{
	int sum=0;
	for(int i=0;i<n;i++)
	{
		sum=sum+a[i];
	}
	return sum;
}
int wrongsum(int a[],int n)
{
	char sum[33];
	for(int i=0;i<32;i++)
		sum[i]='0';
	sum[32]='\0';
	for(int i=0;i<n;i++)
	{
		char num[33];
		dec2bin(a[i],num);
		for(int i=0;i<32;i++)
		{
			if(sum[i]==num[i])
				sum[i]='0';
			else
				sum[i]='1';
		}
	}
	return bin2dec(sum);
}
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n,c[MAXN];
		int p[(int)pow(2,MAXN)][MAXN];	//power set
		int pc=1;					//count of elements in power set
		int pe[(int)pow(2,MAXN)];		//count of no. of elements in each set of power set
		pe[0]=0;
		cin>>n;
		
		for(int j=0;j<n;j++)
		{
			cin>>c[j];
			for(int k=0;k<pc;k++)
			{
				//add all elements of p[k] to p[pc+k]
				int l;
				for(l=0;l<pe[k];l++)
				{
					p[pc+k][l]=p[k][l];
				}
				//add c[j] to to p[pc+k]
				p[pc+k][l]=c[j];
				pe[pc+k]=pe[k]+1;
			}
			pc=2*pc;
		}
		//for each power set
		//find a complementary set, ie. if we are looking at set x, complementary set is (2^n)-x-1
		int maxp=pow(2,n);
		int ans=0;
		for(int j=0;j<maxp/2;j++)
		{
			int cs1=correctsum(p[j],pe[j]);
			int cs2=correctsum(p[maxp-j-1],pe[maxp-j-1]);
			int ws1=wrongsum(p[j],pe[j]);
			int ws2=wrongsum(p[maxp-j-1],pe[maxp-j-1]);
			//cout<<"cs1 = "<<cs1<<", cs2 = "<<cs2<<", ws1 = "<<cs1<<", ws2 = "<<ws2<<endl;
			if(ws1==ws2 && ws1!=0)
			{
				if(cs1>ans)	
					ans=cs1;
				if(cs2>ans)
					ans=cs2;
			}
		}
		if(ans==0)
			cout<<"Case #"<<i<<": NO\n";	
		else
			cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}
