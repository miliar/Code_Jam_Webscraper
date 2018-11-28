#include<iostream>
#include<algorithm>
#include<queue>

using namespace std;

char l[102][102];
int h,w;
int dx[4]={0,-1,1,0};
int dy[4]={-1,0,0,1};
char c;

struct xy{
	int m;
	int px,py;
	vector<int> cx,cy;
} m[102][102];
bool operator<(xy a,xy b){
	return a.m<b.m;
}

void saiki(int x,int y){
//	cout << x << " " << y << endl;
	int i;
	for(i=0;i<m[y][x].cx.size();i++){
		if(l[m[y][x].cy[i]][m[y][x].cx[i]]=='?'){
			l[m[y][x].cy[i]][m[y][x].cx[i]]=c;
			saiki(m[y][x].cx[i],m[y][x].cy[i]);
		}
	}
}

int main()
{
	int i,j,k;
	int t;
	cin >> t;
	for(i=0;i<t;i++){
		for(j=0;j<102;j++){
			for(k=0;k<102;k++){
				m[j][k].m=999999;
				l[j][k]='?';
				m[j][k].cx.clear();
				m[j][k].cy.clear();
			}
		}
		
		cin >> h >> w;
		for(j=1;j<=h;j++){
			for(k=1;k<=w;k++){
				cin >> m[j][k].m;
			}
		}
		for(j=1;j<=h;j++){
			for(k=1;k<=w;k++){
				int mx=k;
				int my=j;
				for(int l=0;l<4;l++){
					if(m[my][mx].m>m[j+dy[l]][k+dx[l]].m){
						my=j+dy[l];
						mx=k+dx[l];
					}
				}
				if(mx==k && my==j){
					m[my][mx].px=mx;
					m[my][mx].py=my;
				}else{
					m[j][k].px=mx;
					m[j][k].py=my;
					m[my][mx].cx.push_back(k);
					m[my][mx].cy.push_back(j);
				}
			}
		}
		
		c='a';
		for(j=1;j<=h;j++){
			for(k=1;k<=w;k++){
				if(l[j][k]=='?'){
					int tx=k;
					int ty=j;
					while(m[ty][tx].px!=tx || m[ty][tx].py!=ty){
						tx=m[ty][tx].px;
						ty=m[ty][tx].py;
					}
					l[ty][tx]=c;
//					cout << c << endl;
					saiki(tx,ty);
					c++;
				}
			}
		}
		
		cout << "Case #" << i+1 << ":" << endl;
		for(j=1;j<=h;j++){
			for(k=1;k<w;k++){
				cout << l[j][k] << " ";
			}
			cout << l[j][k] << endl;
		}
	}
	return 0;
}
