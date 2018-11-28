#include"stdlib.h"
#include"stdio.h"
#include <string>
#include<cmath>
#include<iostream>
#include<fstream>
using namespace std;

int T,C,D,N;
int CMap[26][26],DMap[26][26];

int Produce(int start,int level,char *src,char *dst){
	char c=src[level],c1;
	int st=start;
	dst[start]=c;
	if(level==N){
		dst[start]=0;
		return start;
	}
	if(start==0){
		return Produce(1,level+1,src,dst);
	}
	c1=dst[start-1];
	while(CMap[c-'A'][c1-'A']!=-1){
		st--;
		dst[st]='A'+CMap[c-'A'][c1-'A'];
		if(st==0){
		return	Produce(1,level+1,src,dst);
			
		}
		c=dst[st];
		c1=dst[st-1];
	}
	st++;
	for(int i=0;i<st;i++)
	{	if(DMap[dst[i]-'A'][dst[st-1]-'A']==1){
		return	Produce(0,level+1,src,dst);
	}
		
	}
	return Produce(st,level+1,src,dst);

}

int main()
{
ifstream in;
ofstream out;
in.open("B-large.in");
out.open("OUTPUT.txt");
int i,j;
int endstep;
in>>T;
char s[102]={0};
char ans[102]={0};
for(int Cas=1;Cas<=T;Cas++){
	in>>C;
	for(i=0;i<26;i++)
		for(j=0;j<26;j++)
			CMap[i][j]=-1;
	for(i=0;i<C;i++){
		in>>s;
		CMap[s[0]-'A'][s[1]-'A']=s[2]-'A';
		CMap[s[1]-'A'][s[0]-'A']=s[2]-'A';
	}
	in>>D;
	for(i=0;i<26;i++)
		for(j=0;j<26;j++)
			DMap[i][j]=0;
	for(i=0;i<D;i++){
		in>>s;
		DMap[s[0]-'A'][s[1]-'A']=1;
		DMap[s[1]-'A'][s[0]-'A']=1;
	}
	in>>N;
	in>>s;
	endstep=Produce(0,0,s,ans);
	out<<"Case #"<<Cas<<": [";
	for(i=0;i<endstep-1;i++){
			if(i!=0)out<<' ';
		out<<ans[i]<<',';
	
	}
		if(i!=0)out<<' ';
	if(endstep>0)out<<ans[endstep-1];
	out<<']'<<endl;


}


in.close();
out.clear();
out.close();
return 0;
}