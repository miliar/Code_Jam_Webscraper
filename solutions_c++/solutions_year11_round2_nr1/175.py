#include<stdio.h>
#include<iostream>
#include<vector>
#include<math.h>
#include<algorithm>
#include<memory.h>
#include<map>
#include<queue>

using namespace std;



int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);	
	int t=0;
	cin >> t;
	cout.precision(6);
	for (int e=1;e<=t;e++){
		int n;
		char a[111][111];
		long double s1,s2,q1[111],q2[111],q3[111],k[111];
		cin >> n;
		for (int i=0;i<n;i++)for (int j=0;j<n;j++)cin >> a[i][j];
		for (int i=0;i<n;i++){
			s1=0;
			s2=0;
			for (int j=0;j<n;j++)if (a[i][j]!='.'){
				s2++;
				if (a[i][j]=='1')s1++;
			}
			q1[i]=s1/s2;
			k[i]=s2;
		}
		for (int i=0;i<n;i++){
			s1=0;
			s2=0;
			for (int j=0;j<n;j++)if (a[i][j]!='.'){
				s2++;
				if (a[j][i]=='1')s1+=(q1[j]*k[j]-1)/(k[j]-1);else s1+=q1[j]*k[j]/(k[j]-1);
			}
			q2[i]=s1/s2;
		}
		for (int i=0;i<n;i++){
			s1=0;
			s2=0;
			for (int j=0;j<n;j++)if (a[i][j]!='.'){
				s2++;
				s1+=q2[j];
			}
			q3[i]=s1/s2;
		}
		cout << "Case #" << e << ":" << endl;
		for (int i=0;i<n;i++)cout << fixed << (q1[i]*0.25+q2[i]*0.5+q3[i]*0.25) << endl;
	}
	return 0;
}


