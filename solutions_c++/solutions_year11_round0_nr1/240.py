#include<iostream>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<cstring>
#include<string>
#include<sstream>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<cassert>
using namespace std;

typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef pair<int,int> pii;
typedef long long ll;

#define I ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i = a ; i <= b ; i++)
#define REV(i,a,b) for(int i = a ; i >= b ; i--)
#define REP(i,n) for(int i = 0 ; i < n ; i++)

#define INF 1000000000

vi O,B;
int T,N;
int cas=0;
int ev[105];
char col[105];

int move(int cur, int fin,  int time)
{
	int tcur = cur;
	if(cur <= fin)
		cur += time;
	else
		cur -= time;

	if( abs(tcur-fin) <= time )
		cur = fin;
	return cur;
}

void solve()
{
	int curb = 1,curo = 1;
	int posb = 0,poso = 0;
	int leno = O.size();
	int lenb = B.size();
	int tot=0;
	FOR(i,1,N)
	{
		char c = col[i];
		int temp = ev[i];
		if( c == 'O' )
		{
			int shift = abs(temp-curo) + 1;
			tot += shift;
			curo = temp;
			poso++;
			if(posb < lenb)
				curb = move(curb, B[posb], shift);
			
		}
		else
		{
			int shift = abs(temp-curb) + 1;
			tot += shift;
			curb = temp;
			posb++;
			if(poso < leno)
				curo = move(curo, O[poso] , shift);
		}
		//cout<<tot<<" "<<curb<<" "<<posb<<" "<<curo<<" "<<poso<<endl;
	}
	cout<<"Case #"<<cas<<": "<<tot<<endl;
}

int main()
{
	cin>>T;
	while(T--)
	{
		cas++;
		cin>>N;
		O.clear();
		B.clear();
		FOR(i,1,N)
		{
			int temp;
			string c;
			cin>>c;
			cin>>temp;
			col[i] = c[0];
			ev[i] = temp;
			if(c == "O")
				O.push_back(temp);
			else 
				B.push_back(temp);
		}
		solve();
	}


	return 0;
}
