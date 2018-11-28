#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <vector>
#include <math.h>
#include <queue>
#include <stack>
#include <map>

#define abs(a) (a>=0)?a:(-a)

using namespace std;

int main()
{
	int T,j,i,code[50],cnt,mark[50];
	long long int tmp,ans;
	char a[100];
	FILE * pf = fopen("A-large.in","r");
	FILE * rf = fopen("Aans.in","w");
	fscanf (pf,"%d",&T);
	for (i=0; i<T; i+=1)
	{
		fscanf (pf,"%s",a);
		//cout<<"hi"<<endl;
		for (j=0; j<36; j+=1)
		{
			mark[j]=0;
		}
		cnt=0;
		//cout<<"hi"<<endl;
		for (j=0; j<strlen(a); j+=1)
		{
			if (a[j]>='a' && a[j]<='z' && mark[a[j]-'a'+10]==0)  {cnt++; mark[a[j]-'a'+10]=1;}
			else if (a[j]>='0' && a[j]<='9' && mark[a[j]-'0']==0) {cnt++; mark[a[j]-'0']=1;}
		}
		if (cnt==1) cnt++;
		for (j=0; j<36; j+=1)
		{
			code[j]=-1;
		}
		if (a[0]>='a' && a[0]<='z') code[a[0]-'a'+10]=1;  
		else if (a[0]>='0' && a[0]<='9') code[a[0]-'0']=1;
		tmp=0; 
		//cout<<"hi "<<cnt<<endl;
		for (j=1; j<strlen(a); j+=1)
		{
			if (a[j]>='a' && a[j]<='z' && code[a[j]-'a'+10]==-1) {code[a[j]-'a'+10]=tmp; 
			if (tmp==0) tmp=2; 
			else tmp++;
			}  
			else if (a[j]>='0' && a[j]<='9' && code[a[j]-'0']==-1) {code[a[j]-'0']=tmp; 
			if (tmp==0) tmp=2; 
			else tmp++;
			}
		}
		
		tmp=1; ans=0;
		for (j=strlen(a)-1; j>=0; j-=1)
		{
			if (a[j]>='a' && a[j]<='z') {ans+=tmp*code[a[j]-'a'+10]; /*cout<<code[a[j]-'a'+10]<<endl;*/}
			else if (a[j]>='0' && a[j]<='9') {ans+=tmp*code[a[j]-'0']; /*cout<<code[a[j]-'0']<<endl;*/}
			tmp*=cnt;
		}
		fprintf(rf,"Case #%d: %lld\n",i+1,ans);
	}
	return 0;
}
