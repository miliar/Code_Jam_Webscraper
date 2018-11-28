// console.cpp : 定义控制台应用程序的入口点。
//

#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>

using namespace std;
#define rep(i,N) for(int i=0;i<(N);i++)

//	_getch();


char sq[51][51];

int main(int argc, char* argv[])
{
	//freopen("C:\\users\\lxy\\downloads\\practice.in","r",stdin);
	//freopen("C:\\users\\lxy\\downloads\\B-small-attempt2.in","r",stdin);
//	freopen("in","r",stdin);
//	freopen("C:\\users\\lxy\\downloads\\out","w",stdout);

	int t;
	cin>>t;
	rep(i,t)
	{
//		long long n;
//		int pd,pg;
		cout<<"Case #"<<i+1<<":"<<endl;
		int r,c;
		cin>>r>>c;
		rep(j,r)
		{
			cin>>sq[j];
		}
		rep(j,r)
		{
			rep(k,c)
			{
				if(sq[j][k]=='#')
				{
					if((j<r-1)&&(k<c-1)&&(sq[j+1][k]=='#')&&(sq[j][k+1]=='#')&&(sq[j+1][k+1]=='#'))
					{
						sq[j+1][k]='\\';
						sq[j][k+1]='\\';
						sq[j][k]='/';
						sq[j+1][k+1]='/';

						continue;
					}
					cout<<"Impossible"<<endl;
					goto out;
				}
			}
		}
		rep(j,r)
			cout<<sq[j]<<endl;
out:
			;
	}

}

