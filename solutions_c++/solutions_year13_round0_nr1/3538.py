#include<iostream>
using namespace std;
char map[10][10];
int main(void)
{
	int t;
	int o1,o2,o3,o4,x1,x2,x3,x4, blank;
	bool flago = false, flagx = false;
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	cin>>t;

	for(int i = 0; i<t; i++){
		flago = flagx = false;
		for(int j = 1; j<=4; j++){
			for(int k = 1; k<=4; k++)
			{
				cin>>map[j][k];
			}
		}
		o3 = o4 =  x3 = x4 = blank = 0;
		for(int j = 1; j<=4; j++){
			o1 = x1 = o2 = x2 = 0;
			for(int k = 1; k<=4; k++){
				if(map[j][k] == 'T' || map[j][k] == 'O')o1++;
				if(map[j][k] == 'T' || map[j][k] == 'X')x1++;
				if(map[k][j] == 'T' || map[k][j] == 'O')o2++;
				if(map[k][j] == 'T' || map[k][j] == 'X')x2++; 
				if(map[j][k] == '.')blank++;
			}

			if(map[j][j] == 'T' || map[j][j] == 'O')o3++;
			if(map[j][5-j] == 'T' || map[j][5-j] == 'O')o4++;
			if(map[j][j] == 'T' || map[j][j] == 'X')x3++;
			if(map[j][5-j] == 'T' || map[j][5-j] == 'X')x4++;
			if(o1 == 4 || o2 == 4 || o3 == 4 || o4 == 4)flago = true;
			if(x1 == 4 || x2 == 4 || x3 == 4 || x4 == 4)flagx = true;
		}
		if(flago && !flagx){
			cout<<"Case #"<<i + 1<<": O won"<<endl;
		}
		else if(!flago && flagx){
			cout<<"Case #"<<i + 1<<": X won"<<endl;
		}
		else{
			if(blank == 0)cout<<"Case #"<<i + 1<<": Draw"<<endl;
			else cout<<"Case #"<<i + 1<<": Game has not completed"<<endl;
		}
	}
}