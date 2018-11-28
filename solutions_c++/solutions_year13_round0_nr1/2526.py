#include<iostream>
using namespace std;
int main(){
	int n;
	int t;
	int loop=0;
	freopen("test.txt","w",stdout);
	cin>>t;

	while (loop<t){
		loop++;
		char a[4][4];
		for (int i=0;i<4;++i){
			for (int j=0;j<4;++j){
				cin>>a[i][j];
			}
		}
		bool flag=false;
		int count=0;
		bool toe=false;
		bool empty=false;
		for (int i=0;i<4;++i){
			count=0;
			for (int j=0;j<4;++j){
				if (a[i][j]=='X')count++;
				else if (a[i][j]=='O')count--;
				else if (a[i][j]=='T')toe=true;
				else if (a[i][j]=='.')empty=true;
			}
			if (count==4 || (count==3 && toe==true)){
					cout<<"Case #"<<loop<<": X won"<<endl;
					flag=true;
					break;
			}else
			if (count==-4 || (count==-3 && true==toe)){
				cout<<"Case #"<<loop<<": O won"<<endl;
				flag=true;
				break;
			}
		}
		if (flag!=true){
			for (int j=0;j<4;++j){
				count=0;
				toe=false;
				for (int i=0;i<4;++i){
					if (a[i][j]=='X')count++;
					else if (a[i][j]=='O')count--;
					else if (a[i][j]=='T')toe=true;
					else if (a[i][j]=='.')empty=true;
				}
				if (count==4 || (count==3 && toe==true)){
						cout<<"Case #"<<loop<<": X won"<<endl;
						flag=true;
						break;
				}else
				if (count==-4 || (count==-3 && true==toe)){
					cout<<"Case #"<<loop<<": O won"<<endl;
					flag=true;
					break;
				}
			}
		}
		if (flag!=true){
			count=0;
			toe=false;
			for (int i=0;i<4;++i){
				if (a[i][i]=='X')count++;
					else if (a[i][i]=='O')count--;
					else if (a[i][i]=='T')toe=true;
					else if (a[i][i]=='.')empty=true;
				}
			if (count==4 || (count==3 && toe==true)){
						cout<<"Case #"<<loop<<": X won"<<endl;
						flag=true;
				}else
				if (count==-4 || (count==-3 && true==toe)){
					cout<<"Case #"<<loop<<": O won"<<endl;
					flag=true;
				}
		}
		if (flag!=true){
			count=0;
			toe=false;
			for (int i=0;i<4;++i){
				if (a[i][3-i]=='X')count++;
					else if (a[i][3-i]=='O')count--;
					else if (a[i][3-i]=='T')toe=true;
					else if (a[i][3-i]=='.')empty=true;
				}
			if (count==4 || (count==3 && toe==true)){
						cout<<"Case #"<<loop<<": X won"<<endl;
						flag=true;
				}else
				if (count==-4 || (count==-3 && true==toe)){
					cout<<"Case #"<<loop<<": O won"<<endl;
					flag=true;
				}
		}
		if (flag==false &&empty==true)cout<<"Case #"<<loop<<": Game has not completed"<<endl;
		else if (flag==false &&  empty==false)cout<<"Case #"<<loop<<": Draw"<<endl;
	}
}