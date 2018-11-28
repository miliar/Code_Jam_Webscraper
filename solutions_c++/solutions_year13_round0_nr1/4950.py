#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <utility>
#include <functional>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <climits>
#include <cassert>
using namespace std;
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long ll;
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define EACH(t,i,c) for(t::iterator i=(c).begin(); i!=(c).end(); ++i)
const double EPS = 1e-10;
const double PI  = acos(-1.0);

int dx[]={-1,0,1,1,1,0,-1,-1},dy[]={-1,-1,-1,0,1,1,1,0};
int main() {
	int t;
	cin>>t;
	for (int test = 1;test <= t;	test++)
	{
		vs board(4);
		for (int i = 0; i < 4; i++)
		{
			cin>>board[i];
		}
		bool goingon=false;
		string state;
		for (int d = 0; d < 8; d++)
		{
			for (int y = 0; y < 4; y++)
			{
				for (int x = 0; x < 4; x++)
				{
					for (int col = 0; col < 2; col++)
					{
						char c;
						if(col==0){
							c='O';
						}else{
							c='X';
						}
						int cnt=0;
						for (int i = 0; i < 4; i++)
						{
							int yy=y+dy[d]*i,xx=x+dx[d]*i;
							if(yy>=0&&xx>=0&&yy<4&&xx<4){
								if(board[yy][xx]==c||board[yy][xx]=='T'){
									cnt++;
								}else if(board[yy][xx]=='.'){
									goingon=true;
								}
							}
						}
						if(cnt==4){
							stringstream ss;
							ss<<c<<" won";
							state=ss.str();
							goto end;
						}
					}
				}
			}
		}
		if(goingon){
			state="Game has not completed";
		}else{
			state="Draw";
		}
end:

		cout<<"Case #"<<test<<": ";
		cout<<state<<endl;
	}
}