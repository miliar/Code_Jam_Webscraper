/*Author : Anupam Kanyal : GAMBIT */
// Standard includes
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<string.h>

//Data Structures
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>

using namespace std;

#define FOR(i,a,b) 	for(int i= (int )a ; i < (int )b ; ++i)
#define fill(x,v)	memset(x,v,sizeof(x))
#define	sd(n)		scanf("%d",&n)
#define slld(n)		scanf("%lld",&n)
#define sf(n)		scanf("%lf",&n)
#define ss(n)		scanf("%s",n)
#define MOD 1000000007

typedef long long LL;

#define SORT(A) sort(A.begin(),A.end())

int check(char a[4][4],int n){
	char ch;
	int count1 = 0,count2 = 0,count3 = 0,count4 = 0;
	if(n == 0)
		ch = 'X';
	else
		ch = 'O';
	for(int i=0;i<4;i++){
		count1 = 0;
		count2 = 0;
		for(int j=0;j<4;j++){
			if(a[i][j] == ch || a[i][j] == 'T')
				count1++;
			if(a[j][i] == ch || a[j][i] == 'T')
				count2++;
		}
		if(a[i][i] == ch || a[i][i] == 'T')
			count3 ++;
		if(a[i][3-i] == ch || a[i][3-i] == 'T')
			count4 ++;
		if(count1 == 4 || count2 == 4 || count3 == 4 || count4 == 4)
			return 1;
	}
}

int checkComplete(char a[4][4]){
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(a[i][j] == '.')
				return 0;
		}
	}
	return 1;
	
}
int main()
{
	int t,ans1,ans0;
	cin >> t;
	char a[4][4] ;
	for(int x = 1;x <=t ;x++){
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>a[i][j];
			}
		}
		
		ans0 = check(a,0);
		ans1 = check(a,1);
		if (ans0 == 1)
			cout<<"Case #"<<x<<": "<<"X won"<<endl;
		else if (ans1 == 1)
			cout<<"Case #"<<x<<": "<<"O won"<<endl;
		else if(ans1 == 0 && ans0 == 0)
			if(checkComplete(a))
				cout<<"Case #"<<x<<": "<<"Draw"<<endl;
			else	
				cout<<"Case #"<<x<<": "<<"Game has not completed"<<endl;
	}
	return 0;
}
