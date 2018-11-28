#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <regex>
#include <algorithm>
#include <iomanip>

#define large
#ifdef small
#define T 10
#endif

#ifdef small
#define T 10
#endif

#ifdef large
#define T 1000
#endif
typedef float decimal;
#define eps 1e-6
inline int comp(const decimal &a, const decimal &b) {
	if (fabs(a - b) < eps)
		return 0;
	else if(a<b){
		return -1;
	}
	else {
		return 1;
	}
}


		 

using namespace std;
void main(){
FILE *O,*I;
#ifdef none
freopen_s(&I,"at.in","r+",stdin);
freopen_s(&O,"at.out","w+",stdout);
#endif
#ifdef small
freopen_s(&I,"a-small-attempt2.in","r+",stdin);
freopen_s(&O,"a-small-attempt2.out","w+",stdout);
#endif

#ifdef large
freopen_s(&I,"a-large.in","r+",stdin);
freopen_s(&O,"a-large.out","w+",stdout);
#endif

	int t,flag=0;
	char mat[4][4];
	char buff[5];
/*
int **list=new int*[t];
	for(int i=0;i<t;i++){
		list[i]=new int [4];
	}
*/
	std::cin>>t;
	
		std::cin.getline(buff,5,'\n');	
	for(int i=1;i<=t;i++){
		//std::cin>>num;
		for(int j=0;j<4;j++){
		std::cin.getline(buff,5,'\n');		
		std::istringstream ss(buff);
		
			for(int k=0;k<4;k++){
				ss>>mat[j][k];
			}
		}

		flag=0;
		for(int p=0;p<4;p++){
			if(mat[p][0]+mat[p][1]+mat[p][2]+mat[p][3]==(3*(int)('O')+(int)'T')||mat[p][0]+mat[p][1]+mat[p][2]+mat[p][3]==(4*(int)('O')))
			{
				std::cout<<"Case #"<<i<<": O won"<<endl;
				flag=1;
				break;
			}
					
			else if(mat[p][0]+mat[p][1]+mat[p][2]+mat[p][3]==(3*(int)('X')+(int)'T')||mat[p][0]+mat[p][1]+mat[p][2]+mat[p][3]==(4*(int)('X')))
			{
				std::cout<<"Case #"<<i<<": X won"<<endl;
				flag=1;
				break;
			}
			else if(mat[0][p]+mat[1][p]+mat[2][p]+mat[3][p]==(3*(int)('O')+(int)'T')||mat[0][p]+mat[1][p]+mat[2][p]+mat[3][p]==(4*(int)('O')))
			{
				cout<<"Case #"<<i<<": O won"<<endl;
				flag=1;
				break;
			}
			else if(mat[0][p]+mat[1][p]+mat[2][p]+mat[3][p]==(3*(int)('X')+(int)'T')||mat[0][p]+mat[1][p]+mat[2][p]+mat[3][p]==(4*(int)('X')))
			{
				cout<<"Case #"<<i<<": X won"<<endl;
				flag=1;	
				break;
			}
		}	
		if((mat[0][0]+mat[1][1]+mat[2][2]+mat[3][3]==(3*(int)('O')+(int)'T')||mat[0][0]+mat[1][1]+mat[2][2]+mat[3][3]==(4*(int)('O')))&&!flag)
		{
			cout<<"Case #"<<i<<": O won"<<endl;
			flag=1;
		}
		else 	if((mat[0][0]+mat[1][1]+mat[2][2]+mat[3][3]==(3*(int)('X')+(int)'T')||mat[0][0]+mat[1][1]+mat[2][2]+mat[3][3]==(4*(int)('X')))&&!flag)
		{
			cout<<"Case #"<<i<<": X won"<<endl;
			flag=1;
				
		}
		else 	if((mat[0][3]+mat[1][2]+mat[2][1]+mat[3][0]==(3*(int)('O')+(int)'T')||mat[0][3]+mat[1][2]+mat[2][1]+mat[3][0]==(4*(int)('O')))&&!flag)
		{
			cout<<"Case #"<<i<<": O won"<<endl;
			flag=1;
		}
		else 	if((mat[0][3]+mat[1][2]+mat[2][1]+mat[3][0]==(3*(int)('X')+(int)'T')||mat[0][3]+mat[1][2]+mat[2][1]+mat[3][0]==(4*(int)('X')))&&!flag)
		{
			cout<<"Case #"<<i<<": X won"<<endl;
			flag=1;
		}
							
		if(flag==0){
			int flag2=0;
			for(int p=0;p<4&&!flag2;p++){
				for(int q=0;q<4&&!flag2;q++){
					if(mat[p][q]=='.'){
						cout<<"Case #"<<i<<": Game has not completed"<<endl;
						flag2=1;
					}
				}
			}
			if(!flag2)
				cout<<"Case #"<<i<<": Draw"<<endl;
		}
		
	std::cin.getline(buff,5,'\n');
	}	
	
}		

	



