#include<iostream>
#include<vector>
#include<string>
#include<cmath>
#include<algorithm>
#include<sstream>
#include<stdio.h>
#include<string.h>
#define fr(i,a,b) for(i=a;i<=b;i++)
using namespace std;
int i,j,n,c,d,ti,ca,len;
char combine[256][256];
bool oppose[256][256];
string s,now;
int main(){
	freopen("b2.in","r",stdin);
	freopen("b2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		memset(combine,0,sizeof(combine));
		memset(oppose,0,sizeof(oppose));
		cin>>c;
		while(c--){
			cin>>s;
			combine[s[1]][s[0]]=combine[s[0]][s[1]]=s[2];
		}
		cin>>d;
		while(d--){
			cin>>s;
			oppose[s[1]][s[0]]=oppose[s[0]][s[1]]=true;
		}
		cin>>n;
		cin>>s;
		now="";
		fr(i,0,n-1){
			now=now+s[i];
			len=now.size();
			if(len>=2&&combine[now[len-1]][now[len-2]]>0)
				now=now.substr(0,len-2)+combine[now[len-1]][now[len-2]];
			else
				fr(j,0,len-2)
					if(oppose[now[j]][now[len-1]]){
						now="";
						break;
					}			
		}
		cout<<"Case #"<<ti<<": [";
		if(!now.empty()){
			cout<<now[0];
			fr(i,1,(int)now.size()-1)
				cout<<", "<<now[i];
		}
		cout<<"]"<<endl;
	}
}