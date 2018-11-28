
//Problem A. 

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <cmath>

using namespace std;

int n;
char mapchar[200];
char instr[100];
char res[100];

void compute(){
	int i,j,k;
	for (i=0;i<strlen(instr);i++){
		res[i]=mapchar[instr[i]];
	}
}

int main(){
	int t;
	int i,j,k;
	char a1[100],a2[100],a3[100];
	char b1[100],b2[100],b3[100];
	
	sprintf(a1,"ejp mysljylc kd kxveddknmc re jsicpdrysi");
	sprintf(a2,"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	sprintf(a3,"de kr kd eoya kw aej tysr re ujdr lkgc jv");
	sprintf(b1,"our language is impossible to understand");
	sprintf(b2,"there are twenty six factorial possibilities");
	sprintf(b3,"so it is okay if you want to just give up");
	mapchar[(int)'z']='q';
	mapchar[(int)'q']='z';
	for (i=0;i<strlen(a1);i++) mapchar[a1[i]]=b1[i];
	for (i=0;i<strlen(a2);i++) mapchar[a2[i]]=b2[i];
	for (i=0;i<strlen(a3);i++) mapchar[a3[i]]=b3[i];

	//for (i=0;i<26;i++) printf("%c %c\n",'a'+i,mapchar['a'+i]);

	cin>>t;
	gets(instr);
	for (i=0;i<t;i++){
		gets(instr);
			
		compute();
		cout<<"Case #"<<(i+1)<<": ";
		//for (j=0;j<n;j++) cout<<rpi[j]<<endl;
		for (j=0;j<strlen(instr);j++) printf("%c",res[j]);
		printf("\n");
		//for (j=0;j<n;j++) printf("%f %f %f %.10f\n",wp[j],owp[j],oowp[j],rpi[j]);
	}
}
