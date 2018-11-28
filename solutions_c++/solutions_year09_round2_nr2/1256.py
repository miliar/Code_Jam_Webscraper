#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<string>
#include<map>
#include<cstring>
#include<cassert>
#include<set>
#include<iostream>
#include<sstream>
#include<cstddef>
#include<utility>
#include<iterator>
#include<numeric>
#include<list>
#include<complex>
#include<deque>
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef complex<double> pnt;
typedef pair<int, int> pii;
#define malloc(type,n) ((type*)malloc(sizeof(type)*n))
#define SZ(a) ((int)((a).size()))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(a) (a<0?a*-1:a)

void qs(char *a,int low,int high)
{
int i=low,j=high-1,p=high,t;
while(i<=j && a[i]<=a[high])
	i++;
while(j>=low && a[j]>a[high])
	j--;
while(i<j)
{
	t=a[i];
	a[i]=a[j];
	a[j]=t;
	i++;
	j--;
	while(i<=j && a[i]<=a[high])
		i++;
	while(j>=i && a[j]>a[high])
		j--;
}
if(i!=high)
{
	t=a[high];
	a[high]=a[i];
	a[i]=t;
}
if(i-1>low)
	qs(a,low,i-1);
if(i+1<high)
	qs(a,i+1,high);
}

int main() {
	freopen("B-large.in","r",stdin);
	//freopen("in.txt","r",stdin);
	freopen("out1.txt","w",stdout);
	int tc,i,j,k,ans,flag =0,len,min,q;
	char n[30],c,minc;
	cin >> tc;
	for(i=0;i<tc;i++) {
	cin >> n;
	flag=0;
	len=strlen(n);
	for(j=len-2;j>=0 && !flag;j--) {
		k=j+1;
		while(k<len)
		{
			if(n[k]> n[j])
			{
				flag=1;
				break;
			}
			k++;
		}
		if(!flag)
			continue;
		min=k;
		minc=n[k];
		q=k+1;
		while(q<len)
		{
			if(n[q]<minc && n[q]>n[j])
			{
				min=q;
				minc=n[q];
			}
			q++;
		}
		c=n[min];
		n[min]=n[j];
		n[j]=c;
		flag=1;
	}
	if(flag)
	{
		qs(n,j+2,len-1);
		cout << "Case #" << i+1 << ": " << n << endl;
	}
	else
	{
		char tmp[30];
		strcpy(tmp,n);
		qs(n,0,len-1);
		if(n[0]!='0')
		{
		for(j=len;j>1;j--)
			n[j]=n[j-1];
		n[1]='0';
		n[len+1]='\0';
		cout << "Case #" << i+1 << ": " << n << endl;
		}
		else
		{
			//cout << n << endl;
			int z=1;
			while(n[z]=='0')		
				z++;
			tmp[0]=n[z];
			for(q=1;q<=z+1;q++)
			{
				tmp[q]='0';
				//cout << tmp << endl;
			}
			for(q=z+1,j=z+2;q<len;q++,j++)
				tmp[j]=n[q];			
			tmp[j]='\0';
			cout << "Case #" << i+1 << ": " << tmp << endl;
		}
	}
	
	}
	return 0;
}
