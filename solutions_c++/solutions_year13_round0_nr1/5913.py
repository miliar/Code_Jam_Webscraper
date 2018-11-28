#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream infile("A-large.in");
	ofstream outfile("outfile.out");
	int N;
	infile>>N;
    char A[4][4];
	string str;
	for(int i=0;i<N;i++)
	{
         for(int j=0;j<4;j++)
		 {
			 infile>>str;
			 for(int k=0;k<4;k++) A[j][k]=str[k];
		 }

		 bool flag=true,X=false,O=false;
		 for(int j=0;j<4;j++)
		 {
			 for(int k=0;k<4;k++)
			 {
				 if(A[j][k]=='.') flag=false;
			 }
		 }
		 for(int j=0;j<4;j++)
		 {
			 if((A[j][0]=='X'||A[j][0]=='T')&&(A[j][1]=='X'||A[j][1]=='T')&&(A[j][2]=='X'||A[j][2]=='T')&&(A[j][3]=='X'||A[j][3]=='T') ) {X=true;}
			 if((A[j][0]=='O'||A[j][0]=='T')&&(A[j][1]=='O'||A[j][1]=='T')&&(A[j][2]=='O'||A[j][2]=='T')&&(A[j][3]=='O'||A[j][3]=='T') ) {O=true;}
		 }
		 for(int k=0;k<4;k++)
		 {
			 if((A[0][k]=='X'||A[0][k]=='T')&&(A[1][k]=='X'||A[1][k]=='T')&&(A[2][k]=='X'||A[2][k]=='T')&&(A[3][k]=='X'||A[3][k]=='T') ) {X=true;}
			 if((A[0][k]=='O'||A[0][k]=='T')&&(A[1][k]=='O'||A[1][k]=='T')&&(A[2][k]=='O'||A[2][k]=='T')&&(A[3][k]=='O'||A[3][k]=='T') ) {O=true;}
		 }
		 if((A[0][0]=='X'||A[0][0]=='T')&&(A[1][1]=='X'||A[1][1]=='T')&&(A[2][2]=='X'||A[2][2]=='T')&&(A[3][3]=='X'||A[3][3]=='T')) {X=true;}
          if((A[0][0]=='O'||A[0][0]=='T')&&(A[1][1]=='O'||A[1][1]=='T')&&(A[2][2]=='O'||A[2][2]=='T')&&(A[3][3]=='O'||A[3][3]=='T')) {O=true;}

		  if((A[0][3]=='X'||A[0][3]=='T')&&(A[1][2]=='X'||A[1][2]=='T')&&(A[2][1]=='X'||A[2][1]=='T')&&(A[3][0]=='X'||A[3][0]=='T')) {X=true;}
		  if((A[0][3]=='O'||A[0][3]=='T')&&(A[1][2]=='O'||A[1][2]=='T')&&(A[2][1]=='O'||A[2][1]=='T')&&(A[3][0]=='O'||A[3][0]=='T')) {O=true;}
		  if(flag) {
			  if((!X) && (!O)) outfile<<"Case #"<<i+1<<": Draw"<<endl;
			  else{
				  if(X) outfile<<"Case #"<<i+1<<": X won"<<endl;
				  if(O) outfile<<"Case #"<<i+1<<": O won"<<endl;
			  }
		  }
		  if(!flag){
			  if(!X && !O) outfile<<"Case #"<<i+1<<": Game has not completed"<<endl;
			  else{
				  if(X) outfile<<"Case #"<<i+1<<": X won"<<endl;
				  if(O) outfile<<"Case #"<<i+1<<": O won"<<endl;
			  }
		  }

	}
	infile.close();
	outfile.close();
    return 0;

}
