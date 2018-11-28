#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <float.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

#define ABS(a) (a>=0?a:-(a))
#define MIN(a,b) (a<=b?a:b)
#define MAX(a,b) (a>=b?a:b)
#define rep(a,b) for(a=0;a<b;a++)
#define rep1(a,b) for(a=1;a<=b;a++)
#define rep2(a,b,c) for(a=b;a<c;a++)
#define drep(a,b) for(a=b-1;a>=0;a--)
#define drep1(a,b) for(a=b;a>=1;a--)
#define drep2(a,b,c) for(a=b;a>=c;a--)
#define foreach(vec,it) for(vector<int>::iterator it = vec.begin();it!=vec.end();it++)
#define foreach2(co,ty,it,name) for(co< ty >::iterator it = name.begin();it!=name.end();it++)

#define NMAX 8
int A[NMAX][NMAX];
int check(int i, int j, int opi, int opj)
{
	int ii=i+opi, jj=j+opj;
	int ans = 1;
	while(ii>=0 && ii < 4 && jj>=0 && jj<4 && A[ii][jj]!='.' &&
			(A[i][j]==A[ii][jj] || A[ii][jj]=='T'))
	{	ans++; ii+=opi; jj+=opj; }
	return ans;
}
void solve_problem()
{	
	int n, i, j, k;
	char c;
	scanf("%d",&n);	
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			scanf(" %c",&A[i][j]);
	char ans = 'D';
	rep(i,4) rep(j,4)
	{
		if(A[i][j]=='.') { ans = '.'; continue; }
		if(A[i][j]=='T') continue;
		if(check(i,j,+1,0)>=4) { ans = A[i][j]; goto end; }
		if(check(i,j,+1,+1)>=4) { ans = A[i][j]; goto end; }
		if(check(i,j,+1,-1)>=4) { ans = A[i][j]; goto end; }
		if(check(i,j,-1,0)>=4) { ans = A[i][j]; goto end; }
		if(check(i,j,-1,+1)>=4) { ans = A[i][j]; goto end; }
		if(check(i,j,-1,-1)>=4) { ans = A[i][j]; goto end; }
		if(check(i,j,0,+1)>=4) { ans = A[i][j]; goto end; }
		if(check(i,j,0,-1)>=4) { ans = A[i][j]; goto end; }
	}
end:
	if(ans=='D') cout<<"Draw"<<endl;
	else if (ans=='.') cout<<"Game has not completed"<<endl;
	else cout<<ans<<" won"<<endl;
}

int main(void)
{
	int ct, tc;
	scanf("%d",&tc);	
	for(ct=1;ct<=tc;ct++)			
	{
//		cerr<<ct<<endl;
		printf("Case #%d: ", ct);	
		solve_problem();
	}
}
