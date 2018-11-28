#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <map>

#define mn(a,b) ((a<b) ? (a) : (b))
#define mx(a,b) ((a<b) ? (b) : (a))
#define ab(a) ((a<0) ? (-(a)) : (a))
#define fr(a,b) for(int a=0; a<b; ++a)
#define fe(a,b,c) for(int a=b; a<c; ++a)
#define fw(a,b,c) for(int a=b; a<=c; ++a)
#define df(a,b,c) for(int a=b; a>=c; --a)
#define BIG 1000000000
#define SMALL -1000000000

using namespace std;

char buf[1000];

void get_string(string &s)
	{
	scanf("%s", &buf);
	s.assign(buf);
	}

void get_line(string &s)
	{
	gets(buf);
	s.assign(buf);
	}


string format(int a)
	{
	string res = "";
	fr(i,4)
		{
		res = char('0'+(a%10))+res;
		a/=10;
		}
	return res;
	}

string s;
int dyn[501][20];
string code="welcome to code jam";

int main()
{
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
int n;
scanf("%d\n", &n);
fr(i,n)
	{
	memset(dyn,0,sizeof(dyn));
	get_line(s);
	int l = s.length();
//	cout<<"Get line: "<<s<<endl;
//	cout<<"Get length: "<<l<<endl;
	dyn[l][19] = 1;
	df(j,l-1,0)	
		{
/*
		fr(ii,l)
			{
			fr(jj,19)
				cout<<dyn[ii][jj]<<" ";
			cout<<endl;
			}
*/		
		fr(k,19)
			if(s[j]==code[k])
				{

//				cout<<"Found symbol: "<<s[j]<<endl;
//				cout<<"Welcome position: "<<k<<endl;
//				cout<<"String position: "<<j<<endl;

				fw(jj,j,l)
					dyn[j][k]=(dyn[j][k]+dyn[jj][k+1])%10000;
				}
		}
	int res = 0;

	fr(j,l)
		res=(res+dyn[j][0])%10000;
//	cout<<"Result: "<<res<<endl;
	string res_str = format(res);
//	cout<<"Result string: "<<res_str<<endl;
	printf("Case #%d: %s\n", i+1, res_str.c_str());
	}
return 0;
}
