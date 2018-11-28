#include<stdio.h>
#include<string>
#include<iostream>


using namespace std;

int i,j,k;
int l,d,n;
string dc[5001];
string word;
bool open;
int p,m;
bool mp[16]['z'];
bool valid;
int res;

int main(){
	freopen("bb.in","r",stdin);
	freopen("bb.out","w",stdout);

	scanf("%d %d %d\n",&l,&d,&n);
	for(i=0;i<d;i++){
		getline(cin,dc[i]);
	}
	for(j=1;j<=n;j++){
		open=false;
		m=0;
		for(p=0;p<16;p++)
			for(char c='a';c<='z';c++){
				mp[p][c]=false;
			}

		getline(cin,word);
		
		for(k=0;k<word.length();k++){
			if(open){
				if(word[k]==')'){
					open=false;
					m++;
				}
				else mp[m][word[k]]=true;
			}
			else{
				if(word[k]=='(') open=true;
				else{
					mp[m][word[k]]=true;
					m++;
				}
			}
		}
		/*
		for(p=0;p<l;p++){
			printf("(");
			for(char c='a';c<='z';c++) if(mp[p][c]) printf("%c",c);
			printf(")");
		}
		printf("\n");
		*/
		res=0;
		for(i=0;i<d;i++){
			valid=true;
			for(p=0;p<l;p++){
				if(!mp[p][dc[i][p]]){
					valid=false;
					break;
				}
			}
			if(valid) res++;
		}

		printf("Case #%d: %d\n",j,res);
	}
	return 0;
}
