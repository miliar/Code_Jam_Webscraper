#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <stack>
#include <vector>
#include <math.h>
#include <iomanip>
#include <map>      // std::pair

#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s)-1; i>=(e); i--)
#define CLR(a,x) memset(a, x, sizeof(a))
#define SIZE(v) ((int)(v).size())
#define FOREACH(i,v) for(typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
typedef long long ll;
typedef std::pair<ll,ll> PII;
//typedef vector<PII> VPII;
using namespace std;


int main(){
#ifndef ONLINE_JUDGE
	freopen("d.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int t;
	int a[4][4];
	string s;
	cin>>t;
	FOR(tt,0,t){
		CLR(a,0);
		FOR(j,0,4){
			cin>>s;
			FOR(k,0,s.length()){
				if (s[k]=='X')	a[j][k]=1;
				else if (s[k]=='O')	a[j][k]=2;
				else if (s[k]=='T')	a[j][k]=3;
			}
		}
		//cin>>s;//empty line
		cout<<"Case #"<<tt+1<<": ";

		bool yeah,end=false;int ans;
		FOR(i,0,4){			
			yeah=true;
			FOR(j,0,3){
				if (a[i][j]==0||a[i][j+1]==0){yeah=false;	break;}
				if (a[i][j]!=a[i][j+1] && a[i][j]!=3 && a[i][j+1]!=3){
					yeah=false; break;
				}
				if (a[i][j]!=3)	ans=a[i][j];
			}
			if (yeah){
				end=true;
				if (ans==1)	cout<<"X won"<<endl;
				else cout<<"O won"<<endl;
				break;
			}
		}
		if (end)	continue;

		
		FOR(j,0,4){			
			yeah=true;
			FOR(i,0,3){
				if (a[i][j]==0||a[i+1][j]==0){yeah=false;	break;}
				if (a[i][j]!=a[i+1][j] && a[i][j]!=3 && a[i+1][j]!=3)	{yeah=false; break;}
				if (a[i][j]!=3)	ans=a[i][j];
			}
			if (yeah){
				end=true;
				if (ans==1)	cout<<"X won"<<endl;
				else cout<<"O won"<<endl;
				break;
			}
		}
		if (end)	continue;
		
		yeah=true;
		FOR(i,0,3){
			if (a[i][i]==0||a[i+1][i+1]==0){yeah=false;	break;}
			if (a[i][i]!=a[i+1][i+1] && a[i][i]!=3 && a[i+1][i+1]!=3)	{yeah=false; break;}
			if (a[i][i]!=3)	ans=a[i][i];
		}
		if (yeah){
			end=true;
			if (ans==1)	cout<<"X won"<<endl;
			else cout<<"O won"<<endl;
		}
		if (end)	continue;

		yeah=true;
		FOR(i,0,3){
			if (a[i][3-i]==0||a[i+1][2-i]==0){yeah=false;	break;}
			if (a[i][3-i]!=a[i+1][2-i] && a[i][3-i]!=3 && a[i+1][2-i]!=3)	{yeah=false; break;}
			if (a[i][3-i]!=3)	ans=a[i][3-i];
		}
		if (yeah){
			end=true;
			if (ans==1)	cout<<"X won"<<endl;
			else cout<<"O won"<<endl;
		}
		if (end)	continue;

		FOR(i,0,4)
			FOR(j,0,4)
			if (!end && a[i][j]==0)	{
				cout<<"Game has not completed"<<endl;
				end=true;
			}
		if (!end)	cout<<"Draw"<<endl;

	}

	return 0;

}