#include <fstream.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
ifstream in("test.in");
ofstream out("test.out");
int n,m,c;
char dic[500][16];
char data[500][16][30];
char temp[10];
int totalcnt;
int comp[500];
int compcnt;
void back(int cas,int pos){
	int i;
	int sw,j;
	if(pos==n){
		int cnt=0;
		for(i=0;i<m;i++){
			sw=0;
			for(j=0;j<n;j++){
				if(temp[j] != dic[i][j]){
					sw=1;
					break;
				}
			}
			if(sw==0){
				totalcnt++;
				break;
			}
		}
		return;
	}
	for(i=0;;i++){
		if(!isalpha(data[cas][pos][i])){
			return;
		}
		temp[pos]=data[cas][pos][i];
		
		int aaa=0;
		for(j=0;j<m;j++){
			if(strncmp(dic[j],temp,pos+1)==0){
				aaa=1;
				break;
			}
		}
		if(aaa==1) back(cas,pos+1);
		else continue;
	}
}
int main(){
	in >> n >> m >> c;
	int i;
	for(i=0;i<m;i++){
		in >> dic[i];
	}
	char cc[501][1000];
	for(i=0;i<c;i++){
		in >> cc[i];
	}
	int sw,cnt,len;
	for(i=0;i<c;i++){
		sw=0;
		cnt=0;
		len=strlen(cc[i]);
		for(int j=0;j<len;j++){
			if(cc[i][j]=='('){
				sw=1;
				int k;
				for(k=j+1;k<len;k++){
					if(cc[i][k]==')'){
						sw=0;
						j=k;
						break;
					}
					data[i][cnt][k-(j+1)]=cc[i][k];
				}
				cnt++;
			}else if(isalpha(cc[i][j])){
				data[i][cnt++][0]=cc[i][j];
			}
		}
	}
	for(i=0;i<c;i++){
		back(i,0);
		out << "Case #" << i+1 << ": " << totalcnt << endl;
		totalcnt=0;
	}
	return 0;
}