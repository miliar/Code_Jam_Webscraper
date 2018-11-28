#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<queue>
#include<algorithm>

using namespace std;

int main(){
	int T;
	cin>>T;
	for(int testcase=1;testcase<=T;testcase++){
		int R,C;
		cin>>R>>C;
		vector<string> data(R);
		for(int i=0;i<R;i++)
			cin>>data[i];
		bool flag=true;
		for(int i=0;i<R&&flag;i++)
			for(int j=0;j<C&&flag;j++)
				if(data[i][j]=='#'){
					if(i<R-1&&j<C-1&&data[i+1][j]=='#'&&data[i][j+1]=='#'&&data[i+1][j+1]=='#'){
						data[i][j]='/';
						data[i+1][j]='\\';
						data[i][j+1]='\\';
						data[i+1][j+1]='/';
					}else{
						flag=false;
					}
				}
		cout<<"Case #"<<testcase<<":"<<endl;
		if(flag){
			for(int i=0;i<R;i++)
				cout<<data[i]<<endl;
		}else
			cout<<"Impossible"<<endl;
		
	}
	return 0;
}
