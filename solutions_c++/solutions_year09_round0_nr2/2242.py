#include<iostream>
#include<queue>
using namespace std;

struct cell{
	int alt;
	int out[2];
	bool pick;
	char des;
	int i,j;
	cell ()
	{
		out[0]=-1;
		out[1]=-1;
		pick = false;
	}
};


void bfs(cell** area,int des,int W,int H,int r,int c) 
{
	queue< cell > q;
	
	q.push(area[r][c]);

	while(!q.empty()) {
		//cout  << "in queue for " << des << endl;
		cell tmp = q.front();
	      	q.pop();
		
		int i=tmp.i;
		int j=tmp.j;

		//cout << "CURRENT i=" << i << "j=" << j << endl;
		
		area[i][j].des = des;
		area[i][j].pick = true;
	
		if(tmp.out[0]!=-1 && tmp.pick == false) {
			q.push(area[tmp.out[0]][tmp.out[1]]) ;
			//cout << "OUT i=" << tmp.out[0] << "j= " << tmp.out[1] << endl;
		} 
		if(i-1>=0 && area[i-1][j].pick == false && area[i-1][j].out[0] == i && area[i-1][j].out[1] == j) {
			q.push(area[i-1][j]);
			//cout << "IN i=" << i-1 << "j=" << j << endl;			
		}
	       	if(j-1>=0 && area[i][j-1].pick == false && area[i][j-1].out[0] == i && area[i][j-1].out[1] == j) {
			q.push(area[i][j-1]);
			//cout << "IN i=" << i << "j=" << j-1 << endl;			
		}
		if(j+1< W && area[i][j+1].pick == false && area[i][j+1].out[0] == i && area[i][j+1].out[1] == j) {
			q.push(area[i][j+1]);
			//cout << "IN i=" << i << "j=" << j+1 << endl;			
		}
		if(i+1< H && area[i+1][j].pick == false && area[i+1][j].out[0] == i && area[i+1][j].out[1] == j) {
			q.push(area[i+1][j]);
		//	cout << "IN i=" << i+1 << "j=" << j << endl;			
		}
		
			
	}

}

int main()
{
	int T,H,W;

	cin >> T;

	for(int i=0;i<T;i++) {
		cin >> H >> W;

		cell** area;

		area  = new cell*[H];
		for(int j=0;j<H;j++) area[j] = new cell[W];

		
		for(int j=0;j<H;j++) {
			for(int k=0;k<W;k++) {
				cin >>  area[j][k].alt ; 
				area[j][k].i=j;
				area[j][k].j=k;
			}
		}

		for(int j=0;j<H;j++ ) {
			for(int k=0;k<W;k++) {
				int min=area[j][k].alt;
				int out[2];
				out[0]=-1;out[1]=-1;

				if(j-1 >= 0 && area[j-1][k].alt < min  ) {min = area[j-1][k].alt;out[0]=j-1;out[1]=k;}
				if(k-1 >= 0 && area[j][k-1].alt < min  ) {min = area[j][k-1].alt;out[0]=j;out[1]=k-1;}
				if(k+1 < W && area[j][k+1].alt < min  ) {min = area[j][k+1].alt;out[0]=j;out[1]=k+1;}
				if(j+1 < H && area[j+1][k].alt < min  ) {min = area[j+1][k].alt;out[0]=j+1;out[1]=k;}
			
				if(min < area[j][k].alt) {
					area[j][k].out[0]=out[0];
					area[j][k].out[1]=out[1];
				}
			}
		}
	
		int jj=0;
		for(int j=0;j<H;j++) {
			for(int k=0;k<W;k++) {
				if(area[j][k].pick == false) {
					area[j][k].i=j;	
					area[j][k].j=k;	
					bfs(area,97+jj,W,H,j,k );
					jj++;
				}
			}
		}


		cout << "Case #" << i+1 << ":" << endl;

		for(int j=0;j<H;j++) {
			for(int k=0;k<W;k++) {
				//cout << "alt = " << area[j][k].alt << " " ;
			     	//cout << " out " << area[j][k].out[0] << " " << area[j][k].out[1]  << " "; 
				cout << area[j][k].des << " " ;
			}
			cout << endl;
		}


	}

	return 0;
}
