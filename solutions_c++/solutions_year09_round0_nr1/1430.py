#include<iostream>
#include<vector>
#include<string.h>
#define vs vector<string>
#define pb(v,k) v.push_back(k)
using namespace std;
int main()
{
	int i1,i11;
	int k,n,d,l,j1,tot,j2,end;
	vs myvec;
	scanf("%d%d%d",&l,&d,&n);	
	string s;
	for(i1=0;i1<d;i1++){
		cin>>s;
		myvec.push_back(s);
	}
	
	i1=0;
	while(i1<n){
		cin>>s;
		bool done[35][35];
		for(int i=0;i<35;i++){
			for(int ij=0;ij<35;ij++){
				done[i][ij]=0;
			
			}
		}
		j1=0;
		int sz11=myvec[0].size();
		int sz12=s.size();
		k=0;
		while(k<sz11){

			tot=0;
			if(s[j1]=='('){
				for(j2=j1+1;s[j2]!=')' && j2<sz12;j2++){
					done[k][s[j2]-97]=1;
				}
				j1=j2+1;
			}
			else{
				done[k][s[j1]-97]=1;
					j1++;
			}
			k++;
		}
		end=0;
		int sz13=myvec.size();
		i11=0;
		while(i11<sz13){

			tot=0;
			int sz14=myvec[i11].size();
			for(j1=0;j1<sz14;j1++){
				if(done[j1][myvec[i11][j1]-97])
					tot++;
			}
			if(tot==j1)
				end++;
			i11++;
		}
		cout<<"Case #"<<i1+1<<": "<<end<<endl;
		i1++;
	}	
	return 0;
}

