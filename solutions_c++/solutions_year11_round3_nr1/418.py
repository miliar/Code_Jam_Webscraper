#include"stdlib.h"
#include"stdio.h"
#include <string>
#include<cmath>
#include<iostream>
#include<fstream>
using namespace std;

int Map[51][51]={0};
int cMap[51][51]={0};
int main()
{
ifstream in;
ofstream out;
in.open("A-small-attempt0.in");
out.open("OUTPUT.txt");

int T;
in>>T;
int R,C;


for(int Case=1;Case<=T;Case++){
	in>>R>>C;
	char c;
	for(int i=0;i<R;i++)
		for(int j=0;j<C;j++){
			in>>c;
			if(c=='.')Map[i][j]=0;
			else Map[i][j]=1;			
		}
	int check=1;
		for( i=0;i<R;i++)
			for(int j=0;j<C;j++)
				cMap[i][j]=Map[i][j];
		for( i=0;i<R;i++){
			if(check==0)break;
			for(int j=0;j<C;j++){
				if(Map[i][j]==1){
					if(i==R||j==C)
					{check=0;
					break;
					}
					if(Map[i+1][j]==0||Map[i][j+1]==0||Map[i+1][j+1]==0)				
					{check=0;
					break;
					}
					cMap[i+1][j]=-1;cMap[i][j+1]=-1;
					Map[i][j]=0;Map[i+1][j+1]=0;Map[i][j+1]=0;Map[i+1][j]=0;

				}
			}
		}

		out<<"Case #"<<Case<<":"<<endl;

		if(check==0)
			out<<"Impossible"<<endl;
		else{
			for( i=0;i<R;i++){
				for(int j=0;j<C;j++){
					if(cMap[i][j]==0)out<<'.';
					else 
					{if(cMap[i][j]==1)out<<'/';
						else out<<'\\';
					}
				}
				out<<endl;
			}

		}
		



}

in.close();
out.clear();
out.close();
return 0;
}