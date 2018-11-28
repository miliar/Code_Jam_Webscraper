#include<stdio.h>
#include<string.h>

char s[5005][17];
char pat[10007];

char mat[17][26];	//mat[i][p] = 1 if 'a'+p can be at position-i

int x;
void parse(int i){
	
	if(pat[x]==0)
		return;

	if(pat[x]=='('){
		x++;
		while(pat[x]!=')'){
			mat[i][pat[x]-'a'] = 1;
			x++;
		}
		x++;
	}
	else{
		mat[i][pat[x]-'a'] = 1;
		x++;
	}
	parse(i+1);
}

int main(){

	int l,d,n,i,j,n1;
	int cnt;

	scanf("%d%d%d",&l,&d,&n);

	for(i=0;i<d;i++)
		scanf("%s",s[i]);

	for(n1=1;n1<=n;n1++){
		
		scanf("%s",pat);

		memset(mat,0,sizeof(mat));

		x = 0;
		parse(0);

		cnt = 0;
		for(i=0;i<d;i++){
			for(j=0;j<l;j++)if(mat[j][s[i][j]-'a']==0)
				break;
			if(j==l)
				cnt++;
		}


		printf("Case #%d: %d\n",n1,cnt);
	}


	return 0;
}