#include <iostream>
using namespace std;

int main()
{
	int T,H,W,map[100][100];
	char smap[100][100], label, cd;
	bool cont;
	int dh[4]={-1,0,0,1}, dw[4]={0,-1,1,0}, dir, alt, nh, nw;

	cin>>T;
	for (int t=1; t<=T; t++) {
		cin>>H>>W;
		for (int h=0; h<H; h++)
			for (int w=0; w<W; w++) cin>>map[h][w];
			
		for (int h=0; h<H; h++)
			for (int w=0; w<W; w++) {
				dir=-1;
				alt=map[h][w];
				for (int d=0; d<4; d++) {
					nh=h+dh[d];
					nw=w+dw[d];
					if (nh<0 || nh>=H || nw<0 || nw>=W) continue;
					if (alt>map[nh][nw]) {
						dir=d;
						alt=map[nh][nw];
					}
					if (dir<0) smap[h][w]=4;
					else smap[h][w]=dir;
				}
			}

		nh=nw=0;
		cd=smap[nh][nw];
		while (cd<4) {
			smap[nh][nw]='a';
			switch (cd) {
			case 0: nh--; break;
			case 1: nw--; break;
			case 2: nw++; break;
			case 3: nh++; break;
			default: cerr<<"No way!"<<endl;
			}
			cd=smap[nh][nw];
		}
		smap[nh][nw]='a';
		
		label='b';
		for (int h=0; h<H; h++)
			for (int w=0; w<W; w++) if (smap[h][w]==4) smap[h][w]=label++;
		
		cont=true;
		while (cont) {
			cont=false;
			for (int h=0; h<H; h++)
				for (int w=0; w<W; w++)
					if (smap[h][w]<4) {
						cont=true;
						nh=h;
						nw=w;
						switch (smap[h][w]) {
						case 0: nh--; break;
						case 1: nw--; break;
						case 2: nw++; break;
						case 3: nh++; break;
						}
						if (smap[nh][nw]>='a') smap[h][w]=smap[nh][nw];
					}
		}
			
		cout<<"Case #"<<t<<":"<<endl;
		for (int h=0; h<H; h++) {
			for (int w=0; w<W; w++) cout<<smap[h][w]<<" ";
			cout<<endl;
		}
	}
	return 0;
}

