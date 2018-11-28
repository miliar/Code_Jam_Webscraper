#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define forn(i,a,n) for(int i = (int) a; i < (int)n; i++) 

char s[1000][1000],ss[1000];
int x[1000];
int y[1000];

int main()
{
    freopen("d.in","rt",stdin);
    freopen("d.out","wt",stdout); 
	int n,q,ns;
	cin >> n;
	forn(nn,0,n)
	{
		cin >> ns;
		cin.getline(ss,1000);
		forn(i,0,ns)
		{
			cin.getline(ss,1000);
			strcpy(s[i],ss);
	//		strcat(s[i],"\n");
		}
		cin >> q;
		cin.getline(ss,1000);
		forn(i,0,q)
		{
			cin.getline(ss,1000);
			forn(j,0,ns) if ( strcmp( ss,s[j] ) == 0 ) { x[i] = j; break; }
		}
	/*	forn(i,0,ns)
		{
			strcpy(s[i],"");
			strcat(s[i],"\n");
		}
		strcpy(ss,"");
		strcat(ss,"\n");
		*/
		//forn(i,0,q) cout << x[i] <<" ";
		//cout << endl;
		forn(i,0,ns) y[i] = 0;
		int tt = 0;
		int res = 0;
		forn(i,0,q) 
		{
			if ( y[x[i]] == 0 ) { y[ x[i] ] = 1; tt++; }
			if ( tt == ns )
			{
				res++;
				tt = 1;
				forn(j,0,ns) y[j] = 0;
				y[ x[i] ] = 1;
			}
		}
		cout << "Case #" << nn + 1<<": " << res << endl;
	}
    return 0;
}

