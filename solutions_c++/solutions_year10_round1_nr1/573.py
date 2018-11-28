#include <iostream>
#include <cmath>
#include <vector>
#include <string>
using namespace std;



int main(void)
{
	int CASES;
	cin >> CASES;
	for(int cn=1;cn<=CASES;++cn)
	{
		int N,K;
		cin >> N >> K;
		vector<string> vs(N,string());
		for(int i=0;i<N;++i)
		{
			cin >> vs[i];
		}
		vector<string> out = vs;
		for(int i=0;i<N;++i)
		{
			for(int j=0;j<N;++j)
			{
				out[i][j] = vs[N-1-j][i];
			}
		}
		//gravity
		for(int c=0;c<N;++c)
		{
			int cur = N-1;
			for(int i=N-1;i>=0;--i)
			{
				if(out[i][c] != '.'){out[cur][c] = out[i][c];
					if(i != cur){out[i][c] = '.';}
					--cur;
				}
			}
		}
	//	for(int i=0;i<N;++i)
	//	{cout << out[i] << endl;}
		bool red = false,blue = false;
		for(int i=0;i<N;++i)
		{
			for(int j=0;j<N;++j)
			{
				if(out[i][j] == '.')continue;
				int r,c;
				bool yay;
#define doit(dr,dc) yay = true;r = i;c = j;for(int t=1;t<K;++t){r += dr;c += dc;\
					if(r < 0 || r>= N || c <0 || c >= N || out[r][c] != out[i][j]){yay = false;break;}\
				}\
				if(yay){goto success;}
				doit(0,1);
				doit(1,0);
				doit(1,1);
				doit(1,-1);
				continue;
success:
				if(out[i][j] == 'R'){red = true;}
				else{blue = true;}
			}
		}
		printf("Case #%d: ",cn);
		if(red && blue){cout << "Both" << endl;}
		else if(red) {cout << "Red" << endl;}
		else if(blue){cout << "Blue" << endl;}
		else{cout << "Neither" << endl;}
	}
	return 0;
}
