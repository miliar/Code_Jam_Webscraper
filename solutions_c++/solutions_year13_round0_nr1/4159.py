#include <vector>
#include <list>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;



int main()
{


	ofstream outf;
	ifstream inf;
	outf.open("output.in");
	inf.open("input.in");


    //istringstream lines(line);

	int t;
	inf>>t;



	for(int tt=0;tt<t;tt++)
	{
		int bo[4][4];
		int result[10];
		int dot = 0;
		char test;
		for (int i =0;i<4;i++)
			for (int j =0;j<4;j++){

				inf>>test;
				if (test=='.'){
				bo[i][j]=0;
				dot=1;
				}
				if (test=='X')
						bo[i][j]=2;
				if (test=='O')
						bo[i][j]=-2;
				if (test=='T')
						bo[i][j]=1;
			}
		result[0]=bo[0][0]+bo[0][1]+bo[0][2]+bo[0][3];
		result[1]=bo[1][0]+bo[1][1]+bo[1][2]+bo[1][3];
		result[2]=bo[2][0]+bo[2][1]+bo[2][2]+bo[2][3];
				result[3]=bo[3][0]+bo[3][1]+bo[3][2]+bo[3][3];

				result[4]=bo[0][0]+bo[1][0]+bo[2][0]+bo[3][0];
				result[5]=bo[0][1]+bo[1][1]+bo[2][1]+bo[3][1];
				result[6]=bo[0][2]+bo[1][2]+bo[2][2]+bo[3][2];
				result[7]=bo[0][3]+bo[1][3]+bo[2][3]+bo[3][3];

				result[8]=bo[0][0]+bo[1][1]+bo[2][2]+bo[3][3];
				result[9]=bo[0][3]+bo[1][2]+bo[2][1]+bo[3][0];
		int final=0;
		for (int i =0;i<10;i++){
			if (result[i]==8 ||result[i]==7){
			final=1;
			break;
			}
			if (result[i]==-8 ||result[i]==-5){
			final=2;
			break;
			}

		}
		if (final ==1)
			outf<<"Case #"<<tt+1<<": X won\n";
		if (final ==2)
					outf<<"Case #"<<tt+1<<": O won\n";
		if (final ==0){
			if(dot==1)
				outf<<"Case #"<<tt+1<<": Game has not completed\n";
			if(dot==0)
							outf<<"Case #"<<tt+1<<": Draw\n";

		}
	/*	if(tt==4){
	for (int i =0;i<10;i++){
						cout<<result[i]<<"\n";

		}



		for (int i =0;i<4;i++){
			for (int j =0;j<4;j++){
				cout<<bo[i][j];
			}
			cout<<"\n";
		}}

*/

	}//tt lope


}


