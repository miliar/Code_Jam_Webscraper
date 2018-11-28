#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<stdio.h>
#include<string.h>
#include<malloc.h>

using namespace std;

int flag[500];
int num[500];


char result[500];

#define MAX_DIGITS 100

void multiply(char * NumA,char * NumB,char * Result);
void pluss(char *a, char *b, char *c);


void inttochar(int n, char* buf)
{
	memset(buf,0,500);
	vector<int>  vec;
	if ( n == 0 )
	{
		buf[0] = '0';
		return;
	}
	while (n)
	{
		vec.push_back( n%10 );
		n /= 10;
	}
	for ( int i=0; i<vec.size(); ++i )
	{
		buf[i] = vec[vec.size()-1-i]+'0';
	}
}

string get_num( int ba, int size )
{
	char ex[500];
	char base[500];
	char tmp[500];
	char tmp2[500];
	memset( ex,0,sizeof ex );
	memset( base,0,sizeof base );
	memset( tmp,0,sizeof tmp );
	memset( tmp2,0,sizeof tmp2 );
	memset( result,0,sizeof result );
	inttochar(ba, base);
	inttochar(1,ex );
	inttochar(0,result);
	string ret = "";
	inttochar(num[size-1],tmp2);
	multiply(tmp2,ex,tmp);
	inttochar(0,tmp2);
	pluss(tmp2,tmp,result);
	for ( int i=1; i< size; ++i)
	{
		strcpy(tmp,ex);
		multiply(tmp,base,ex);
		inttochar(num[size-1-i],tmp2);
		multiply(ex,tmp2,tmp);
		strcpy(tmp2,result);
		pluss(tmp2,tmp,result);
	}
	for ( int i=0; i<500; ++i )
	{
		if ( result[i] == 0 )
			break;
		ret += result[i];
	}
	return ret;

}

int main()
{

	

	freopen("d://in.txt", "r", stdin);
	freopen("d://out.txt", "w", stdout);
	int t;
	cin >> t;
	for ( int it=0; it<t; ++it )
	{
		memset( flag,0,sizeof flag );
		memset( num,0, sizeof num );
		string code;
		cin >> code;
		int cnt = 1;
		flag[code[0]] = cnt;
		for ( int i=0; i<code.size(); ++i )
		{
			if ( flag[code[i]] == 0 )
			{
				flag[code[i]] = ++cnt;
			}
		}
		for ( int i=0; i<code.size(); ++i )
		{
			if ( flag[code[i]] == 2 )
			{
				num[i] = 0;
			}
			else if ( flag[code[i]] == 1 )
			{
				num[i] = 1;
			}
			else
			{
				num[i] = flag[code[i]]-1;
			}
		}
		cout << "Case #" << it+1 << ": " << get_num( cnt, code.size() ) << endl;


	}



	return 0;
}
void multiply(char * NumA,char * NumB,char * Result)
{
    int i,j,LengthA,LengthB;
    int * TempResult;

    LengthA=strlen(NumA);
    LengthB=strlen(NumB);
    TempResult = (int*)malloc(sizeof(int)*(LengthA+LengthB));

    for (i=0 ; i< LengthA+LengthB ; i++)
        TempResult[i]=0;

    for (i=0 ; i<LengthA ; i++)
        for (j=0 ; j<LengthB ; j++)
            TempResult[i+j+1]+=(NumA[i]-'0')*(NumB[j]-'0');

    for (i=LengthA+LengthB-1 ; i>=0 ; i--)
        if (TempResult[i]>=10)
        {
            TempResult[i-1]+=TempResult[i]/10;
            TempResult[i]%=10;
        }
    i=0;
    while (TempResult[i]==0)
        i++;
    for (j=0 ; i<LengthA+LengthB ; i++,j++)
        Result[j]=TempResult[i]+'0';
    Result[j]='\0';
    free(TempResult);
}


void pluss(char *a, char *b, char *c) {     
    char r[1000];     
    int _a, _b, _c, _r;     
    for(_a = 0; a[_a]; _a++);     
    for(_b = 0; b[_b]; _b++);     
    for(_r = 0; _a&&_b; r[_r++] = a[--_a] + b[--_b] - '0');     
    for(; _a; r[_r++] = a[--_a]);     
    for(; _b; r[_r++] = b[--_b]);     
    for(_c = 0; _c < _r; _c++)     
        if (r[_c] > '9') {     
            r[_c] -= 10;     
            (_c + 1 == _r) ? r[_r++] = '1' : r[_c + 1]++;     
        }     
    while(_r--) *c++ = r[_r];     
    *c = 0;     
    return;     
}    