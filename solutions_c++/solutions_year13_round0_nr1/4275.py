#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int T;
string s;
vector<vector<char> > grid (5, vector<char>(5));
int i;
int j;
int k;
char c;
int sum;
char cT='T';
char cX='X';
char cO='O';
char cDot='.';

int main(int argc, char *argv[]) {
	ifstream in("A-large.in");
	in>>T;
	ofstream out("A-large.out");
	for(i=1;i<=T;i++){
		for(j=1;j<=4;j++){
			in>>s;
			if(s=="\n"){
				j--;
			}
			else{
				for(k=1;k<=4;k++){
					c=s[k-1];
					grid[j][k]=s[k-1];
				}
			}
		}
		
		for(j=1;j<=4;j++){
			sum=0;
			for(k=1;k<=4;k++){
				c=grid[j][k];
				if(grid[j][k]==cT){
					sum=sum+10;
				}
				if(grid[j][k]==cO){
					sum=sum+0;
				}
				if(grid[j][k]==cX){
					sum=sum+1;
				}
				if(grid[j][k]==cDot){
					sum=sum+100;
				}
			}
			if(sum==0 || sum==10){
				out << "Case #" << i << ": O won" << endl;
				goto A;
			}
			if(sum==4 || sum==13){
				out << "Case #" << i << ": X won" << endl;
				goto A;
			}
		}
		
		for(j=1;j<=4;j++){
			sum=0;
			for(k=1;k<=4;k++){
				c=grid[k][j];
				if(grid[k][j]==cT){
					sum=sum+10;
				}
				if(grid[k][j]==cO){
					sum=sum+0;
				}
				if(grid[k][j]==cX){
					sum=sum+1;
				}
				if(grid[k][j]==cDot){
					sum=sum+100;
				}
			}
			if(sum==0 || sum==10){
				out << "Case #" << i << ": O won" << endl;
				goto A;
			}
			if(sum==4 || sum==13){
				out << "Case #" << i << ": X won" << endl;
				goto A;
			}
		}
		sum=0;
		for(j=1;j<=4;j++){
			
			k=j;
			c=grid[j][k];
				if(grid[j][k]==cT){
					sum=sum+10;
				}
				if(grid[j][k]==cO){
					sum=sum+0;
				}
				if(grid[j][k]==cX){
					sum=sum+1;
				}
				if(grid[j][k]==cDot){
					sum=sum+100;
				}
		}
			if(sum==0 || sum==10){
				out << "Case #" << i << ": O won" << endl;
				goto A;
			}
			if(sum==4 || sum==13){
				out << "Case #" << i << ": X won" << endl;
				goto A;
			}
		
		sum=0;		
		for(j=1;j<=4;j++){
			k=5-j;
			c=grid[j][k];
				if(grid[j][k]==cT){
					sum=sum+10;
				}
				if(grid[j][k]==cO){
					sum=sum+0;
				}
				if(grid[j][k]==cX){
					sum=sum+1;
				}
				if(grid[j][k]==cDot){
					sum=sum+100;
				}
		}
			if(sum==0 || sum==10){
				out << "Case #" << i << ": O won" << endl;
				goto A;
			}
			if(sum==4 || sum==13){
				out << "Case #" << i << ": X won" << endl;
				goto A;
			}
		
		for(j=1;j<=4;j++){
			for(k=1;k<=4;k++){
				c=grid[j][k];
				if(grid[j][k]==cDot){
					out << "Case #" << i << ": Game has not completed" << endl;
					goto A;
				}
			
			}
		}
		
		out << "Case #" << i << ": Draw" << endl;
		A:
			int mark;
	}
	return 0;
}
