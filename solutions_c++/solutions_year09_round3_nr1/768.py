#include <iostream>
using namespace std;

FILE *in = fopen("A-large.in","r");
FILE *out = fopen("A-large.out","w");

bool used[130];
int mean[130];
char line[100];

typedef __int64 bigInt;

bigInt solve(char *line){
	bigInt res;
	int len = strlen(line);
	if(len == 1)return 1;
	int count,i;
	memset(used,false,sizeof(used));
	for(i = 0; i < 128; i++)
		mean[i] =-1;

	count = 0;
	for(i = 0; i < len; i++){
		if(used[line[i]])continue;
		else{
			used[line[i]] = true;
			count++;
		}
	}
	//fprintf(out,"%d",count);

	int cur = 0;
	mean[line[0]] = 1;
	for(i =1; i < len; i++){
		if(mean[line[i]] == -1){
			mean[line[i]] = cur;
			cur++;
			if(cur==1)cur++;
		}
	}

	if(count==1){
		count = 2;
	}

	bigInt base = 1;
	res = 0;
	for(i = len-1; i >=0; i--){
		res+=mean[line[i]]*base;
		base*=count;
	}
	return res;
}

int main(){
	int n,t;
	fscanf(in,"%d",&n);
	t = 0;
	while(n--){
		t++;
		fscanf(in,"%s",line);

		fprintf(out,"Case #%d: %I64d\n",t,solve(line));

	}

	fclose(out);
	return 0;
}