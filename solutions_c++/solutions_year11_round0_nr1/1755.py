#include<iostream>
#include<cstdio>
#include<vector>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<cmath>
#include<queue>
#include<cstring>
#include<string>
#include<algorithm>
//#include<nevertimelimited.h>
//#include<neverwronganswer.h>
//#include<accepted forever.h>
using namespace std;
int main(void){
	FILE * fp1=fopen("in.in","r");
	FILE * fp2=fopen("out.in","w");
	int t,k,n,p;
	char s[5];
	int pos,bpos,opos;
	int bt,ot,tem,ans;
	fscanf(fp1,"%d",&t);
	for(k=1;k<=t;k++){
		fscanf(fp1,"%d",&n);
		bpos=opos=1;
		ans=bt=ot=0;
		for(p=0;p<n;p++){
			fscanf(fp1,"%s%d",s,&pos);
			if(s[0]=='B') tem=max(pos-bpos,bpos-pos);
			else tem=max(pos-opos,opos-pos);
			tem++;
			if(s[0]=='B'){
				bpos=pos;
				ans+=max(1,tem-ot);
				bt+=max(1,tem-ot);
				ot=0;
			}
			else{
				opos=pos;
				ans+=max(1,tem-bt);
				ot+=max(1,tem-bt);
				bt=0;
			}
//			if(k==t)
//			cout<<ot<<"   "<<bt<<"   "<<tem<<"    "<<ans<<endl;    //
		}
//		printf("Case %d: %d\n",k,ans);    /////////////////////
		fprintf(fp2,"Case #%d: %d\n",k,ans);
	}
	system("pause");
	return 0;
}