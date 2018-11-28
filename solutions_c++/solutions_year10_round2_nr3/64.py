#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../output.txt");
ifstream fin("../../input.txt");

long long MOD = 100003;

long long inv(long long x)
{
	int mod = MOD - 2;
	long long ans = 1;
	long long curr = x;
	for(int i=0; i<20; i++)
	{
		if( (mod & ( 1<<i))>0)
		{
			//cout << "HELLO ";
			ans*=curr;
			ans%=MOD;
		}
		curr*=curr;
		curr%=MOD;
		//cout << i << " " << curr << " " << ans << endl;
	}
	
	
	return ans;
}
long long invs[120000];
long long choose(long long a, long long b)
{
	long long ans = 1;
	if(a<b)
		return 0;
	for(int i=1; i<=b; i++)
	{
		ans*=((long long)a+1-i);
		ans%=MOD;
		ans*=invs[i];
		ans%=MOD;
	}
	return ans;
}

long long anses[501][501];
long long chooses[501][501];


int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	cout << inv(2) << " " << inv(3) << endl;
	
	int i,j,k;
	
	for(i=1; i<=500; i++)
	{
		invs[i]=inv(i);
	}
	
	for(i=0; i<=500; i++)
	{
		for(j=0;j<=500; j++)
		{
			chooses[i][j]=choose(i,j);
		}
	}
	cout << chooses[10][3] << " " << chooses[10][2] << endl;
		
	for(i=2; i<=500; i++){
		anses[i][1]=1;
		for(j=2; j<i; j++)
		{
			for(k=1; k<j; k++)
			{
				anses[i][j]+=anses[j][k]*chooses[i-j-1][j-k-1];
				anses[i][j]%=MOD;
			}
		}
	}
	cout << anses[5][4] << endl;
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n;
		fin >> n;
		long long ans=0;
		for(i=0; i<n; i++)
		{
			ans+=anses[n][i];
			ans%=MOD;
		}
		
		
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
		
	}
	
	
	return 0;
}

