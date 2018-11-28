#include<iostream>
//#include<fstream>

using namespace std;
char A[5][5];

int main(){
	int n,i,j,k,fill=0;
	char kar;
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.txt","w",stdout);
	cin>>n;
	for (i=0;i<n;i++){
		for (j=0;j<4;j++){
			for (k=0;k<4;k++){
				cin>>A[j][k];
				if (A[j][k]!='.')
					fill++;
			}
		}cout<<"Case #"<<i+1<<": ";
		for (j=0;j<4;j++){
			kar=A[j][0];
			if (kar=='T')
				kar=A[j][1];
			if (kar=='X' || kar=='O'){
				for (k=1;k<4;k++){
					if (kar!=A[j][k] && A[j][k]!='T')
						break;
				}if (k==4){
					cout<<kar<<" won"<<endl;
					break;
				}
			}
		}if (j==4){
			for (j=0;j<4;j++){
				kar=A[0][j];
				if (kar=='T')
					kar=A[1][j];
				if (kar=='X' || kar=='O'){
					for (k=1;k<4;k++){
						if (kar!=A[k][j] && A[k][j]!='T')
							break;
					}if (k==4){
						cout<<kar<<" won"<<endl;
						break;
					}
				}
			}if (j==4){
				kar=A[0][0];
				if (kar=='T')
					kar=A[1][1];
				if (kar=='X' || kar=='O'){
					for (k=1;k<4;k++){
						if (kar!=A[k][k] && A[k][k]!='T')
							break;
					}if (k==4)
						cout<<kar<<" won"<<endl;
				}if (k<4 || kar=='.'){
					kar=A[3][0];
					if (kar=='T')
						kar=A[2][1];
					if (kar=='X' || kar=='O'){
						for (k=1;k<4;k++){
							if (kar!=A[3-k][k] && A[3-k][k]!='T')
								break;
						}if (k==4)
							cout<<kar<<" won"<<endl;
					}if (k<4 || kar=='.'){
						if (fill==16)
							cout<<"Draw"<<endl;
						else
							cout<<"Game has not completed"<<endl;
					}
				}
			}
		}fill=0;
	}
}
