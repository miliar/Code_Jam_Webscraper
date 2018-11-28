#include<iostream.h>
#include<conio.h>
#include<fstream.h>




void main(){

clrscr();

ofstream output;
output.open("output.txt");
ifstream input;
input.open("input.txt");

int N;
input>>N;
int i=0;
for(i=0;i<N;i++){
char* x=new char[10];
int* y=new int[10];
for(int j=0;j<10;j++)
y[j]=0;

char c;
int em=0;
for(j=0;j<4;j++){
	for(int k=0;k<4;k++){
		input>>c;
		if(c=='.'){
			y[j]=1;
			y[k+4]=1;
			if(j==k)
				y[8]=1;
			if(j+k==3)
				y[9]=1;
			em=1;
		}else
		if(c!='T'){
			cout<<y[j];
			if(y[j]==2){
				if(x[j]!=c){
					y[j]=1;
				}
			}else if(y[j]!=1){
				cout<<y[j];
				y[j]=2;
				x[j]=c;
			}
			if(y[k+4]==2){
				if(x[k+4]!=c){
					y[k+4]=1;
				}
			}else if(y[k+4]!=1){
				y[k+4]=2;
				x[k+4]=c;
			}
			if(j==k){
				if(y[8]==2){
					if(x[8]!=c){
						y[8]=1;
					}
				}else if(y[8]!=1){
					y[8]=2;
					x[8]=c;
				}
			}
			if(j+k==3){
				if(y[9]==2){
				if(x[9]!=c){
					y[9]=1;
				}}else if(y[9]!=1){
					y[9]=2;
					x[9]=c;
				}
			}

		}
	}
}

for(j=0;j<10;j++){
	if(y[j]==2){
		if(x[j]=='X'){
			output<<"Case #"<<i+1<<": X won"<<endl;
		}
		if(x[j]=='O'){
			output<<"Case #"<<i+1<<": O won"<<endl;
		}
		break;
	}
}
if(j==10){
	if(em==0){
		output<<"Case #"<<i+1<<": Draw"<<endl;
	}else
		output<<"Case #"<<i+1<<": Game has not completed"<<endl;

}



}
getch();
}