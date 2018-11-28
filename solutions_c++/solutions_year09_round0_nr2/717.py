#include<iostream>
#include<vector>
using namespace std;

vector< vector <int> > map;
vector< vector <char> > sol;
char curletter;
int H,W;

void recur(int h,int w)
{
	

	if(sol[h][w] != ' ' )
		return;

	int nh,nw;
	int cur = map[h][w];
	int curh = h,curw = w;



	nh = h-1;
	nw = w;
	if ( nh>=0 && nh<H && nw>=0 && nw<W) {
		if (map[nh][nw] < cur ) {
			curh = nh;
			curw = nw;
			cur = map[nh][nw];
		}
	}

	
	
	nh = h;
	nw = w-1;
	if ( nh>=0 && nh<H && nw>=0 && nw<W) {
		if (map[nh][nw] < cur ) {
			curh = nh;
			curw = nw;
			cur = map[nh][nw];
		}
	}


	nh = h;
	nw = w+1;
	if ( nh>=0 && nh<H && nw>=0 && nw<W) {
		if (map[nh][nw] < cur ) {
			curh = nh;
			curw = nw;
			cur = map[nh][nw];
		}
	}


	nh = h+1;
	nw = w;
	if ( nh>=0 && nh<H && nw>=0 && nw<W) {
		if (map[nh][nw] < cur ) {
			curh = nh;
			curw = nw;
			cur = map[nh][nw];
		}
	}

	if(curh==h && curw==w) {
		//end;
		sol[h][w] = curletter;
		
		curletter++;
	} else {
		
		recur(curh,curw);
		sol[h][w] = sol[curh][curw];
	}
};

int main()
{
	int testcase;
	cin >> testcase;
	for(int t=0;t<testcase;t++) {
		cin >> H >> W ;
		map = vector< vector <int> >(H,vector<int>(W));
		sol = vector< vector <char> >(H,vector<char>(W,' '));

		for(int h=0;h<H;h++) {
			for(int w=0;w<W;w++) {
				int input;
				cin >> input;
				map[h][w] = input;
			}
		}
		curletter = 'a';

		for(int h=0;h<H;h++) {
			for(int w=0;w<W;w++) {
				recur(h,w);
			}
		}

		cout << "Case #" << t+1 << ":" <<endl;
		for(int h=0;h<H;h++) {
			for(int w=0;w<W;w++) {
				cout << sol[h][w];
				if ( w < W-1 )
					cout << ' ' ;
			}
			cout << endl;
		}
		
	}
}