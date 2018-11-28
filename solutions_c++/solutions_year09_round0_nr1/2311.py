#include<iostream>
#include<string>
using namespace std;
int main()
{
	int i,j,k,l,d,n,l1,cnt,found;
	string lang[5000],test[500],groups[15];
	scanf("%d %d %d",&l,&d,&n);
	for(i=0;i<d;++i)
		cin>>lang[i];

	for(i=0;i<n;++i){
		cin>>test[i];
		l1=test[i].size();
		k=-1;
		for(j=0;j<l1;++j){
			groups[++k]="";
			if(test[i][j]=='(')
				while(test[i][++j]!=')')
					groups[k]+=test[i][j];	
			else
				groups[k]=test[i][j];
		}		
		cnt=0;
		for(k=0;k<d;++k){
			for(j=0;j<l;++j){
				found=groups[j].find(lang[k][j]);
				if(found==string::npos)
					break;
			}
			if(j==l)++cnt;
		}
		printf("Case #%d: %d\n",i+1,cnt);
	}
	return 0;
}
