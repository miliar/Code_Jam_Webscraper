#include<iostream>

using namespace std;

int cas, cas_n;
char com[4] = "___";
char rev[3] = "__";
char ll[128];
char res[128];
int pos = -1;

void check_rev();
void check_com();
void check_com(){
	if(pos>=1){
		if((res[pos] == com[0] && res[pos-1] == com[1]) || (res[pos] == com[1] && res[pos-1] == com[0])){
			res[pos-1] = com[2];
			pos--;
			check_com();
			check_rev();
		}
	}
}

void check_rev()
{
	if(pos>=1){
		if(res[pos] == rev[0])	{
			//for(int i=pos-1; i>=0; i--){
			for(int i=0;i<pos; i++){
				if(res[i] == rev[1]){
					pos = -1;//i - 1;
				}
			}
		}else if(res[pos] == rev[1]){
			//for(int i=pos-1; i>=0; i--){
			for(int i=0;i<pos; i++){
				if(res[i] == rev[0]){
					pos = -1;//i - 1;
				}
			}
		}
	}
}
int main(int argc, char *argv[])
{
	freopen("t.in", "r", stdin);
	freopen("t.out", "w", stdout);
	scanf("%d\n", &cas);




	for(int cas_n=1; cas_n<=cas; cas_n++)
	{
		int c,r,n;
		scanf("%d ", &c);
		if(c) scanf("%s", com);
		scanf("%d ", &r);
		if(r) scanf("%s", rev);
		scanf("%d", &n);
		scanf("%s", ll);

		pos = -1;
		for(int i=0; i< n;i++)
		{
			res[++pos] = ll[i];
			if(c) 
				check_com();
			if(r)
				check_rev();
		}


		printf("Case #%d: [", cas_n);
		for(int i = 0; i<= pos; i++){
			printf("%c", res[i]);
			if(i!=pos)
				printf(", ");
		}
		printf("]\n");
	}

	return 0;
}
