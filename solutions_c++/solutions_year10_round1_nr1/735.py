#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;
int  sp(int m[][200],int q, int x,int y, int dx, int dy ) {
  int ans = 0 ;
  while (m[x+ans*dx][y+ans*dy]==q) ans++;
 // cout << x<<y<<" "<<dx << " "<<dy<<ans<<" "<<q<< endl;
  return ans;
}
bool lr(int m[][200],int q,int n,int k ) {
	for (int i = 1; i<=n; i++)
		for (int j = 1; j<=n; j++)
		{
			if (sp(m,q,i,j,0,1)>=k) return true;
            if (sp(m,q,i,j,0,-1)>=k) return true;
			if (sp(m,q,i,j,1,0)>=k) return true;
            if (sp(m,q,i,j,-1,0)>=k) return true;
			if (sp(m,q,i,j,1,1)>=k) return true;
            if (sp(m,q,i,j,-1,-1)>=k) return true;
			if (sp(m,q,i,j,1,-1)>=k) return true;
            if (sp(m,q,i,j,-1,1)>=k) return true;
		}
	return false;
}
int main()
{
	int map[200][200];
	int n0; cin >> n0;
	for (int nn = 1;  nn<=n0; nn++) { 
		cout << "Case #"<<nn<<": ";
		string s;
		int n;
		int k ;
		memset(map,0,sizeof(map));
		cin >> n >> k;
		for (int i = 1; i<=n; i++) {
			cin >> s;
			int y = n;
			for (int j = n-1; j>=0; j--)
				if (s[j]!='.') {
					map[i][y--] = (s[j]=='R')?1:2;
				}
		}
	/*	for (int i = 1; i<=n; i++)
		{for (int j =1; j<=n; j++)
		cout << map[i][j];
		cout << endl;}
	*/	
		bool fl1 = lr(map,1,n,k);
		bool fl2 = lr(map,2,n,k);
		if (fl1 && fl2) cout <<"Both"<< endl;
		if ((!fl1) && fl2) cout <<"Blue"<< endl;
		if (fl1 && (!fl2)) cout <<"Red"<< endl;
		if ((!fl1) && (!fl2)) cout <<"Neither"<< endl;


	}
}