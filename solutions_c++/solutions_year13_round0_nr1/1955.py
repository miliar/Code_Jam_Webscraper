#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
string s[4];
bool tox_X(int t){for(int i=0;i<4;i++) if(s[t][i]!='X' && s[t][i]!='T') return false;return true;}
bool tox_O(int t){for(int i=0;i<4;i++) if(s[t][i]!='O' && s[t][i]!='T') return false;return true;}
bool sOun_X(int t){for(int i=0;i<4;i++) if(s[i][t]!='X' && s[i][t]!='T') return false;return true;}
bool sOun_O(int t){for(int i=0;i<4;i++) if(s[i][t]!='O' && s[i][t]!='T') return false;return true;}
bool ank1_X(){for(int i=0;i<4;i++) if(s[i][i]!='X' && s[i][i]!='T') return false;return true;}
bool ank1_O(){for(int i=0;i<4;i++) if(s[i][i]!='O' && s[i][i]!='T') return false;return true;}
bool ank2_X(){for(int i=0;i<4;i++) if(s[i][3-i]!='X' && s[i][3-i]!='T') return false;return true;}
bool ank2_O(){for(int i=0;i<4;i++) if(s[i][3-i]!='O' && s[i][3-i]!='T') return false;return true;}
void solve()
{
	int i,j;
	s[3]=s[2]=s[1]=s[0]="";
	for(i=0;i<4;i++) cin>>s[i];
	for(i=0;i<4;i++) {if(tox_X(i)) {cout<<"X won\n";return;} if(tox_O(i)){cout<<"O won\n";return;}}
	for(i=0;i<4;i++) {if(sOun_X(i)) {cout<<"X won\n";return;} if(sOun_O(i)){cout<<"O won\n";return;}}
	if(ank1_X() || ank2_X()) {cout<<"X won\n";return;} if(ank1_O() || ank2_O()){cout<<"O won\n";return;}
	for(i=0;i<4;i++) for(j=0;j<4;j++) if(s[i][j]=='.') {cout<<"Game has not completed\n";return;}
	cout<<"Draw\n";
}
int main()
{
	freopen("2.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i,n;
	cin>>n;
	for(i=0;i<n;i++){cout<<"Case #"<<i+1<<": "; solve();}
	return 0;
}