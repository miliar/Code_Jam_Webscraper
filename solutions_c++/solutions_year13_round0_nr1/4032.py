#include<fstream>
#include<cmath>
using namespace std;

int k;
const int xWin1=3*'X'+'T',xWin2=4*'X';
const int oWin1=3*'O'+'T',oWin2=4*'O';
ofstream fout ("A-large.out");
ifstream fin ("A-large.in");

bool is_win(int sum){

	if( sum%xWin1==0 || sum%xWin2==0){
		fout<<"Case #"<<k<<": X won"<<endl;
		return true;
	}
	else if( sum%oWin1==0 || sum%oWin2==0){
		fout<<"Case #"<<k<<": O won"<<endl;
		return true;
	}
	else
		return 0;

}
int main(){
	 // ifstream fin ("test.in");
	int i,j,t;
	fin>>t;
	char game[4][4];
	bool is_completed,finish;
	int sum=0;
		for(k=1;k<=t;k++){

			// enter Data
			is_completed=true;
			finish=false;
			for(i=0;i<4;i++)
				for(j=0;j<4;j++){
					fin>>game[i][j];
				if(game[i][j]=='.')
						is_completed=false;
				}
			
			
			//check rows
			for(i=0;i<4;i++){
				sum=0;
				for(j=0;j<4;j++)
					sum+=static_cast<int>(game[i][j]);
				if(is_win(sum)) {
					finish=true;
					break;
				}
			}
			if(finish)continue;

			//check colomns
			for(i=0;i<4;i++){
				sum=0;
				for(j=0;j<4;j++)
					sum+=static_cast<int>(game[j][i]);
				if(is_win(sum)) {
					finish=true;
					break;
				}
			}
			if(finish)continue;



			//check First Diagonal
			sum=0;
			for(i=0;i<4;i++)
					sum+=static_cast<int>(game[i][i]);
			if(is_win(sum))continue;
				
			
			//check Second Diagonal
			sum=0;
			for(i=0;i<4;i++)
					sum+=static_cast<int>(game[i][3-i]);
			if(is_win(sum))continue;


			
			if(is_completed)
				fout<<"Case #"<<k<<": Draw"<<endl;
			else
				fout<<"Case #"<<k<<": Game has not completed"<<endl;
		}
	return 0;


}