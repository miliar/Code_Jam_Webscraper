#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<algorithm>
#include<memory.h>
#include<iomanip>
#include<cmath>
#include<fstream>
#include<map>
#include<ctime>
#include<queue>
using namespace std;

struct A{
	char c;
	int x;
}p[105];

int WORK(int a){
	if(a>0) return a;
	else return -a;
}

int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("out1.txt","w",stdout);
	int t,n,i,j;
	string s;
	cin>>t;
	for(int k=1;k<=t;k++){
		cin>>n;
		int now1=1,now2=1;
		for(i=0;i<n;i++){
			cin>>p[i].c>>p[i].x;
		}
		int ans=0;
		for(i=0;i<n;i++){
			if(p[i].c=='O'){
				int f=WORK(p[i].x-now1)+1;
				ans+=f;
				now1=p[i].x;
				for(j=i+1;j<n;j++){
					if(p[j].c=='B'){
						//cout<<"ÐÞ¸Ä2"<<endl;
						if(p[j].x>=now2){
							if(f+now2<=p[j].x) now2+=f;
							else now2=p[j].x;
						}else{
							if(now2-f>=p[j].x) now2-=f;
							else now2=p[j].x;
						}
						break;
					}
				}
				//cout<<"             "<<now1<<' '<<now2<<endl;
				//cout<<"  debu  "<<ans<<endl;
			}else if(p[i].c=='B'){
				int f=WORK(p[i].x-now2)+1;
				ans+=f;
				now2=p[i].x;
				for(j=i+1;j<n;j++){
					if(p[j].c=='O'){
						//cout<<"ÐÞ¸Ä1"<<endl;
						if(p[j].x>=now1){
							if(f+now1<=p[j].x) now1+=f;
							else now1=p[j].x;
						}else{
							if(now1-f>=p[j].x) now1-=f;
							else now1=p[j].x;
						}
						break;
					}
				}
				//cout<<"             "<<now1<<' '<<now2<<endl;
				//cout<<"  debu  "<<ans<<endl;
			}
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}




