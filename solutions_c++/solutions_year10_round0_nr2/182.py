#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
typedef vector<int> NUM;

const int base=10000;

NUM num(int a){
	vector<int> ret;
	if(a==0)ret.push_back(0);
	while(a>0){ret.push_back(a%base);a/=base;}
	return ret;
}

NUM readnum(){
	char buf[1000];
	scanf(" %s",buf);
	int l=strlen(buf);
	int siz;
	NUM ret;
	
	for(int i=0;i<l;i++)if(i%4==0)ret.push_back(0);
	for(int i=0;i<l;i++){
		int dig=(int)(buf[l-1-i]-'0');
		if(i%4>=1)dig*=10;
		if(i%4>=2)dig*=10;
		if(i%4>=3)dig*=10;
		ret[i/4]=ret[i/4]+dig;
	}
	return ret;
}


void printnum(NUM a){
	int i;
	for(i=a.size()-1;i>=0 && a[i]==0;i--);
	if(i==-1)printf("0");
	else{
		printf("%d",a[i]);
		for(i--;i>=0;i--)printf("%04d",a[i]);
	}
}



NUM add(NUM a, NUM b){
	NUM c;
	int carry=0;
	for(int i=0;i<max(a.size(),b.size());i++){
		c.push_back(carry+a[i]+b[i]);
		if(c[i]>=base){c[i]-=base;carry=1;}
		else carry=0;
	}
	if(carry==1)c.push_back(1);
	return c;
}

int cmp(NUM a, NUM b){
	//printf("mod ");printnum(a);printf(",");printnum(b);puts("");
	//printf("%d %d\n",a.size(),b.size());
	for(int i=max(a.size(),b.size())-1;i>=0;i--){
		if(i>=a.size() && b[i]!=0)return -1;
		if(i>=b.size() && a[i]!=0)return 1;
		if(i<min(a.size(),b.size()) && a[i]<b[i])return -1;
		if(i<min(a.size(),b.size()) && a[i]>b[i])return 1;
	}
	return 0;
}

NUM subabs(NUM a, NUM b){
	if(cmp(a,b)==-1)swap(a,b);
	NUM c;
	int carry=0;
	for(int i=0;i<a.size();i++){
		if(i>=b.size())c.push_back(carry+a[i]);
		else c.push_back(carry+a[i]-b[i]);
		if(c[i]<0){c[i]+=base;carry=-1;}
		else carry=0;
	}
	return c;
}

NUM mod(NUM a, NUM b){
	//printf("mod ");printnum(a);printf(",");printnum(b);puts("");
	if(cmp(a,b)==-1)return a;//{printnum(a);puts(" wo kaesu");return a;}
	NUM m=mod(a,add(b,b));
	if(cmp(m,b)==-1)return m;//{printnum(m);puts("desune");return m;}
	else return subabs(m,b);//{printnum(subabs(m,b));puts("desune");return subabs(m,b);}
}

NUM gcd(NUM a, NUM b){
	//printf("gcd ");printnum(a);printf(",");printnum(b);puts("");
	if(cmp(b,num(0))==0)return a;
	//printf("else case\n");
	return gcd(b,mod(a,b));
}

/*
NUM readnum(){
	int x;
	scanf("%d",&x);
	return x;
}

NUM num(int a){
	return a;
}

void printnum(NUM a){
	printf("%d",a);
}
*/

main(){
	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		int n;
		scanf("%d",&n);
		NUM a[1000];
		for(int i=0;i<n;i++)a[i]=readnum();
		//for(int i=0;i<n;i++){printnum(a[i]);printf("\n");}
		NUM g=num(0);
		for(int i=1;i<n;i++){
			//printnum(subabs(a[0],a[i]));puts("");
			g=gcd(g,subabs(a[0],a[i]));
			//printnum(subabs(a[0],a[i]));printf(" ");printnum(g);
			//puts("");
		}
		printf("Case #%d: ",t);
		printnum(mod(subabs(g,mod(a[0],g)),g));
		puts("");
	}
}