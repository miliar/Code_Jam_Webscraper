#include <iostream>
#include <stdio.h>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>

using namespace std;


int main(){
	int t;
	scanf("%d",&t);
	for(int tst=1;tst<=t;tst++){
		vector<string> a; 

		for(int i=0;i<4;i++){
			string s;
			cin>>s;
			a.push_back(s);
		}

		/*for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cout<<a[i][j];
			}
			cout<<endl;
		}*/

		int xcount=0,ocount=0,emptycount=0;
		int xflag=0,xflag2=0,xflag3=0,xflag4=0,oflag=0,oflag2=0,oflag3=0,oflag4=0;


		for(int i=0;i<4;i++){
			xcount=0;
			for(int j=0;j<4;j++){
				if(a[i][j]=='X' || a[i][j]=='T')
					xcount++;
			}
			if(xcount==4){
				xflag=1;
				break;
			}
		}

		for(int j=0;j<4;j++){
			xcount=0;
			for(int i=0;i<4;i++){
				if(a[i][j]=='X' || a[i][j]=='T')
					xcount++;
			}
			if(xcount==4){
				xflag2=1;
				break;
			}
		}

//diagonal checking
		int y=0;
		xcount=0;
		for(int x=0;x<4;x++){
				if(a[x][y]=='X' || a[x][y] == 'T')
					xcount++;
				y++;
		}

		if(xcount == 4)
			xflag3=1;
		

		y=3;
		xcount=0;
		for(int x=0;x<4;x++){
				if(a[x][y]=='X' || a[x][y] == 'T')
					xcount++;
				y--;
		}

		if(xcount == 4)
			xflag4=1;

//diagonal checking

		
		for(int i=0;i<4;i++){
			ocount=0;
			for(int j=0;j<4;j++){
				if(a[i][j]=='O' || a[i][j]=='T')
					ocount++;
			}
			if(ocount==4){
				oflag=1;
				break;
			}
		}

		for(int j=0;j<4;j++){
			ocount=0;
			for(int i=0;i<4;i++){
				if(a[i][j]=='O' || a[i][j]=='T')
					ocount++;
			}
			if(ocount==4){
				oflag2=1;
				break;
			}
		}


		//diagonal checking
		y=0;
		ocount=0;
		for(int x=0;x<4;x++){
				if(a[x][y]=='O' || a[x][y] == 'T')
					ocount++;
				y++;
		}

		if(ocount == 4)
			oflag3=1;
		

		y=3;
		ocount=0;
		for(int x=0;x<4;x++){
				if(a[x][y]=='O' || a[x][y] == 'T')
					ocount++;
				y--;
		}

		if(ocount == 4)
			oflag4=1;

		//diagonal checking


		if(xflag ==1 || xflag2 ==1 || xflag3 ==1 || xflag4 ==1)
			cout<<"Case #"<<tst<<": X won"<<endl;
		else if(oflag ==1 || oflag2 ==1 || oflag3 ==1 || oflag4 ==1)
			cout<<"Case #"<<tst<<": O won"<<endl;
		else{
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					if(a[i][j]=='.')
						emptycount++;
				}
			}

			if(emptycount==0)
				cout<<"Case #"<<tst<<": Draw"<<endl;
			else
				cout<<"Case #"<<tst<<": Game has not completed"<<endl;
		}
	}
	return 0;
}