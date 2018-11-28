#include<iostream.h>
#include<conio.h>
#include<fstream.h>
void main(){

clrscr();
//int* N=new int[T];

ofstream output;
output.open("output.txt");
ifstream input;
input.open("input.txt");


int T;
input>>T;


for(int i=0;i<T;i++)
{
int N,S,P;
input>>N>>S>>P;
int count=0;

	for(int j=0;j<N;j++)
	{
		int t;
		input>>t;
		int flag=0;
		for(int l=10;l>=P;l--){
		if(3*l-4<=t){
		  for(int m=l;m>=l-2&&m>=0;m--){
		  for(int n=m;n>=l-2&&n>=0;n--){
		    if(l+m+n==t){
			   if(l-n==2){
					 if(flag!=1&&S>0)
					 flag=2;

			   }else{
				flag=1;


			   }
		    }

		}}}}

		if(flag==1){
		count++;
		}else if(flag==2){
		 count++;
		 S--;
		}

	}
	  output<<"Case #"<<i+1<<": "<<count<<endl;

}
output.close();
getch();

}