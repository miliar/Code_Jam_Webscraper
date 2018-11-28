#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<cstdlib>
#include<cstring>
#include<sstream>
#include<cassert>
using namespace std;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vb> vvb;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef pair<int,int> ii;
typedef pair<int,ii> pii;
typedef double ll;
#define sz(c) (int)c.size()
#define pb push_back
#define all(v) v.begin(),v.end()
#define inc(i,n) for(int i=0;i<n;i++)
#define dec(i,n) for(int i=n-1;i>=0;i--)
int main(){

	int nt;
	scanf("%d",&nt);
	for(int g=1;g<=nt;g++){
		int n;
		cin>>n;
		double arr[n][6];
		for(int i=0;i<n;i++){
			for(int j=0;j<6;j++){
				cin>>arr[i][j];
			}
		}
		vector<double> col;
		for(int i=0;i<6;i++){
			double sum=0;
			for(int j=0;j<n;j++){
				sum+=arr[j][i];
			}
			col.pb(sum);
		}
		double a=col[0]*col[0]+col[1]*col[1]+col[2]*col[2];
		double c=col[3]*col[3]+col[4]*col[4]+col[5]*col[5];
		double b=2*(col[0]*col[3]+col[1]*col[4]+col[2]*col[5]);
		swap(c,a);
		assert(a>=0 && c>=0);
		if(a==0){
			if(b>=0)
				printf("Case #%d: %0.8lf 0.00000000\n",g,sqrt(c)/(double)n);
			else{
				double t=-c/(double)b;
				printf("Case #%d:  0.00000000 %.8lf\n",g,t);
			}
			continue;
		}
		double ans;
		if(b>=0){
			assert(c>=0);
			ans=sqrt(c)/(double)n;
			printf("Case #%d: %.8lf 0.00000000\n",g,ans);

		}
		else{
			double t;
			if(b*b>=4*a*c){
				t=(-b+sqrt(b*b-4*a*c))/(double)(2*a);
				printf("Case #%d: 0.00000000 %.8lf\n",g,t);
			}
			else{
				t=-b/(double)(2*a);
				double dist=sqrt((a*t*t+b*t+c))/(double)n;
				printf("Case #%d: %.8lf %.8lf\n",g,dist,t);
			}

		}
	}
return EXIT_SUCCESS;

}
