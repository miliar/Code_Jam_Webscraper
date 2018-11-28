 #include <vector>
#include <list>
#include <limits.h>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <stdlib.h>
using namespace std;

int main(){	
	freopen("in.txt","r", stdin);
	freopen("out.txt","w", stdout);
	int t;
	string str[4];
	cin>>t;
	for(int k=1; k<=t; k++){
		for(int i=0; i<4; i++)
			cin>>str[i];
		int tcoun=0;
		int xcoun=0;
		int ocoun=0;
		bool solution = false;
		// count in row
		for(int i=0; i<4; i++){
			tcoun=0;
			xcoun=0;
			ocoun=0;
			for(int j=0; j<4; j++){
				if(str[i][j]=='X')
					xcoun++;
				else if(str[i][j]=='O')
					ocoun++;
				else if(str[i][j]=='T')
					tcoun++;				
			}
			if(tcoun+xcoun==4){
				solution = true;
				cout<<"Case #"<<k<<": X won"<<endl;
			}
			else if(tcoun+ocoun==4){
				solution = true;
				cout<<"Case #"<<k<<": O won"<<endl;
			}
			if(solution == true)
				break;
		}
		if(solution == true)
			continue;
		// count in col
		for(int i=0; i<4; i++){
			tcoun=0;
			xcoun=0;
			ocoun=0;
			for(int j=0; j<4; j++){
				if(str[j][i]=='X')
					xcoun++;
				else if(str[j][i]=='O')
					ocoun++;
				else if(str[j][i]=='T')
					tcoun++;
			}
			if(tcoun+xcoun==4){
				solution = true;
				cout<<"Case #"<<k<<": X won"<<endl;
			}
			else if(tcoun+ocoun==4){
				solution = true;
				cout<<"Case #"<<k<<": O won"<<endl;
			}
			if(solution == true)
				break;
		}
		if(solution == true)
			continue;
		//diagnal
		tcoun=0;
		xcoun=0;
		ocoun=0;
		for(int i=0; i<4; i++){
			if(str[i][i]=='X')
				xcoun++;
			else if(str[i][i]=='O')
				ocoun++;
			else if(str[i][i]=='T')
				tcoun++;
		}
		if(tcoun+xcoun==4){
			solution = true;
			cout<<"Case #"<<k<<": X won"<<endl;
		}
		else if(tcoun+ocoun==4){
			solution = true;
			cout<<"Case #"<<k<<": O won"<<endl;
		}
		if(solution==true)
			continue;
		
		tcoun=0;
		xcoun=0;
		ocoun=0;
		for(int i=0; i<4; i++){
			if(str[i][3-i]=='X')
				xcoun++;
			else if(str[i][3-i]=='O')
				ocoun++;
			else if(str[i][3-i]=='T')
				tcoun++;
		}
		if(tcoun+xcoun==4){
			solution = true;
			cout<<"Case #"<<k<<": X won"<<endl;
		}
		else if(tcoun+ocoun==4){
			solution = true;
			cout<<"Case #"<<k<<": O won"<<endl;
		}

		if(solution==true)
			continue;
			
		for(int i=0; i<4; i++)
		for(int j=0; j<4; j++){
			if(str[i][j]=='.' && solution==false){
				solution = true;
				cout<<"Case #"<<k<<": Game has not completed"<<endl;
				break;
			}
		}
		if(solution == false)
			cout<<"Case #"<<k<<": Draw"<<endl;
	}
	
	return 0;
}
