#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <cmath>

using namespace std;

int main(){
	ifstream in;
	ofstream out;
	
	in.open("A-large.in");
	out.open("output.txt");

	

	int T;
	in>>T;


	for(int u=0;u<T;u++){

		int tile[50][50];
		char final[50][50];

		int R,C;
		in>>R>>C;

		int B=0;

		for(int i=0;i<R;i++){
			string temp;
			in>>temp;
			for(int j=0;j<C;j++){
				if(temp[j]=='.'){
					tile[i][j]=0;
				}
				else{
					tile[i][j]=1;
					B++;
				}
			}
		}

		vector<int> possible;
		int stat=0;
		//checking if possible and storing values;
		for(int i=0;i<R;i++){
			stat=0;
			for(int j=0;j<C;j++){
				if(tile[i][j]==1){
					if(i+1>=R || j+1>=C){
						stat=1;
						break;
					}
					else{
						if(tile[i][j]==1&&tile[i+1][j]==1&&tile[i][j+1]==1&&tile[i+1][j+1]==1){
							tile[i][j]=2;
							tile[i+1][j]=2;
							tile[i][j+1]=2;
							tile[i+1][j+1]=2;
							final[i][j]='/';
							final[i+1][j]='\\';
							final[i][j+1]='\\';
							final[i+1][j+1]='/';
							possible.push_back(i);
							possible.push_back(j);
						}
						else{
							stat=1;
						}
					}
				}
				else if(tile[i][j]==0){
					final[i][j]='.';
				}
			}
			if(stat==1){
				break;
			}
		}

		out<<"Case #"<<(u+1)<<":"<<endl;
		if(stat==1){//impossible
			out<<"Impossible"<<endl;
			continue;
		}
		else{
			for(int i=0;i<R;i++){
				for(int j=0;j<C;j++){
					out<<(char)final[i][j];
				}
				out<<endl;
			}

		}


		/*for(int i=0;i<R;i++){
			for(int j=0;j<C;j++){
				cout<<tile[i][j]<<" ";
			}
			cout<<endl;
		}*/


	}

	in.close();
	out.close();

	return 0;
}