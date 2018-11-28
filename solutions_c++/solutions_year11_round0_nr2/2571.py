#include <iostream>
#include <string>
using namespace std;
char str1[40][5],str2[30][4],str3[150],stack[2000];
int top = -1;
char pop()
{
	char ans = stack[top];
	top --;
	return ans;
}
void push(char ch){
	top++;
	stack[top] = ch;
}
int main()
{
	int T,C,D,n,cnt=0;
	freopen("D:\\B-large.in","r",stdin);
	freopen("D:\\B-large1.out","w",stdout);
	scanf("%d",&T);
	while(T--) {
		top =-1;
		scanf("%d",&C);
		for(int i = 0 ; i < C ; i ++) scanf("%s",&str1[i]);
		scanf("%d",&D);
		for(int i = 0 ; i < D ; i ++) scanf("%s",&str2[i]);
		scanf("%d",&n);
		scanf("%s",&str3);
		for(int i = 0 ; i < n ; i++) 
		{
			int flag1= 0,flag2=0;
			for(int j = 0 ; j < C ; j ++ ) {
				if(flag1) break;
				if(str3[i] == str1[j][0] || str3[i] == str1[j][1] ) { //合并的
					if(str3[i] == str1[j][1]) {
						if(top > -1) {
							char ch = stack[top];
							if(stack[top]==str1[j][0]) {
								pop();
								push(str1[j][2]);
								flag1= 1;
							}
						}
					}
					else if(str3[i] == str1[j][0]) {
						if(top > -1) {
							char ch = stack[top];
							if(stack[top]==str1[j][1]) {
								pop();
								push(str1[j][2]);
								flag1=1;
							}
						}
					}
				}
			}
			for(int k = 0 ; k < D ; k ++) {
				if(flag2) break;
				if(!flag1 && (str3[i] == str2[k][0] || str3[i] == str2[k][1])) { //删除的
					if(str3[i] == str2[k][0])  {
						if(top > -1) {
							int pos=-1;
							for(int j = 0  ; j <= top; j ++) {
								if(stack[j] == str2[k][1]) {
									pos = j;
									break;
								}
							}
							if(pos!=-1) {
								top = -1;flag2=1;
							}
						}
					}
					if(str3[i] == str2[k][1])  {
						if(top > -1){
							int pos=-1;
							for(int j = 0 ; j <= top; j ++) {
								if(stack[j] == str2[k][0]) {
									pos = j;
									break;
								}
							}
							if(pos!=-1) {
								top = -1;flag2=1;
							}
						}
					}
				}
			}
			if(!flag1 && !flag2) push(str3[i]);
		}
		if(top == -1) printf("Case #%d: []\n",++cnt);
		else {
			printf("Case #%d: [%c",++cnt,stack[0]);
			for(int i =1 ; i <= top ;i++)
				printf(", %c",stack[i]);
			printf("]\n");
		}
	}
	return 0;
}