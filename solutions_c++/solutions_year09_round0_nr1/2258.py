#include<stdio.h>
#include<string.h>

int n,m,k;
char dic[5000][15];
char sen[1000];
bool chk[15][26];

FILE *fout=fopen("output.txt","w");

void process(int tc){
	int len = strlen(sen);
	int i,j,st=0,cnt=0;
	for(i=0;i<n;i++)
		for(j=0;j<26;j++)
			chk[i][j] = false;
	for(i=0;i<len;i++){
		if(st==0 && sen[i] >= 'a' && sen[i] <= 'z'){
			chk[cnt][int(sen[i]-'a')] = true;
			cnt++;
		}
		else if(st==1 && sen[i] >= 'a' && sen[i] <= 'z'){
			chk[cnt][int(sen[i]-'a')] = true;
		}
		else if(sen[i] == '(') st = 1;
		else if(sen[i] == ')'){
			st = 0;
			cnt++;
		}
	}

	int ccnt = 0;
	for(i=0;i<m;i++){
		for(j=0;j<n;j++){
			if(!chk[j][int(dic[i][j]-'a')]) break;
		}
		if(j==n) ccnt++;
	}
	fprintf(fout,"Case #%d: %d\n",tc+1,ccnt);
}

int main(void){
	int i;
	FILE *fin=fopen("input.txt","r");
	fscanf(fin,"%d%d%d",&n,&m,&k);
	for(i=0;i<m;i++){
		fscanf(fin,"%s",dic[i]);
	}
	for(i=0;i<k;i++){
		fscanf(fin,"%s",sen);
		process(i);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}