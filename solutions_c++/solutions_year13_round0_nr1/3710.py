//Data Structure includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
//Other Includes
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<sstream>
//some common functionn
#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
#define FOR(i,a,b)              for(int i=a;i<b;i++)
#define FORs(i,a,b)             for(int i=a;i>=b;i--)
#define fill(a,v)               memset(a,v,sizeof a)
#define abS(x)                  ((x)<0?-(x):(x))
#define mP                      make_pair
#define pB                      push_back
#define error(x)                cout << #x << " : " << (x) << endl
#define all(c)                  (c).begin(),(c).end()
// Input macros
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

// Output macros
#define p(n)                        printf("%d",n)
#define pc(n)                       printf("%c",n)
#define pl(n)                       printf("%lld",n)
#define pf(n)                       printf("%lf",n)
#define ps(n)                       printf("%s",n)

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<int,PII> TRI;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<PII> VII;
typedef vector<PLL> VLL;
typedef vector<TRI> VT;
typedef vector<VI> VVI;
typedef vector<VL> VVL;
typedef vector<VII> VVII;
typedef vector<VLL> VVLL;
typedef vector<VT> VVT;

using namespace std;

void chekarre(int * arr,int n)
{
    cout<<"[";
    for(int i=0;i<n;i++)
        cout<<arr[i]<<" ";
    cout<<"]"<<endl;
}


int n, m ;
string s[4], ow[4], xw[4];
int flag=0;
int xcnt=0, ocnt=0;
int solve()
{
	/*
	cout<<endl;
	FOR(i,0,4)
		{
		FOR(j,0,4)
		{
			cout<<s[i][j];
		}
		cout<<endl;
		
		}
	cout<<endl;
	FOR(i,0,4)
		{
		FOR(j,0,4)
		{
			cout<<ow[i][j];
		}
		cout<<endl;
		
		}
	cout<<endl;
	FOR(i,0,4)
		{
		FOR(j,0,4)
		{
			cout<<xw[i][j];
		}
		cout<<endl;
		
		}
		cout<<endl;
	*/
	
	FOR(i,0,4)
	{
		xcnt=0;
		ocnt=0;
		FOR(j,0,4)
		{
			if(xw[i][j]=='X')
			{
				xcnt++;
			}
			if(ow[i][j]=='O')
			{
				ocnt++;
			}
		}
		if(xcnt==4)
		{
	//		cout<<"------1\n";
			cout<<"X won";
			return 1;
		}
		if(ocnt==4)
		{
	//		cout<<"------2\n";
			cout<<"O won";
			return 1;
		}
	}
	
	FOR(i,0,4)
	{
		xcnt=0;
		ocnt=0;
		FOR(j,0,4)
		{
			if(xw[j][i]=='X')
			{
				xcnt++;
			}
			if(ow[j][i]=='O')
			{
				ocnt++;
			}
		}
		if(xcnt==4)
		{
	//		cout<<"------3\n";
			cout<<"X won";
			return 1;
		}
		if(ocnt==4)
		{
	//		cout<<"------4\n";
			cout<<"O won";
			return 1;
		}
	}
	xcnt=0, ocnt=0;
	FOR(i,0,4)
	{
				if(xw[i][i]=='X')
				{
					xcnt++;
				}
				if(ow[i][i]=='O')
				{
					ocnt++;
				}
	}
		if(xcnt==4)
		{
	//		cout<<"------5\n";
			cout<<"X won";
			return 1;
		}
		if(ocnt==4)
		{
	//		cout<<"------6\n";
			cout<<"O won";
			return 1;
		}
	xcnt=0, ocnt=0;
	
	FOR(i,0,4)
	{
		FOR(j,0,4)
		{
			if((i+j)==3)
			{
	//			error(i);error(j);
				if(xw[i][j]=='X')
				{
					xcnt++;
				}
				if(ow[i][j]=='O')
				{
					ocnt++;
				}
			}
		}
	}
	//error(xcnt);error(ocnt);
		if(xcnt==4)
		{
	//		cout<<"------7\n";
			cout<<"X won";
			return 1;
		}
		if(ocnt==4)
		{
	//		cout<<"------8\n";
			cout<<"O won";
			return 1;
		}
	
	FOR(i,0,4)
	{
		FOR(j,0,4)
		{
			if(s[i][j]=='.')
			{
				cout<<"Game has not completed";
				return 1;
			}
		}
	}
	cout<<"Draw";

    return 1;
}

bool input()
{
	FOR(i,0,4)
	{
		cin>>s[i];
	}
	FOR(i,0,4)
		FOR(j,0,4)
		{
			ow[i][j]='.';
			xw[i][j]='.';
		}
	FOR(i,0,4)
		FOR(j,0,4)
		{
			if(s[i][j]=='T')
			{
				ow[i][j]='O';
				xw[i][j]='X';
			}
			else if(s[i][j]=='O')
			{
				ow[i][j]='O';
			}
			else if(s[i][j]=='X')
			{
				xw[i][j]='X';
			}
		}
	return true;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T=1;
    s(T);
    for(int testnum=1;testnum<=T;testnum++)
    {
        if(!input()) break;
		cout<<"Case #"<<testnum<<": ";
        solve();
        printf("\n");

    }
//    system("pause");
    return 0;
}




