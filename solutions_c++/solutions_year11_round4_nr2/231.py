#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <math.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef vector<ii> vii;
#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define loop(i,n) for(int i=0; i<(n); i++)
#define tr(it,c) for(it=(c).begin(); it!=(c).end(); it++)
#define tr2(it1,c,it2,d) for(it1=(c).begin(),it2=(d).begin(); it1!=(c).end(); it1++,it2++)

string solve(int& R, int& C, const vvi& D)
{
	vii center(min(R,C)+1);
	vi weight(min(R,C)+1);
	int maxsize = 0;
	loop(r, R-2) loop(c, C-2)
	{
		for(int size=3; size<=min(R-r, C-c); size++)
		{
			if(size == 3)
			{
				center[size].first = D[r+1][c]+D[r+1][c+1]+D[r+1][c+2] + 2*(D[r+2][c]+D[r+2][c+1]+D[r+2][c+2]);
				center[size].second = D[r][c+1]+D[r+1][c+1]+D[r+2][c+1] + 2*(D[r][c+2]+D[r+1][c+2]+D[r+2][c+2]);
				weight[size] = D[r][c]+D[r][c+1]+D[r][c+2] + D[r+1][c]+D[r+1][c+1]+D[r+1][c+2] + D[r+2][c]+D[r+2][c+1]+D[r+2][c+2];
			}
			else
			{
				int dr=0, dc=0, dw=0;
				loop(i, size-1)
				{
					dr += (size-1) * D[r+size-1][c+i];
					dc += i * D[r+size-1][c+i];
					dr += i * D[r+i][c+size-1];
					dc += (size-1) * D[r+i][c+size-1];
					dw += D[r+size-1][c+i] + D[r+i][c+size-1];
				}
				dr += (size-1) * D[r+size-1][c+size-1];
				dc += (size-1) * D[r+size-1][c+size-1];
				dw += D[r+size-1][c+size-1];
				center[size].first = center[size-1].first + dr;
				center[size].second = center[size-1].second + dc;
				weight[size] = weight[size-1] + dw;
			}
			int c_r = center[size].first - (size-1)*(D[r+size-1][c]+D[r+size-1][c+size-1]);
			int c_c = center[size].second - (size-1)*(D[r][c+size-1]+D[r+size-1][c+size-1]);
			int c_w = weight[size] - (D[r][c]+D[r][c+size-1]+D[r+size-1][c]+D[r+size-1][c+size-1]);
			if(c_r*2 == (size-1)*c_w && c_c*2 == (size-1)*c_w)
				maxsize = max(maxsize, size);
		}
	}
	char answer[11];
	if(maxsize > 0)
		sprintf(answer, "%d", maxsize);
	else
		strcpy(answer, "IMPOSSIBLE");
	return answer;
}

void preprocess(){}

void readinput(int& R, int& C, vvi& D)
{
	int base;
	cin>>R>>C>>base;
	D.resize(R, vi(C));
	loop(i, R)
	{
		string str;
		cin>>str;
		loop(j, C)
			D[i][j] = str[j]-'0';
	}
}

vs getoutput()
{
	int R, C;
	vvi D;
	readinput(R, C, D);
	string answer = solve(R, C, D);
	return vs(1, answer);
}

void main()
{
//	freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
	freopen("test\\B-small-attempt0.in", "r", stdin);freopen("test\\B-small-attempt0.out", "w", stdout);
//	freopen("test\\B-large.in", "r", stdin);freopen("test\\B-large.out", "w", stdout);
	int testcase;
	cin>>testcase;
	preprocess();
	for(int i=1; i<=testcase; i++)
	{
		cout<<"Case #"<<i<<": ";
		vs answer = getoutput();
		loop(j, sz(answer))
			cout<<answer[j]<<endl;
	}
	fclose(stdin);
	fclose(stdout);
}