#include<iostream>
#include<cmath>
#include<stdio.h>
#include<cstring>
#include<map>
#include<string>
#include<algorithm>
using namespace std;
const int N = 45 ;
const int M = 35 ;
const int INF = 10005 ;
const double eps = 1e-8 ;
#define ll __int64
int n , m ;
typedef pair<int,int> P;

string com[N], opp[N];
int c, d;
string ans ;

void slove(string opt)
{
	int i, j , k,  sz = opt.size();
	char last ;
	bool f1, f2;

    ans = "";
    for (i = 0; i < sz ; i++)
    {
		if ( ans.size() > 0 ) last = ans[ans.size() - 1] ;
		else last = char(0);
        f1 = false;
		f1 = false;
        for (j = 0; j < c; j++)
		{
            if (com[j][0] == last && com[j][1] == opt[i] || com[j][1] == last && com[j][0] == opt[i])
            {
                ans[ans.size() - 1] = com[j][2];
				f1 = true;
                break;
            }
		}
        for (j = 0; !f1 && !f1 && j < d; j++)
		{
            for (k = 0; !f1 && k < ans.size(); k++)
			{
                if (opp[j][0] == opt[i] && opp[j][1] == ans[k] || opp[j][1] == opt[i] && opp[j][0] == ans[k])
                {
                    ans = "", f1 = true;
                    break;
                }
			}
		}
        if (!f1 && !f1){
            ans += opt[i];
		}
    }
}

int main()
{
	int i, j, k, tmp, cas = 1, t , state ;
	string s ;

	for( scanf("%d" , &t ), cas = 1 ; cas <= t ; cas++ )
	{
        scanf("%d", &c ) ;
        for ( i = 0; i < c; i++){
			cin >> com[i] ;
        }
        scanf("%d", &d ) ;
        for ( i = 0; i < d; i++){
			cin >> opp[i] ;
        }
		cin >> n >> s ;
		slove(s) ;
		printf("Case #%d: [", cas ) ;
        for ( i = 0; i < ans.size(); i++)
		{
            if (i == 0){
                cout << ans[i];
			}
            else{
                cout << ", " << ans[i];
			}
		}
		puts("]") ;
	}

	return 0;
}