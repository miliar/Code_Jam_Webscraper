#include<stdio.h>
#include<iostream>
#include <string.h>
#include<map>
using namespace std;
int mod(int a) {if(a<0) return -a; else return a;}
int zero(int a) {if(a<0) return 0; else return a;}
int main()
{
	int a,b,c,d=0,t;
	
	char g,h,i[4],j,m[103],f[103];
	string q,r;
	cin>>t;
	for(int k=1;k<=t;k++)
	{	map< string, char> w;
		multimap < char, char> ex;
		map<string,char>::iterator it;
		multimap<char,char>::iterator it1;
  		pair<multimap<char,char>::iterator,multimap<char,char>::iterator> ret;

		cin>>b;
		for(int l=0;l<b;l++)
		{
			scanf("%s",i);
			g=i[2];i[2]='\0';q=i;j=i[0];i[0]=i[1];i[1]=j;r=i;			
			w[q]=g;w[r]=g;
		}
		cin>>b;	
		for(int l=0;l<b;l++)
		{	
			cin>>g>>h;	
			ex.insert(pair<char,char>(g,h));ex.insert(pair<char,char>(h,g));
			
		}
		cin>>b;
		cin>>m;
		int flag=1;
		while(flag==1){
		flag=0;
		f[0]=m[0];
		int e=1,big=0;;
		for(int l=1;l<b;l++){
			big=0;
			i[0]=m[l];i[1]=m[l-1];i[2]='\0';q=i;
			it=w.find(q);
			if(it!=w.end()) {f[--e]=it->second;flag=1;big=1;e++;}
			else  { big=0;ret = ex.equal_range(m[l]); for(d=e-1;d>=0;d--){ for (it1=ret.first; it1!=ret.second; ++it1) if((*it1).second==f[d])
			{e=0;flag=1;big=1;break;}if(big==1) break;} }if(big!=1) {f[e++]=m[l];} else {f[e]='\0';strcat(f,m+l+1);strcpy(m,f);b=strlen(f);m[strlen(f)]='\0';break;}
			
		}}
		cout<<"Case #"<<k<<": [";
		if(strlen(m)>0){
		for(int l=0;l<strlen(m)-1;l++) cout<<m[l]<<", ";
		 cout<<m[strlen(m)-1];} cout<<"]\n";
	}
}

