//Problem A
#include <math.h>
#include <stdlib.h>

#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

#define MAX_CASES 50

class Picture{
public:

	char picture[50][50];
	int r,c;

	bool possible;

	Picture(){
		r=c=0;
		possible=true;
	}

	void Set(char inPicture[50][50],int inR,int inC){
		r=inR;
		c=inC;
		for (int i=0;i<r;i++)
		{
			for (int j=0;j<c;j++){
				picture[i][j]=inPicture[i][j];
			}
		}
	}

	void Calculate(char inPicture[50][50]){
		for (int i=0;i<r;i++){
			for (int j=0;j<c;j++){
				if ((inPicture[i][j]!='/')&&(inPicture[i][j]!='\\')){
					inPicture[i][j]=picture[i][j];
				}
				if (inPicture[i][j]=='#'){
					if (i==(r-1)){
						possible=false;
						break;
						break;
					}
					if (j==(c-1)){
						possible=false;
						break;
						break;
					}
					if ((picture[i+1][j]=='#')&&(picture[i+1][j+1]=='#')&&(picture[i][j+1]=='#')){
						inPicture[i][j]='/';
						inPicture[i+1][j]='\\';
						inPicture[i+1][j+1]='/';
						inPicture[i][j+1]='\\';
					}else{
						possible=false;
						break;
						break;
					}
				}
			}
		}
	}
};

int main() {
	ifstream in("inputFile.inp");
	ofstream out("outputFile.out");

	int c,r, T;

	Picture pic[MAX_CASES];
	char inPic[50][50];

	in>>T;

	for (int i=0;i<T;i++){
		in>>r;
		in>>c;
		for (int j=0;j<r;j++){
			in>>inPic[j];
		}
		pic[i].Set(inPic,r,c);
		pic[i].Calculate(inPic);
		out << "Case #" <<i+1<<":"<<endl;
		if (pic[i].possible){
			for (int k=0;k<r;k++)
			{
				for (int j=0;j<c;j++){
					out<<inPic[k][j];
				}
				out<<endl;
			}
		}else{
			out << "Impossible" <<endl;
		}
	}

	in.close();
	out.close();

	return 0;
}
