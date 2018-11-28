#include<iostream>
#define fark(x,y) ((x)>(y) ? (x)-(y) : (y)-(x))
using namespace std;
int T;
int order[102];
int buttons[2][102];
int buttonsin[2][102];
int main(){
	cin >> T;
	for(int t=1;t<=T;t++){
		int cnt[2];
		cnt[0]= cnt[1]=0;
		cout << "Case #" << t << ": ";
		int N;
		cin >> N;
		for(int i=0;i<N;i++){
			int x,y;
			char ch;
			cin >> ch >> x;
			y = ch =='O' ? 0 : 1;
			buttonsin[y][cnt[y]++]=x;
			order[i]=y;
		}
		buttons[0][0]=buttonsin[0][0];
		buttons[1][0]=buttonsin[1][0];
		for(int i=1;i<cnt[0];i++)
			buttons[0][i] = fark(buttonsin[0][i-1],buttonsin[0][i])+1;
		for(int i=1;i<cnt[1];i++)
			buttons[1][i] = fark(buttonsin[1][i-1],buttonsin[1][i])+1;
		int ii[2],pos[2];
		ii[0]=ii[1]=0;
		pos[0]=pos[1]=1;
		int i=0,top=0;
		while(ii[0]!=cnt[0] || ii[1]!=cnt[1]){
			int x = order[i];
			int y = 1-x;
			int d=buttons[x][ii[x]];
			top+=d;
			ii[x]++;
			if(buttons[y][ii[y]] > d)
				buttons[y][ii[y]]-=d;
			else buttons[y][ii[y]]=1;
			i++;
		}
		cout << top << endl;
	}
}
