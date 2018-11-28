#include <fstream>
#include <iostream>
#include <string>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");
#define cin fin
#define cout fout

#define x(i,j) (a[i][j]=='X' || a[i][j]=='T')
#define o(i,j) (a[i][j]=='O' || a[i][j]=='T')
#define p(i) (a[i][0]=='.' || a[i][1]=='.' || a[i][2]=='.' || a[i][3]=='.')

int main()
{
	int n;
	cin>>n;
	for(int x=1;x<=n;x++){
		char a[4][4];
		for(int i=0;i<4;i++) cin>>a[i][0]>>a[i][1]>>a[i][2]>>a[i][3];
		cout<<"Case #"<<x<<": ";
		int oup=0;
		for(int i=0;i<4;i++) if(x(i,0)&&x(i,1)&&x(i,2)&&x(i,3)) oup++,cout<<"X won"<<endl;
		for(int i=0;i<4;i++) if(!oup &&x(0,i)&&x(1,i)&&x(2,i)&&x(3,i)) oup++,cout<<"X won"<<endl;
		if(!oup &&x(0,0)&&x(1,1)&&x(2,2)&&x(3,3)) oup++,cout<<"X won"<<endl;
		if(!oup &&x(0,3)&&x(1,2)&&x(2,1)&&x(3,0)) oup++,cout<<"X won"<<endl;
		for(int i=0;i<4;i++) if(!oup &&o(i,0)&&o(i,1)&&o(i,2)&&o(i,3)) oup++,cout<<"O won"<<endl;
		for(int i=0;i<4;i++) if(!oup &&o(0,i)&&o(1,i)&&o(2,i)&&o(3,i)) oup++,cout<<"O won"<<endl;
		if(!oup &&o(0,0)&&o(1,1)&&o(2,2)&&o(3,3)) oup++,cout<<"O won"<<endl;
		if(!oup &&o(0,3)&&o(1,2)&&o(2,1)&&o(3,0)) oup++,cout<<"O won"<<endl;
		if(!oup){
			if(p(0)||p(1)||p(2)|| p(3)) cout<<"Game has not completed"<<endl;
			else cout<<"Draw"<<endl;
		}
	}
}