#include<set>
#include<map>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
#include<queue>
using namespace std;


int walk(int now, int wnext, int wtime)
{
	if(wtime>=abs(now - wnext)){
		return wnext;
	}
	if(wnext>now) return now+wtime;
	else return now - wtime;
}

int dir[4][2]={{0,0},{0,1},{1,0},{1,1}};
char dc[4]={'/','\\','\\','/'};

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outl.txt","w",stdout);
    
	int t;
	char ch[52][52];

	int r,c;
	bool im;
	cin >> t;
	for(int i=1;i<=t;i++){
		cin >> r >> c;
		for(int j=0;j<r;j++){
			for(int k=0;k<c;k++){
				cin >> ch[j][k];
			}
		}
		im=true;
		for(int j=0;j<r;j++){
			for(int k=0;k<c;k++){
				if(ch[j][k]=='#'){
					for(int x=0;x<4;x++){
						if(ch[j+dir[x][0]][k+dir[x][1]]!='#'||j+dir[x][0]==r||k+dir[x][1]==c){
							im=false;
							break;
						}
					}
					if(!im) break;
					else{
						for(int x=0;x<4;x++){
							ch[j+dir[x][0]][k+dir[x][1]]=dc[x];
						}
						k++;
					}
				}
			}
			if(!im) break;
		}

		if(!im){
			cout << "Case #" << i << ": " << endl;	
			cout << "Impossible" << endl;
		}
		else {
			cout << "Case #" << i << ": " << endl;	
			for(int j=0;j<r;j++){
				for(int k=0;k<c;k++){
					cout << ch[j][k];
				}
				cout << endl;
			}
		}

	}

}