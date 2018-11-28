#include<iostream>
#include<cstring>
using namespace std;
long long muls[100];
int imuls=0;
long long power(long long base, int p){
	if(p<=imuls){
		return muls[p];
	}else{
		
		do{
			imuls++;
			muls[imuls]=base*muls[imuls-1];
		}while(imuls<p);
		return muls[p];
	}
}
/*long long power(long long base,int p){
	long long f=1;
	for(int i=0;i<p;i++){
		f*=base;
	}
	return f;
}*/
int main(){
	int totcases;
	cin>>totcases;
	for(int cases=1;cases<=totcases;cases++){
		char line[100];
		int dec[100];
		scanf("%s",line);
		bool num[10]={0};
		bool alpha[26]={0};
		for(int i=0;i<10;i++){
			num[i]=false;
		}
		for(int i=0;i<26;i++){
			alpha[i]=false;
		}
		int numnum[10];
		int alphanum[26];
		int l = strlen(line);
		if(isdigit(line[0])){
			num[line[0]-'0']=true;
			numnum[line[0]-'0']=1;
		}else{
			alpha[line[0]-'a']=true;
			alphanum[line[0]-'a']=1;
		}
		dec[0]=1;
		bool assnums[10];
		for(int i=0;i<10;i++)
			assnums[i]=false;
		assnums[1]=true;
		for(int i=1;i<l;i++){
			if(isdigit(line[i])){
				if(num[line[i]-'0']){
					dec[i]=numnum[line[i]-'0'];
				}else{
					int j;
					for(j=0;j<10 && assnums[j];j++);
					assnums[j]=true;
					num[line[i]-'0']=true;
					numnum[line[i]-'0']=j;
					dec[i]=j;
				}
			}else{
				if(alpha[line[i]-'a']){
					dec[i]=alphanum[line[i]-'a'];
				}else{
					int j;
					for(j=0;j<10 && assnums[j];j++);
					assnums[j]=true;
					alpha[line[i]-'a']=true;
					alphanum[line[i]-'a']=j;
					dec[i]=j;
				}
			}
		}
	/*	for(int i=0;i<10;i++){
			printf("%d=%d\t",i,num[i]);
		}
		for(int i=0;i<26;i++){
			printf("%c=%d\t",i+'a',alpha[i]);
		}
		for(int i=0;i<l;i++){
			printf("%d ",dec[i]);
		}
		cout<<endl;*/
		imuls=0;
		muls[0]=1LL;
		long long base = 9LL;
		long long ans=0LL;
		while(!assnums[base])base--;
		base++;
	// 	cout<<power(2LL,2)<<endl;;
		for(int i=l-1;i>=0;i--){
			ans = ans + dec[i]*power(base,l-1-i);
		}
		printf("Case #%d: %lld\n",cases,ans);
	}
	return 0;
}