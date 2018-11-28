#include <iostream>
#include <string>
using namespace std;

FILE *in = fopen("A-large.in","r");
FILE *out = fopen("A-large.out","w");

struct dicItem{
	char word[20];
}dic[5005];

char str[500];

int main(){
	int l,d,n,t,i,j;
	fscanf(in,"%d %d %d", &l,&d,&n);
	for(i = 0; i < d; i++)
	{
		fscanf(in,"%s",dic[i].word);
	}

	t = 0;
	while(n--){
		t++;
		fscanf(in,"%s",str);
		bool map[20][30];
		memset(map,0,sizeof(map));
		i =0; j = 0;
		int len = strlen(str);
		while(i<len){
			if(str[i] == '(')
			{
				i++;
				while(str[i] != ')'){
					map[j][str[i]-'a'] = true;
					i++;
				}
			}
			else
			{
				map[j][str[i]-'a'] = true;
			}
			i++;
			j++;
		}

// 		for( i  = 0; i < l; i++){
// 			for(j = 0; j < 26; j ++)
// 				fprintf(out,"%d ",map[i][j]);
// 			fprintf(out,"\n");
// 		}
		int ans = 0;
		for(i = 0; i < d; i++){
			for(j = 0; j < l; j++)
			{
				if(!map[j][dic[i].word[j]-'a'])
					break;
			}
			if(j==l)
				ans++;
		}
		fprintf(out,"Case #%d: %d\n",t,ans);
	}
}