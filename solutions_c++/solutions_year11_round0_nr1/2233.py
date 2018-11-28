#include<iostream>
#include<complex>
#include<vector>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstdio>
#include<memory.h>
using namespace std;
int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t,k=0;
	cin >> t;
	for (;t;t--){

		int n, x[110], p1=1, p2=1, next_b[110], next_o[110];
		char c[110];
		cin >> n;
		for (int i=0; i<n; i++)
			cin>>c[i]>>x[i];
		int res=0;
		for (int i=0; i<n; i++){
			next_o[i]=next_o[max(i-1,0)];
			next_b[i]=next_b[max(i-1,0)];
			for (int j=i+1; j<n; j++)
				if (c[j]=='O'){
					next_o[i]=j;
					break;
				}

			for (int j=i+1; j<n; j++)
				if (c[j]=='B'){
					next_b[i]=j;
					break;
				}

		}
		for (int i=0; i<n; i++){
			if (c[i]=='O'){
				int y=abs(x[i]-p1)+1;
				res+=y;
				if (x[next_b[i]]>=p2)
					p2=min(p2+y,x[next_b[i]]);
				else
					p2=max(p2-y,x[next_b[i]]);
				p1=x[i];
			}
			else{
				int y=abs(x[i]-p2)+1;
				res+=y;
				if (x[next_o[i]]>=p1)
					p1=min(p1+y,x[next_o[i]]);
				else
					p1=max(p1-y,x[next_o[i]]);
				p2=x[i];
			}
		}
		k++;
		cout<<"Case #" << k << ": " << res << endl; 
	}

    return 0;
}