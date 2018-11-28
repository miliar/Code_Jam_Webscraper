#include<cstdio>
#include<cmath>
#include<vector>
#include<algorithm>
#include<iostream>
#include<string>
using namespace std;

int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,p;
	int x,o;
	vector<string> input;
	input.resize(4);
	while(scanf("%d",&T)!=EOF){
		vector<int> result;
		vector<int> dot;
		dot.resize(T);
		result.resize(T);
		for(int i=0;i<T;i++){
			result[i]=0;
			dot[i]=0;
			for(int j=0;j<4;j++){
				cin>>input[j];
			}
			for(int j=0;j<4;j++){//row
				x=0;
				o=0;
				for(int k=0;k<3;k++){
					if(input[j][k]=='X'){
						if(input[j][k+1]!='X' && input[j][k+1]!='T') break;
						x++;
					}
					else if(input[j][k]=='O'){
						if(input[j][k+1]!='O' && input[j][k+1]!='T') break;
						o++;
					}
					else if(input[j][k]=='.'){
						dot[i]=1;
						break;
					}
					else if(input[j][k]=='T'){
						x++;
						o++;
					}
				}
				if(x==3){
					result[i]=1;
					break;
				}
				else if(o==3){
					result[i]=2;
					break;
				}
			}
			for(int k=0;k<4;k++){//col
				x=0;
				o=0;
				for(int j=0;j<3;j++){
					if(input[j][k]=='X'){
						if(input[j+1][k]!='X' && input[j+1][k]!='T') break;
						x++;
					}
					else if(input[j][k]=='O'){
						if(input[j+1][k]!='O' && input[j+1][k]!='T') break;
						o++;
					}
					else if(input[j][k]=='.'){
						dot[i]=1;
						break;
					}
					else if(input[j][k]=='T'){
						x++;
						o++;
					}
				}
				if(x==3){
					result[i]=1;
					break;
				}
				else if(o==3){
					result[i]=2;
					break;
				}
			}
			x=0;
			o=0;
			for(int j=0;j<4;j++){//dia1
				if(input[j][j]=='X'){
					if(input[j+1][j+1]!='X' && input[j+1][j+1]!='T') break;
					x++;
				}
				else if(input[j][j]=='O'){
					if(input[j+1][j+1]!='O' && input[j+1][j+1]!='T') break;
					o++;
				}
				else if(input[j][j]=='.'){
					dot[i]=1;
					break;
				}
				else if(input[j][j]=='T'){
					x++;
					o++;
				}
				if(x==3){
					result[i]=1;
					break;
				}
				else if(o==3){
					result[i]=2;
					break;
				}
			}
			p=3;
			x=0;
			o=0;
			for(int j=0;j<4;j++){//dia2
				if(input[j][p]=='X'){
					if(input[j+1][p-1]!='X' && input[j+1][p-1]!='T') break;
					x++;
				}
				else if(input[j][p]=='O'){
					if(input[j+1][p-1]!='O' && input[j+1][p-1]!='T') break;
					o++;
				}
				else if(input[j][p]=='.'){
					dot[i]=1;
					break;
				}
				else if(input[j][p]=='T'){
					x++;
					o++;
				}
				if(x==3){
					result[i]=1;
					break;
				}
				else if(o==3){
					result[i]=2;
					break;
				}
				p--;
			}
		}
		for(int i=0;i<T;i++){
			if(result[i]==1)
				cout<<"Case #"<<i+1<<": X won"<<endl;
			else if(result[i]==2)
				cout<<"Case #"<<i+1<<": O won"<<endl;
			else if(result[i]==0 && dot[i]==1)
				cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
			else if(result[i]==0 && dot[i]==0)
				cout<<"Case #"<<i+1<<": Draw"<<endl;
		}
	}
	return 0;
}