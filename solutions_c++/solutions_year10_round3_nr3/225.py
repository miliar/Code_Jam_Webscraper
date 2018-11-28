#include <stdio.h>
#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <string.h>
#include <stdlib.h>
using namespace std;

int m,n;

int b[512][512];
int sq[512][512];
int sz[512];


int main()
{
int tc;
cin >>tc;
char str[512];
for(int t=1;t<=tc;++t)
{
cin>>m>>n;
for(int i=0;i<m;++i)
{
	cin>>str;
	int k=0;
	for(int j=0;j<n/4;++j)
	 {
		int c;
		if (str[j]>='0' & str[j]<='9')
			c = str[j]-'0';
		else 
			c = 10 + str[j] - 'A';
		b[i][k++] = (c>>3)&1;
		b[i][k++] = (c>>2)&1;
		b[i][k++] = (c>>1)&1;
		b[i][k++] = c&1;

	 }
}

/*for(int i=0;i<m;++i){
	for(int j=0;j<n;++j)
		cout<<b[i][j];
  cout<<endl;
}*/	


int mx = min(m,n);
int cnt=0;
//cout<<"mx=="<<mx<<endl;

for(int l = mx;l>=1;--l)
{
sz[l]=0;
for(int i=0;i+l-1<m;++i)
	for(int j=0;j+l-1<n;++j)
	{
		int clr=-1,flag=true;
		int inc = 1,st=j,c;
		for(int r=i;r<i+l;++r) {
			for(c=st;c<j+l && c>=j;c+=inc)
			 {
				if (clr==b[r][c]||b[r][c]==2)  {flag=false;goto out;}
				clr = b[r][c];	
			 }
			if(c==j+l) {
				st=j+l-1;inc=-1;		
			} else {
				st=j;inc=1;
			}
		}
		out:;
		if(flag) {
			//	cout<<i<<' '<<j<<' '<<l<<endl;
				sz[l]++;
				for(int r=i;r<i+l;++r)
                        		for(int c=j;c<j+l;++c)
						b[r][c]=2;
			}
	}
if (sz[l]>0)
	++cnt;
}

cout<<"Case #"<<t<<": "<<cnt<<endl;
for(int i=mx;i>=1;--i)
{
if (sz[i]>0)
	cout<<i<<' '<<sz[i]<<endl;
}

}

}
