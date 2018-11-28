#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define MAX 52

int R,C;
char pic[MAX][MAX];

bool replace(int posx,int posy)
{
	if(pic[posx][posy+1]=='#'&&
		pic[posx+1][posy]=='#'&&
		pic[posx+1][posy+1]=='#'){
			pic[posx][posy]='/';
			pic[posx][posy+1]='\\';
			pic[posx+1][posy]='\\';
			pic[posx+1][posy+1]='/';
	}else return false;
}


int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int testcase;
	cin>>testcase;

	int index=1;
	while(testcase--){
		cin>>R>>C;
		for(int i=0;i<R;i++){
			cin>>pic[i];
		}

		bool flag=true;
		for(int i=0;i<R&&flag;i++){
			for(int j=0;j<C&&flag;j++){
				if(pic[i][j]=='#'){
					if(j==C-1||i==R-1)flag=false;
					else flag=replace(i,j);
				}
			}
		}

		cout<<"Case #"<<index++<<":"<<endl;
		if(flag){
			for(int i=0;i<R;i++){
				cout<<pic[i]<<endl;
			}
		}else{
			cout<<"Impossible"<<endl;
		}
	}

	return 0;
}