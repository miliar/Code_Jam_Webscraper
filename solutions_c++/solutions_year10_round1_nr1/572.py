#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ofstream fout ("g101aa.out");
	ifstream fin ("g101aa.in");
	int numCases;
	fin>>numCases;
	for(int caseNum=0; caseNum<numCases; caseNum++){
		int length, need, original[50][50], rot[50][50], height[50];
		bool win[3];
		fin>>length>>need;
		for(int i=0; i<length; i++){
			fin.get();
			for(int j=0; j<length; j++){
				int c=fin.get();
				if(c=='R')
					original[i][j]=1;
				else if(c=='B')
					original[i][j]=2;
				else
					original[i][j]=0;
				rot[i][j]=0;
			}
		}
		for(int i=0; i<length; i++){
			height[i]=0;
			for(int j=length-1; j>=0; j--)
				if(original[i][j]){
					rot[i][height[i]]=original[i][j];
					height[i]++;
				}
		}
		for(int n=1; n<=2; n++)
			win[n]=false;
		for(int i=0; i<length; i++){
			int last=0, chain=0;
			for(int j=0; j<length; j++){
				if(rot[i][j]!=last){
					last=rot[i][j];
					chain=0;
				}
				chain++;
				if(chain>=need)
					win[last]=true;
			}
		}
		for(int i=0; i<length; i++){
			int last=0, chain=0;
			for(int j=0; j<length; j++){
				if(rot[j][i]!=last){
					last=rot[j][i];
					chain=0;
				}
				chain++;
				if(chain>=need)
					win[last]=true;
			}
		}
		for(int i=0; i<length; i++){
			int last=0, chain=0;
			for(int j=0; j<length-i; j++){
				if(rot[j][i+j]!=last){
					last=rot[j][i+j];
					chain=0;
				}
				chain++;
				if(chain>=need)
					win[last]=true;
			}
		}
		for(int i=1; i<length; i++){
			int last=0, chain=0;
			for(int j=0; j<length-i; j++){
				if(rot[i+j][j]!=last){
					last=rot[i+j][j];
					chain=0;
				}
				chain++;
				if(chain>=need)
					win[last]=true;
			}
		}
		for(int i=0; i<length; i++){
			int last=0, chain=0;
			for(int j=0; j<=i; j++){
				if(rot[j][i-j]!=last){
					last=rot[j][i-j];
					chain=0;
				}
				chain++;
				if(chain>=need)
					win[last]=true;
			}
		}
		for(int i=1; i<length; i++){
			int last=0, chain=0;
			for(int j=0; j<=i; j++){
				if(rot[i+j][length-j-1]!=last){
					last=rot[i+j][length-j-1];
					chain=0;
				}
				chain++;
				if(chain>=need)
					win[last]=true;
			}
		}
		fout<<"Case #"<<caseNum+1<<": ";
		if(win[1] && win[2])
			fout<<"Both"<<endl;
		else if(win[1])
			fout<<"Red"<<endl;
		else if(win[2])
			fout<<"Blue"<<endl;
		else
			fout<<"Neither"<<endl;
	}
	return 0;
}
