
//main includes
#include<iostream>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>


//other includes
#include<algorithm>
#include<climits>
#include<vector>
#include<queue>
#include<stack>
#include<bitset>
#include<set>
#include<deque>
#include<cstdlib>
#include<map>
#include <utility>

#define re



using namespace std;

#define FOR(a,b)        for(__typeof(b) i=(a);i<(b);i++)


// O == 2  8 7
// T == 1
// X == 5  20 16
// . == 20

int t;
int a[4][4];
bool flag;
void preprocess()
{
	char temp;
	flag = false;
	for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
		{
			cin>>temp;
			switch(temp)
			{
				case 'X': a[i][j] = 5;
				break;
				case 'O':a[i][j] = 2;
				break;
				case 'T':a[i][j] = 1;
				break;
				case '.':a[i][j] = 20;
				flag = true;
				break;
			}
		}
	/*for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		cout<<a[i][j]<<" ";
	cout<<endl;
}
	cout<<endl;*/

}
	

char check(int t)
{
	if(t==8 || t==7)
	{
		return 'O';
	}
	else if (t == 20 || t==16)
	{
		return 'X';
	}

	return ' ';
}

void solve()
{
	//check diagonal
	int t = a[0][0]+ a[1][1]+a[2][2]+a[3][3];
	if(check(t) != ' ')
	{cout<<check(t)<<" won"<<endl;
		return ;
	}
	t = a[0][3]+a[1][2]+a[2][1]+a[3][0];
	if(check(t)!= ' ')
		{cout<<check(t)<<" won"<<endl;
	return ;
	}


	//check rows
	for(int i=0;i<4;i++)
	{
		t=0;
		for(int j=0;j<4;j++)
			t += a[i][j];
		if(check(t)!= ' ')
		{
		cout<<check(t)<<" won"<<endl;
		return ;
		}

	}
		
		//for column
		for(int i=0;i<4;i++)
	{
		t=0;
		for(int j=0;j<4;j++)
			t += a[j][i];
	if(check(t)!=  ' '){
	cout<<check(t)<<" won"<<endl;
	return ;
	}
	}

	if(flag)
		cout<<"Game has not completed"<<endl;
	else
		cout<<"Draw"<<endl;
}


int main(){
#ifdef re
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
freopen("log.txt","w",stderr);
#endif
cin>>t;
for(int i=1;i<=t;i++)
{
	preprocess();
	cout<<"Case #"<<i<<": ";
	solve();
}
#ifdef re
//printf("\n  Time Taken  %.31f sec\n",(double)clock()/(CLOCKS_PER_SEC));

#endif
return 0;
}

