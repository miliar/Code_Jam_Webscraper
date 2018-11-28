/*
# Author:      pikkupr
# Problem:     A. Tic-Tac-Toe-Tomek
*/
#include<iostream>
#include<stdio.h>

using namespace std;

int chk_completion(int i,int j,char arr[4][4]){
	int x=0,y =0;
	for(x=0;x<4;x++){
		for(y=0;y<4;y++){
			if(arr[x][y]=='.')
				return 1;
		}
	}
	return 0;

}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int n, t=1,x=0,o=0,comp = 0,i=0,j=0;
	char arr[4][4];
	cin>>n;
	while(t<=n){
		x=0;
		o=0;
		comp=0;
		//Input
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin>>arr[i][j];//cout<<arr[i][j];
			}
			//cout<<"\n";
		}
		//Check for X
		for(i=0;i<4;i++){
			x = 0;
			for(j=0;j<4;j++){
				if(arr[i][j]=='X'||arr[i][j]=='T')
					x++;
			}
			if(x==4)
				break;
		}
		
		if(x!=4){
			for(i=0;i<4;i++){
			x = 0;
			for(j=0;j<4;j++){
				if(arr[j][i]=='X'||arr[j][i]=='T')
					x++;
			}
			if(x==4)
				break;
			}
		}
		
		if(x!=4){
			x=0;
			for(i=0,j=0;i<4;i++,j++)
				if(arr[i][j]=='X'||arr[i][j]=='T')
					x++;
		}

		if(x!=4){
			x=0;
			for(i=0,j=3;j>=0;i++,j--)
				if(arr[i][j]=='X'||arr[i][j]=='T')
					x++;
		}
		//Check for O
		for(i=0;i<4;i++){
			o = 0;
			for(j=0;j<4;j++){
				if(arr[i][j]=='O'||arr[i][j]=='T')
					o++;
			}
			if(o==4)
				break;
		}
		
		if(o!=4){
			for(i=0;i<4;i++){
			o = 0;
			for(j=0;j<4;j++){
				if(arr[j][i]=='O'||arr[j][i]=='T')
					o++;
			}
			if(o==4)
				break;
			}
		}
		
		if(o!=4){
			o=0;
			for(i=0,j=0;i<4;i++,j++)
				if(arr[i][j]=='O'||arr[i][j]=='T')
					o++;
		}

		if(o!=4){
			o=0;
			for(i=0,j=3;j>=0;i++,j--)
				if(arr[i][j]=='O'||arr[i][j]=='T')
					o++;
		}

		comp = chk_completion(0,0,arr);

		if(((x!=4)&&(o!=4))&&(comp==0))
			printf("Case #%d: Draw",t);
		else if(x==4)
			printf("Case #%d: X won",t);
		else if(o==4)
			printf("Case #%d: O won",t);
		else
			printf("Case #%d: Game has not completed",t);

	/*for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cout<<arr[i][j];
			}
			cout<<"\n";
		}*/
		if(t!=n)
			cout<<"\n";
		t++;
	}


}
