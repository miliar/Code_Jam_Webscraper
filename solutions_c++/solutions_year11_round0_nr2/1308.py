#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <queue>
#include <cmath>
using namespace std;
int main()
{
freopen("out.txt","w",stdout);
freopen("in.txt","r",stdin);
int t;
bool f;
scanf("%d",&t);
int z,resn,tmp,k;
string inv[64]; string opp[32];
string str,res,res1;
int c=0,d=0,n=0;
for(int j=1; j<=t; j++){
c=0;d=0;n=0;
cin>>c;
for(int i=0;i<c;i++)
	cin>>inv[i];
cin>>d;
for(int i=0;i<d;i++)
	cin>>opp[i];
cin>>n;
cin>>str;
res+=str[0];
for (int i=1; i<n; i++){
	f=false;
	if(res.length()>0)
		resn=res.length()-1;
		else resn=0;
	k=0;
	while(k<c&&!f){
		if(res[resn]==inv[k][0]&&str[i]==inv[k][1]){
			res.erase(res.end()-1);
			res+=inv[k][2];
			f=true;
			}
		if(res[resn]==inv[k][1]&&str[i]==inv[k][0]){
			res.erase(res.end()-1);
			res+=inv[k][2];
			f=true;
			}
		k++;
		}
	if(!f)
		for(int l=0; l<d; l++){
			if(!f){
			z=resn;
			tmp=2;
			if (str[i]==opp[l][0]) 
				tmp=1;
			if (str[i]==opp[l][1]) 
				tmp=0;
			if (tmp!=2)
				while(z>=0){
					if (res[z]==opp[l][tmp]) {res=" ";f=true;break;}
					else z--;}
			}}
	if(!f)res+=str[i];
	}
while((*res.begin())==' ')res.erase(res.begin());
if (res.length()>0)
res1+=res[0];
for (int i=1; i<res.length(); i++){
res1+=", ";
res1+=res[i];}
res1+="]";
cout<<"Case #"<<j<<": ["<<res1<<endl;
str.clear();
res.clear();
res1.clear();
for(int i=0;i<c;i++)
	inv[i].clear();
for(int i=0;i<d;i++)
	opp[i].clear();
}
return 0;}
