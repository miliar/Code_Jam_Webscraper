#include<iostream>
#include<cstdio>
#include<string.h>
#include<cstring>
#include<string>
using namespace std;
char str[4][4];
bool flag1;
bool flag2;
int main()
{
	freopen("input.in","r",stdin);
        freopen("output.txt","w",stdout);
	int i,j,k,sum=0,t;
	cin >> t;
	for(k=1;k<=t;k++){
		flag1 = false;
		flag2 = false;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin >> str[i][j];
				if(str[i][j] == '.')
					flag2 = true;
			}
		}
		for(i=0;i<4;i++){
			sum = 0;
			sum = (str[i][0] + str[i][1] + str[i][2] + str[i][3]);
			if(sum == 352 || sum == 348){
				flag1=true;
				cout << "Case #"<< k <<": X won";
				break;
			}
		else if(sum == 316 || sum == 321){
				flag1=true;
				cout << "Case #"<< k << ": O won";
				break;
			}
		}
		if(flag1==false){
			for(i=0;i<4;i++){
				sum = 0;
				sum = (str[0][i] + str[1][i] + str[2][i] + str[3][i]);
				if(sum == 352 || sum == 348){
					flag1 = true;
					cout << "Case #"<< k<<": X won";
					break;
				}
			     else if(sum == 316 || sum == 321){
					flag1 = true;
					cout << "Case #"<< k<<": O won";
					break;
				}
			}
		}
		if(flag1==false){
			int sum1 = 0;
			int sum2 = 0;
			sum1 = str[0][0] + str[1][1] + str[2][2] + str[3][3];
			sum2 = str[0][3] + str[1][2] + str[2][1] + str[3][0];
			if(sum1 == 352 || sum1 == 348 || sum2 == 352 || sum2 == 348){
				flag1=true;
				cout << "Case #"<< k <<": X won";
			}

	       		else if(sum1 == 316 || sum1 == 321 || sum2 == 316 || sum2 == 321){
				flag1=true;
				cout <<"Case #"<<k<<": O won";
			}
		}

		if(flag1 == false){
			if(flag2==true){
				flag1=true;
				cout << "Case #"<< k <<": Game has not completed";
			}
		}
	       if(flag1==false)
			cout<<"Case #"<<k<<": Draw";

		cout << "\n";
	}
	return 0;
}
			

