#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<fstream>
#include<map>

using namespace std;

ofstream fout("a.out");

int count(int number,int lim){
	char arr[10],temp[10];
	map<string, int> checkList;
	sprintf(arr,"%d",number);
	int res=0;
	int len=strlen(arr);
	for(int i=0;i<len-1;++i){
		int k=0,j;
		for(j=i+1,k=0;j<len;++j,++k){
			temp[k]=arr[j];
		}
		for(j=0;j<=i;++j,++k){
			temp[k]=arr[j];
		}
		if(temp[0]=='0')
			continue;
		checkList[temp]=1;
	}
	map<string, int>::iterator it;
	for(it=checkList.begin();it!=checkList.end();it++){
		int no_obtained=atoi((*it).first.c_str());
		if(no_obtained<=lim && no_obtained>number){
			++res;
			//fout<<"("<<number<<" , "<<no_obtained<<")\n";
		}
	}
	return res;
}

int main(){
	int t,i=1;
	cin>>t;
	while(t-->0){
		int a,b,sum=0;
		cin>>a>>b;
		for(int i=a;i<=b;++i){
			sum+=count(i,b);
		}
		printf("Case #%d: %d\n",i,sum);
		++i;
	}
	fout.close();
}