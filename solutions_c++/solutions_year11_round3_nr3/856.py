#include <stdio.h>
FILE *fin = fopen("input.txt","r");
FILE *fout = fopen("output.txt","w");

int n;
__int64 h, l;
__int64 fre[1000];
__int64 ous;
void input()
{
	int i;
	fscanf(fin,"%d %I64d %I64d",&n, &l, &h);
	for (i=0;i<n;i++){
		fscanf(fin,"%I64d",&fre[i]);
	}
}
void pro()
{
	__int64 i;
	int j;
	bool flag;
	ous = -1;
	for (i=l;i<=h;i++){
		flag = false;
		for (j=0;j<n;j++){
			if (i>fre[j]){
				if ((i%fre[j])!=0){
					flag = true;
					break;
				}
			}else{
				if ((fre[j]%i)!=0){
					flag = true;
					break;
				}
			}
		}
		if (flag == false){
			ous = i;
			break;
		}
	}
}
void output()
{
	if (ous == -1){
		fprintf(fout,"NO\n");
	}else{
		fprintf(fout,"%I64d\n",ous);
	}
}
int main()
{
	int i,t;
	fscanf(fin,"%d",&t);
	for (i=0;i<t;i++){
		input();
		pro();
		fprintf(fout,"Case #%d: ",i+1);
		output();
	}
	return 0;
}
