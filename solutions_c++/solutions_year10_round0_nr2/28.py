/*
 *  A.cpp
 *  
 *
 *  Created by Nathan David Claus on 4/1/10.
 *  Copyright 2010 __MyCompanyName__. All rights reserved.
 *
 */


// cheburashka, bear-mouse, team template

#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <stack>
#include <cmath>
#include <queue>
#include <cstring>
#include <set>
using namespace std;

typedef long long ll;
typedef vector < string > vs;
typedef vector <int> vi;
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;

#define pb(x) push_back(x)

#define mp(x, y) make_pair(x, y)

#define PII pair<long long,long long>
const int MAXSIZE = 60;
struct Biggie 
{
	int nums[MAXSIZE];
	int SZ;
};

inline int gsize(Biggie A)
{
	for(int i = MAXSIZE-1; i >= 0; i--)
	{
		if(A.nums[i] > 0) return i+1;
	}
	return 0;
}

void bdeb(Biggie A)
{
	if(gsize(A) == 0)
	{
		printf("0\n");
		return;
	}
	for(int i = MAXSIZE-1; i >= 0; i--)
	{
		if(A.nums[i] > 0)
		{
			A.SZ = i+1;
			break;
		}
	}
	if(A.SZ == 0) A.SZ = 1;
	for(int i = A.SZ-1; i >= 0; i--)
	{
		printf("%d",A.nums[i]);
	}
	printf("\n");
}

bool bigger(Biggie A, Biggie B)
{
	for(int i = MAXSIZE-1; i >= 0; i--)
	{
		if(A.nums[i] > B.nums[i]) return true;
		if(B.nums[i] > A.nums[i]) return false;
	}
	return true;
}

Biggie sub(Biggie A, Biggie B)
{
	Biggie ret;
	memset(ret.nums,0,sizeof(ret.nums));
	for(int i = 0; i < MAXSIZE; i++)
	{
		ret.nums[i] = A.nums[i]-B.nums[i];
		if(ret.nums[i] < 0)
		{
			ret.nums[i] += 10;
			A.nums[i+1]--;
		}
	}
	return ret;
}

Biggie mult(Biggie A, Biggie B)
{
	Biggie ret;
	memset(ret.nums,0,sizeof(ret.nums));
	B.SZ = A.SZ = 0;
	for(int i = MAXSIZE-1; i >= 0; i--)
	{
		if(A.nums[i] > 0 && A.SZ == 0)
		{
			A.SZ = i+1;
		}
		if(B.nums[i] > 0 && B.SZ == 0)
		{
			B.SZ = i+1;
		}
	}
	for(int i = 0; i < B.SZ; i++)
	{
		if(B.nums[i] == 0) continue;
		for(int j = 0; j < A.SZ; j++)
		{
			if(A.nums[j] == 0) continue;
			ret.nums[i+j] += B.nums[i]*A.nums[j];
			int k = i+j;
			while(ret.nums[k] > 9)
			{
				ret.nums[k+1] += ret.nums[k]/10;
				ret.nums[k] %= 10;
				k++;
			}
		}
	}
	return ret;
}

Biggie gmodulus(Biggie A, Biggie B)
{
    Biggie tmp,NA;
	memset(tmp.nums,0,sizeof(tmp.nums));
	for(int i = 0; i < MAXSIZE; i++) NA.nums[i] = A.nums[i];
    //BigInt tmp( 0, size );
	
	int start = MAXSIZE-1;
	while(NA.nums[start] == 0) start--;
    for(int i = start; i >= 0; i-- )
    {
		
        tmp.nums[0] += NA.nums[i];
        NA.nums[i] = 0;
        while( bigger(tmp,B) ) { tmp  = sub(tmp,B); NA.nums[i]++; }
		for(int k = start-i; k >= 0; k--)
		{
			tmp.nums[k+1] = tmp.nums[k];
		}
		tmp.nums[0] = 0;
    }
    Biggie full = mult(NA,B);
	Biggie ret = sub(A,full);
	/*
	printf("MODULUS\n");
	bdeb(A);
	bdeb(B);
	bdeb(NA);
	bdeb(ret); */
    return ret;
}

	

Biggie gcd(Biggie A, Biggie B)
{
	if(gsize(B) == 0) return A;
	return gcd(B,gmodulus(A,B));
}

long long GG(long long A, long long B)
{
	if(B == 0) return A;
	return GG(B,A%B);
}

int main()
{
	/*
	Biggie A, B;
	memset(A.nums,0,sizeof(A.nums));
	memset(B.nums,0,sizeof(B.nums));
	for(int i = 0; i < 500; i++)
	{
		if(i%100 == 0) deb(i);
		for(int j = 0; j < 500; j++)
		{
			A.nums[2] = i / 100;
			B.nums[2] = j / 100;
			A.nums[1] = (i / 10) % 10;
			A.nums[0] = i % 10;
			B.nums[1] = (j / 10) % 10;
			B.nums[0] = j % 10;
			gcd(A,B);
		}
	}
	bdeb(A);
	*/
	int T;
	cin >> T;
	for(int tcase = 1; tcase <= T; tcase++)
	{
		int N;
		cin >> N;
		Biggie Q[N];
		for(int i = 0; i < N; i++)
		{
			string neu = "";
			cin >> neu;
			memset(Q[i].nums,0,sizeof(Q[i]));
			for(int j = 0; j < neu.size(); j++)
			{
				Q[i].nums[neu.size()-j-1] = neu[j]-'0';
			}
			//bdeb(Q[i]);
		}
		Biggie ret;
		if(bigger(Q[0],Q[1])) ret = sub(Q[0],Q[1]);
		else ret = sub(Q[1],Q[0]);
		
		for(int j = 2; j < N; j++)
		{
			Biggie next;
			if(bigger(Q[0],Q[j])) next = sub(Q[0],Q[j]);
			else next = sub(Q[j],Q[0]);
			ret = gcd(ret,next);
		}
		
		Biggie D;
		memset(D.nums,0,sizeof(D.nums));
		for(int i = 0; i < N; i++)
		{
			Biggie next = gmodulus(Q[i],ret);
			if(gsize(next) == 0) continue;
			next = sub(ret,next);
			if(bigger(next,D)) D = next;
		}
		printf("Case #%d: ",tcase);
		bdeb(D);
	}
	
	return 0;
}