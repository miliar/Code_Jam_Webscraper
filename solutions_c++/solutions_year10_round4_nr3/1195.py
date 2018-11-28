#include <stdio.h>
#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <string.h>
#include <stdlib.h>
using namespace std;

char b[102][102];

int main()
{
int tc;
cin >>tc;

for(int t=1;t<=tc;++t)
{
int r;
cin>>r;
memset(b,'0',sizeof b);
for(int i=0;i<r;++i)
  {
	int x1,y1,x2,y2;
	cin>>x1>>y1>>x2>>y2;
	for(int j=x1;j<=x2;++j)
		for(int k=y1;k<=y2;++k)
			b[j][k]='1';
  }
int cnt=0;
for(int i=1;i<=100;++i)
   for(int j=1;j<=100;++j)
	if(b[i][j]=='1') ++cnt;

long long ans=0;
/*for(int i=0;i<7;++i) {
        for(int j=0;j<10;++j)
                cout<<b[i][j];
        cout<<endl;
 }*/

while(cnt>0)
{
++ans;
//cout<<"cnt=="<<cnt<<endl;
for(int i=1;i<=100;++i)
   for(int j=1;j<=100;++j)
   {
	if (b[i][j]=='1') {
	if( ((i==1)||(i-1>=1 && (b[i-1][j]=='0' || b[i-1][j]=='3'))) && ( (j==1)||(j-1>=1 && (b[i][j-1]=='0' || b[i][j-1]=='3'))) )
		{b[i][j]='2';--cnt;}
	} else {
	if( (i-1>=1 && (b[i-1][j]=='1'||b[i-1][j]=='2')) && (j-1>=1 && (b[i][j-1]=='1'||b[i][j-1]=='2')) )
		{b[i][j]='3';++cnt;}
	}
  }

for(int i=1;i<=100;++i)
   for(int j=1;j<=100;++j)
	if(b[i][j]=='2')
		b[i][j]='0';
	else if(b[i][j]=='3')
		b[i][j]='1';

// for(int i=0;i<7;++i) {
//	for(int j=0;j<10;++j)
//		cout<<b[i][j];
 //	cout<<endl;
// }

}



cout<<"Case #"<<t<<": "<<ans<<endl;
}

}
