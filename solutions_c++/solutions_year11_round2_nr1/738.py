#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstdio>
#include<map>
#define PI 3.1415926535897932384626433832795
using namespace std;
int main(){
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t;
	cin>>t;
	for (int q=0; q<t; q++){
		cout<<"Case #"<<q+1<<":"<<endl;
		int n;
		cin>>n;
		string s[100];
		double w1[200],w2[200],w3[200];
		for (int i=0; i<n; i++){
			cin>>s[i];
			int k1=0,k2=0;
			for (int j=0; j<n; j++)
				if (s[i][j]=='1')
					k1++;
				else
					if(s[i][j]=='0')
						k2++;
			w1[i]=(k1+0.0)/(k2+k1+0.0);
		}
		for (int z=0; z<n; z++){
			int k=0;
			double w=0;
			for (int i=0; i<n; i++)
			if (s[z][i]!='.'){
				int k1=0,k2=0;
				for (int j=0; j<n; j++)
					if (j!=z)
					if (s[i][j]=='1')
						k1++;
					else
						if(s[i][j]=='0')
							k2++;
				w+=(k1+0.0)/(k2+k1+0.0);
				k++;
			}
			if (k==0)
				w2[z]=0;
			else
				w2[z]=w/(k+0.0);
			//cout<<"   "<<w2[z]<<endl;
		}

		for (int i=0; i<n; i++){
			int k=0;
			double w=0;
			for (int j=0; j<n; j++)
				if (s[i][j]!='.'){
					k++;
					w+=w2[j];
				}
			w3[i]=w/(k+0.0);
			printf("%.6f\n",0.25*w1[i]+0.5*w2[i]+0.25*w3[i]);
		}
	}
	
return 0;
}