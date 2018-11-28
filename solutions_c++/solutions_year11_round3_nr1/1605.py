#include <iostream>
#include <algorithm>
using namespace std;

char pic[50][50];

int main(){

	int T;
	cin>>T;

	for (int i=0;i<T;i++){
		cout<<"Case #"<<i+1<<":";
		
		int R,C;
		cin>>R>>C;

		for (int r=0;r<R;r++){
			for (int c=0;c<C;c++){
				cin>>pic[r][c];
			
			}
		}

		bool blue_to_red=true;
		for (int r=0;r<R;r++){
			for (int c=0;c<C;c++){
				if (pic[r][c]=='#'){
					if (r==R || c==C) {
						blue_to_red=false;
						break;
					}
					if (pic[r+1][c]!='#' || pic[r][c+1]!='#' || pic[r+1][c+1]!='#'){
						blue_to_red=false;
						break;
					}
					pic[r][c]='/';
					pic[r][c+1]='\\';
					pic[r+1][c]='\\';
					pic[r+1][c+1]='/';
				}
			
			}
			if(!blue_to_red) break;
		}

		cout<<endl;
		if (blue_to_red){
			for (int r=0;r<R;r++){
				for (int c=0;c<C;c++)
					cout<<pic[r][c];
				cout<<endl;
			};
		}
		else cout<<"Impossible"<<endl;
	}


	return 0;
}
