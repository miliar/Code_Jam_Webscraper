#include<iostream>
using namespace std;
int checkIfWin(char c,char a[4][5]);
int iSboardFull(char arr[4][5]);

int main(){

	int t,count=1;
	char arr[4][5];

	cin>>t;

	while(t--){

		cin>>arr[0];
		cin>>arr[1];
		cin>>arr[2];
		cin>>arr[3];

		cout<<"Case #"<<count<<": ";
		if(checkIfWin('X',arr)){
			cout<<"X won";
		}else if(checkIfWin('O',arr)){
			cout<<"O won";
		}else if(iSboardFull(arr)){
			cout<<"Draw";
		}else{
			cout<<"Game has not completed";
		}

		cout<<endl;
		count++;

	}



	return 0;
}

int checkIfWin(char c,char arr[4][5]){

int i;

for(i=0;i<5;i++){

if ( (arr[i][0]==c || arr[i][0]=='T')  &&  (arr[i][1]==c || arr[i][1]=='T') && (arr[i][2]==c || arr[i][2]=='T') && (arr[i][3]==c || arr[i][3]=='T') )
return 1;


if ( (arr[0][i]==c || arr[0][i]=='T')  &&  (arr[1][i]==c || arr[1][i]=='T') && (arr[2][i]==c || arr[2][i]=='T') && (arr[3][i]==c || arr[3][i]=='T') )
return 1;

}


if ( (arr[0][0]==c || arr[0][0]=='T') && (arr[1][1]==c || arr[1][1]=='T') && (arr[2][2]==c || arr[2][2]=='T') && (arr[3][3]==c || arr[3][3]=='T') )
return 1;

if ( (arr[0][3]==c || arr[0][3]=='T') && (arr[1][2]==c || arr[1][2]=='T') && (arr[2][1]==c || arr[2][1]=='T') && (arr[3][0]==c || arr[3][0]=='T') )
return 1;

return 0;
}

int iSboardFull(char arr[4][5]){

int i,j;

for(i=0;i<5;i++){

  for(j=0;j<5;j++){
	if(arr[i][j]=='.')
	return 0;
  }

}


return 1;
}
