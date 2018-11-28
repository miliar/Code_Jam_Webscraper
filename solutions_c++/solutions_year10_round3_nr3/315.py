#include<iostream>
#include<vector>
#include<queue>
#include<set>
#include<cstdio>
#include<algorithm>
#include<string>
#include<map>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<stack>
using namespace std;

int T,i,j,k;
string z[17];

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cin >> T;
	z[0]="0000";
	for (i=1;i<16;i++) {
		string d="";
		int num=i;
		while (num>0) {
			d+=(num%2)+'0';
			num/=2;
		}
		reverse(d.begin(),d.end());
		int len=d.length();
		for (j=0;j<4-len;j++)
			d="0"+d;
		z[i]=d;
	}
	for (int ii=0;ii<T;ii++) {
		int n,m;
		cin >> m >> n;
		vector<string> a; 
		int col[33][33],row[33][33];
		bool fin[33][33][33];
		string str,str1;
		for (i=0;i<m;i++) {
			str1="";
			cin >> str;
			for (j=0;j<str.length();j++) {
				if (str[j]>='0' && str[j]<='9') {
					str1+=z[str[j]-'0'];
				} else {
					str1+=z[(str[j]-'A')+10];
				}
			}
			a.push_back(str1);
		}
		int res[33];
		for (i=0;i<33;i++)
			res[i]=0;
		while (true) {
			int maxx=1,lx,ly;
			for (i=0;i<m;i++)
				for (j=0;j<n;j++)
					for (k=1;k<=max(n,m);k++) {
						col[i][j]=1;
						row[i][j]=1;
						fin[i][j][k]=false;
						if (a[i][j]!='2')
							fin[i][j][1]=true;
					}
			for (i=0;i<m;i++)
				for (j=0;j<n;j++) {
					if (i-1>=0 && ((a[i][j]=='0' && a[i-1][j]=='1') || (a[i][j]=='1' && a[i-1][j]=='0'))) {
						col[i][j]=col[i-1][j]+1;
					} else
						col[i][j]=1;
					if (j-1>=0 && ((a[i][j]=='0' && a[i][j-1]=='1') || (a[i][j]=='1' && a[i][j-1]=='0'))) {
						row[i][j]=row[i][j-1]+1;
					} else 
						row[i][j]=1;
				}
			for (k=2;k<=max(n,m);k++)
				for (i=1;i<m;i++)
					for (j=1;j<n;j++)
					if (fin[i-1][j-1][k-1] && a[i-1][j-1]==a[i][j] && col[i][j]>=k && row[i][j]>=k) {
						fin[i][j][k]=true;
						if (k>maxx) {maxx=k; ly=i; lx=j; }
					}
			if (maxx==1) {
				for (i=0;i<m;i++)
					for (j=0;j<n;j++)
						if (fin[i][j][1]) res[1]++;
				break;
			} else {
				for (i=ly-maxx+1;i<=ly;i++) {
					for (j=lx-maxx+1;j<=lx;j++) {
						a[i][j]='2';
					}
				}
				res[maxx]++;
			}
		}
		int count=0;
		for (i=max(m,n);i>=1;i--)
			if (res[i]!=0) count++;
		cout << "Case #" << ii+1 << ": " << count << endl;
		for (i=max(m,n);i>=1;i--)
			if (res[i]!=0) cout << i << " " << res[i] << endl;
	}

	return 0;
}
