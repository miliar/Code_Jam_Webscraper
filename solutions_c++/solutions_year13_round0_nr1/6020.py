#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <set>
#include <stack>





using namespace std;


char grid[4][4];

int main(){

	freopen("proba.in","r",stdin);
	freopen("proba1.out","w",stdout);



	int cases;
	cin>>cases;


	for(int i=1;i<=cases;i++){

		bool dotflag=false;

		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				cin>>grid[j][k];
				if(grid[j][k]== '.'){
					dotflag=true;
				}
			}
		}







		if(dotflag){



			int xcount=0;
			int ocount=0;
			int tcount=0;

			bool xwin=false;
			bool owin=false;


			for(int l=0;l<4;l++){
				xcount=0;
				ocount=0;
				tcount=0;
			for(int j=0;j<4;j++){


				if(grid[l][j]=='X')
					xcount++;

				else if(grid[l][j]=='O')
					ocount++;

				else if(grid[l][j]=='T')
					tcount++;


			}

			if(xcount==4 ||   (xcount==3 && tcount==1) )
				xwin=true;

			else if(ocount == 4  || (ocount==3 && tcount==1) )
				owin=true;


			}



			for(int l=0;l<4;l++){

				 xcount=0;
				ocount=0;
				tcount=0;
			for(int j=0;j<4;j++){


				if(grid[j][l]=='X')
					xcount++;

				else if(grid[j][l]=='O')
					ocount++;

				else if(grid[j][l]=='T')
					tcount++;

			}

			if(xcount==4 ||   (xcount==3 && tcount==1) )
				xwin=true;

			else if(ocount == 4  || (ocount==3 && tcount==1) )
				owin=true;



			}

			xcount=0;
			ocount=0;
			tcount=0;

			for(int j=0;j<4;j++){

				if(grid[0+j][0+j] == 'X')
					xcount++;
				else if(grid[0+j][0+j]=='O')
					ocount++;

				else if(grid[0+j][0+j]=='T')
					tcount++;

			}

			if(xcount==4 ||  (xcount==3 && tcount==1))
				xwin=true;

			else if(ocount == 4 || (ocount==3 && tcount==1))
				owin=true;


			 xcount=0;
			 ocount=0;
			 tcount=0;


			for(int j=0;j<4;j++){


				if(grid[3-j][0+j]=='X')
					xcount++;
				else if(grid[3-j][0+j]=='O')
					ocount++;

				else if(grid[3-j][0+j]=='T')
					tcount++;




			}

			if(xcount==4 ||  (xcount==3 && tcount==1))
							xwin=true;

						else if(ocount == 4 || (ocount==3 && tcount==1))
							owin=true;

			if(xwin)
				printf("Case #%d: X won\n",i);
			else if(owin)
				printf("Case #%d: O won\n",i);
			else
				printf("Case #%d: Game has not completed\n",i);





		}

		else{




			int xcount=0;
			int ocount=0;
			int tcount=0;

			bool xwin=false;
			bool owin=false;


			for(int l=0;l<4;l++){
				xcount=0;
				ocount=0;
				tcount=0;
			for(int j=0;j<4;j++){


				if(grid[l][j]=='X')
					xcount++;

				else if(grid[l][j]=='O')
					ocount++;

				else if(grid[l][j]=='T')
					tcount++;


			}

			if(xcount==4 ||   (xcount==3 && tcount==1) )
				xwin=true;

			else if(ocount == 4  || (ocount==3 && tcount==1) )
				owin=true;


			}



			for(int l=0;l<4;l++){

				 xcount=0;
				ocount=0;
				tcount=0;
			for(int j=0;j<4;j++){


				if(grid[j][l]=='X')
					xcount++;

				else if(grid[j][l]=='O')
					ocount++;

				else if(grid[j][l]=='T')
					tcount++;

			}

			if(xcount==4 ||   (xcount==3 && tcount==1) )
				xwin=true;

			else if(ocount == 4  || (ocount==3 && tcount==1) )
				owin=true;



			}

			xcount=0;
			ocount=0;
			tcount=0;

			for(int j=0;j<4;j++){

				if(grid[0+j][0+j] == 'X')
					xcount++;
				else if(grid[0+j][0+j]=='O')
					ocount++;

				else if(grid[0+j][0+j]=='T')
					tcount++;

			}

			if(xcount==4 ||  (xcount==3 && tcount==1))
				xwin=true;

			else if(ocount == 4 || (ocount==3 && tcount==1))
				owin=true;


			 xcount=0;
			 ocount=0;
			 tcount=0;


			for(int j=0;j<4;j++){


				if(grid[3-j][0+j]=='X')
					xcount++;
				else if(grid[3-j][0+j]=='O')
					ocount++;

				else if(grid[3-j][0+j]=='T')
					tcount++;




			}

			if(xcount==4 ||  (xcount==3 && tcount==1))
							xwin=true;

						else if(ocount == 4 || (ocount==3 && tcount==1))
							owin=true;

			if(xwin)
				printf("Case #%d: X won\n",i);
			else if(owin)
				printf("Case #%d: O won\n",i);
			else
				printf("Case #%d: Draw\n",i);










		}

	}


}

