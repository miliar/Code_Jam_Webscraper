#include<iostream>
#include<fstream>
using namespace std;

char checkrows(char mat[4][4])
{
	int i,j;
	for(i=0;i<4;i++){
		char c=mat[i][0];
		if(c=='.')
			continue;
		for(j=1;j<4;j++){
			if(mat[i][j]=='.')
				break;
			if(c=='T'){
				c=mat[i][j];
			}
			else{
				if(c!=mat[i][j] && mat[i][j]!='T'){
					break;
				}
			}
		}
		if(j==4)
			return c;
	}
	return 'N';
}
char checkcolumns(char mat[4][4])
{
	int i,j;
	for(j=0;j<4;j++){
		char c=mat[0][j];
		if(c=='.')
			continue;
		for(i=1;i<4;i++){
			if(mat[i][j]=='.')
				break;
			if(c=='T'){
				c=mat[i][j];
			}
			else{
				if(c!=mat[i][j] && mat[i][j]!='T'){
					break;
				}
			}
		}
		if(i==4)
			return c;
	}
	return 'N';
}
char checkDiagnols(char mat[4][4])
{
	int i;
	char c=mat[0][0];
	for(i=1;i<4;i++){
		if(c=='.')
			break;
		else if(c=='T'){
			c=mat[i][i];
			continue;
		}
		else if(c!=mat[i][i] && mat[i][i]!='T'){
			break;
		}
	}
	if(i==4)
		return c;
	c=mat[0][3];
	int row=1;
	for(i=2;i>=0;i--){
		if(c=='.')
			break;
		else if(c=='T'){
			c=mat[row++][i];
			continue;
		}
		else if(c!=mat[row][i] && mat[row][i]!='T'){
			break;
		}
		row=row+1;
	}
	if(i==-1)
		return c;
	return 'N';

}

char checkmat(char mat[4][4])
{
	char c=checkrows(mat);
	if(c!='N')
		return c;
	c=checkcolumns(mat);
	if(c!='N')
		return c;
	c=checkDiagnols(mat);
	return c;
}

int main(){
	ofstream fout ("tictactoe.out");
	ifstream fin ("tictactoe.in");
	char mat[4][4];
	int testcases;
	fin>>testcases;
	int isDotted=0;
	int count=1;
	while(testcases--){
		isDotted=0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				fin>>mat[i][j];
				if(mat[i][j]=='.')
					isDotted=1;
			}
		}
		/*for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				fout<<mat[i][j]<<" ";
			}
			fout<<endl;
		}*/
		char ans=checkmat(mat);
		if(ans=='N'){
			if(isDotted)
				fout<<"Case #"<<count<<": Game has not completed"<<endl;
			else
				fout<<"Case #"<<count<<": Draw"<<endl;
		}
		else
			fout<<"Case #"<<count<<": "<<ans<<" won"<<endl;
		count++;
	}
	return 0;
}
