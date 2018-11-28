#include <iostream>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define LLI long long int
#define ULL unsigned long long int
#define VI vector<int>
#define VS vector<string>
#define SZ(x) x.size()
#define CL(x) x.clear()
#define PB push_back
#define dmax(A,B) ((A)>(B)?(A):(B))
#define dmin(A,B) ((A)<(B)?(A):(B))

int main()
{
	int i,j,k,l,n,m,res;
	int t,T;
	vector<string> v;
	vector<string> x;
	string st,tst,xst,yst;
	bool flag;
	
	cin>>T;
	
	for(t=1;t<=T;t++){
		cin>>n>>m;
		v.clear();
		x.clear();
		res=0;
		for(i=0;i<n;i++){
			cin>>st;
			v.push_back(st);
		}
		for(i=0;i<m;i++){
			cin>>st;
			l=st.length();
			j=1;
			while(j<l){
				if(st[j]=='/'){
					tst=st.substr(0,j);
					x.push_back(tst);
				}
				j++;
			}
			x.push_back(st);
		}
		
		sort(x.begin(),x.end());
		
		//for(i=0;i<x.size();i++)
		//	cout<<x[i]<<endl;
		
		l=x.size();
		for(i=0;i<l;i++){
			flag=true;
			k=v.size();
			for(j=0;j<k;j++){
				if(v[j]==x[i]){
					flag=false;
					break;
				}
			}
			if(flag){
				res=res+1;
				v.push_back(x[i]);
			}
		}
			
		printf("Case #%d: %d\n",t,res);
	}
		
	
	return 0;
}