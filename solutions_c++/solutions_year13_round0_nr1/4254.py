#include<iostream>
using namespace std;
int main(){
int test, test1, i,j;
char arr[4][4];
cin>>test;
test1 = test;
while(test--)
{
	int dot=0;
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			cin>>arr[i][j];
	if(arr[0][0]+arr[0][1]+arr[0][2]+arr[0][3] == 352 || arr[0][0]+arr[0][1]+arr[0][2]+arr[0][3] ==348 || arr[1][0]+arr[1][1]+arr[1][2]+arr[1][3] == 352 || 
		arr[1][0]+arr[1][1]+arr[1][2]+arr[1][3] == 348 || arr[2][0]+arr[2][1]+arr[2][2]+arr[2][3] == 352 || arr[2][0]+arr[2][1]+arr[2][2]+arr[2][3] == 348 ||
		arr[3][0]+arr[3][1]+arr[3][2]+arr[3][3] == 352 || arr[3][0]+arr[3][1]+arr[3][2]+arr[3][3] ==348 || arr[0][0]+arr[1][1]+arr[2][2]+arr[3][3] == 352 ||
		arr[0][0]+arr[1][1]+arr[2][2]+arr[3][3] == 348 || arr[3][0]+arr[2][1]+arr[1][2]+arr[0][3] == 352 || arr[3][0]+arr[2][1]+arr[1][2]+arr[0][3] == 348 ||
		arr[0][0]+arr[1][0]+arr[2][0]+arr[3][0] == 352 || arr[0][1]+arr[1][1]+arr[2][1]+arr[3][1] == 352 || arr[0][2]+arr[1][2]+arr[2][2]+arr[3][2] == 352 ||
		arr[0][3]+arr[1][3]+arr[2][3]+arr[3][3] == 352 || arr[0][0]+arr[1][0]+arr[2][0]+arr[3][0] == 348 || arr[0][1]+arr[1][1]+arr[2][1]+arr[3][1] == 348 || 
		arr[0][2]+arr[1][2]+arr[2][2]+arr[3][2] == 348 ||
		arr[0][3]+arr[1][3]+arr[2][3]+arr[3][3] == 348)
	   {
			cout<<"Case #"<<test1-test<<": X won\n";
			continue;
	   }
	else if(arr[0][0]+arr[0][1]+arr[0][2]+arr[0][3] == 321 || arr[0][0]+arr[0][1]+arr[0][2]+arr[0][3] ==316 || arr[1][0]+arr[1][1]+arr[1][2]+arr[1][3] == 321 || 
		arr[1][0]+arr[1][1]+arr[1][2]+arr[1][3] == 316 || arr[2][0]+arr[2][1]+arr[2][2]+arr[2][3] == 321 || arr[2][0]+arr[2][1]+arr[2][2]+arr[2][3] == 316 ||
		arr[3][0]+arr[3][1]+arr[3][2]+arr[3][3] == 321 || arr[3][0]+arr[3][1]+arr[3][2]+arr[3][3] ==316 || arr[0][0]+arr[1][1]+arr[2][2]+arr[3][3] == 321 ||
		arr[0][0]+arr[1][1]+arr[2][2]+arr[3][3] == 316 || arr[3][0]+arr[2][1]+arr[1][2]+arr[0][3] == 321 || arr[3][0]+arr[2][1]+arr[1][2]+arr[0][3] == 316 || 		arr[0][0]+arr[1][0]+arr[2][0]+arr[3][0] == 321 || arr[0][1]+arr[1][1]+arr[2][1]+arr[3][1] == 321 || arr[0][2]+arr[1][2]+arr[2][2]+arr[3][2] == 321 ||
		arr[0][3]+arr[1][3]+arr[2][3]+arr[3][3] == 321 || arr[0][0]+arr[1][0]+arr[2][0]+arr[3][0] == 316 || arr[0][1]+arr[1][1]+arr[2][1]+arr[3][1] == 316 || 
		arr[0][2]+arr[1][2]+arr[2][2]+arr[3][2] == 316 ||
		arr[0][3]+arr[1][3]+arr[2][3]+arr[3][3] == 316)
	   {
			cout<<"Case #"<<test1-test<<": O won\n";
			continue;
	   }	
	   
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(arr[i][j]==46)
				dot = 1;
		if(dot)
	   {
			cout<<"Case #"<<test1-test<<": Game has not completed\n";
			continue;
	   }				
	   else 
	   {	
	   		cout<<"Case #"<<test1-test<<": Draw\n";
			continue;
	   }
	
}
return 0;
}
