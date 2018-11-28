#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<stdio.h>
#include<string.h>

using namespace std;

bool isugly(long long int num){
	if (num<0) num=-num;
	if(num==0) return 1;

	int two=(num%2==0);
	int three=(num%3==0);
	int five=(num%5==0);
	int seven=(num%7==0);
 
	if(two+three+five+seven==0) return 0;
	else return 1;
}

long long int atoLL(char* str){
	int len=strlen(str);
	int zero=int('0');
	long long int result=0;
	for(int i=0;i<len;i++){
		result=result*10;
		result=result+str[i]-zero;
	}
	return result;
}

long long int testugly(char* str,int* sign,int idx,int len){
	long long int tmp;
	long long int evalnum;
	int last;
	tmp=0;
	char evalstr[1000];
	if(idx==len-1){
		// sum all
		last=len-1;
		evalnum=0;
		int seglen;
		int i;
		for(i=len-2;i>=0;i--){
			if(sign[i]!=0){
				seglen=last-i;
				strncpy(evalstr,str+i+1,seglen);
				evalstr[seglen]='\0';
				last=i;
				if(sign[i]==1)evalnum=evalnum+atoLL(evalstr);
				else if(sign[i]==-1)evalnum=evalnum-atoLL(evalstr);
			}
		}
		seglen=last-i;
		strncpy(evalstr,str+i+1,seglen);
		evalstr[seglen]='\0';
		last=i;
		evalnum=evalnum+atoLL(evalstr);
		
		// test isugly
		if(isugly(evalnum)==1)tmp++;
	}
	else{
		// test +1
		sign[idx]=1;
		tmp+=testugly(str,sign,idx+1,len);
		// test 0
		sign[idx]=0;
		tmp+=testugly(str,sign,idx+1,len);
		// test -1
		sign[idx]=-1;
		tmp+=testugly(str,sign,idx+1,len);
	}
	
	return tmp;
}
int main(int argc,char** argv){
	int cases;
	long long int result;
	char str[1000];
	int sign[1000];
	scanf("%d",&cases);
	int i;
	for(i=0;i<1000;i++)sign[i]=0;
	for(i=0;i<cases;i++){
		scanf(" %s",str);
		// printf("%s",str);
		int len=strlen(str);
		result=testugly(str,sign,0,len);
		cout << "Case #" << i+1 << ": " << result << endl;
	}
}
