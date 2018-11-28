#include<iostream>
#include<cstring>
using namespace std;
int main(){
	int N;
	scanf("%d",&N);
	getchar();
	for(int i=1;i<=N;i++){
		char input[600];
		gets(input);
		int ans[19],length;
		length=strlen(input);
		for(int j=0;j<19;j++)
			ans[j]=0;
		for(int j=0;j<length;j++){
			if(input[j]=='w')
				ans[0]++;
			else if(input[j]=='e'){
				ans[1]=ans[1]+ans[0];
				ans[6]=ans[6]+ans[5];
				ans[14]=ans[14]+ans[13];
			}
			else if(input[j]=='l')
				ans[2]=ans[2]+ans[1];
			else if(input[j]=='c'){
				ans[3]=ans[3]+ans[2];
				ans[11]=ans[11]+ans[10];
			}
			else if(input[j]=='o'){
				ans[4]=ans[4]+ans[3];
				ans[9]=ans[9]+ans[8];
				ans[12]=ans[12]+ans[11];
			}
			else if(input[j]=='m'){
				ans[5]=ans[5]+ans[4];
				ans[18]=ans[18]+ans[17];
			}
			else if(input[j]==' '){
				ans[7]=ans[7]+ans[6];
				ans[10]=ans[10]+ans[9];
				ans[15]=ans[15]+ans[14];
			}
			else if(input[j]=='t')
				ans[8]=ans[8]+ans[7];
			else if(input[j]=='d')
				ans[13]=ans[13]+ans[12];
			else if(input[j]=='j')
				ans[16]=ans[16]+ans[15];
			else if(input[j]=='a')
				ans[17]=ans[17]+ans[16];
		}
		printf("Case #%d: ",i);
		int finalAnswer=ans[18]%10000;
		if(finalAnswer<10)
			printf("000%d\n",finalAnswer);
		else if(finalAnswer>=10 and finalAnswer<100)
			printf("00%d\n",finalAnswer);
		else if(finalAnswer>=100 and finalAnswer<1000)
			printf("0%d\n",finalAnswer);
		else if(finalAnswer>=1000 and finalAnswer<10000)
			printf("%d\n",finalAnswer);
	}
	return 0;
}
