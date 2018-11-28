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

int checksymmetry(const vvi& data, int r, int c)
{
	int k = sz(data);
	bool valid = true;
	loop(i, k) loop(j, k)
	{
		int i2 = r-c+j;
		int j2 = i-r+c;
		if(i2>=0 && i2<k && j2>=0 && j2<k && data[i2][j2]!=data[i][j])
		{
			valid = false;
			break;
		}
		int i3 = r+c-j;
		int j3 = r+c-i;
		if(i3>=0 && i3<k && j3>=0 && j3<k && data[i3][j3]!=data[i][j])
		{
			valid = false;
			break;
		}
	}
	if(!valid)
		return -1;
	else
	{
		int relai = abs(2*r-k+1);
		int relaj = abs(2*c-k+1);
		return max(relai, relaj);
	}
}

int halfchecksymmetry(const vvi& data, int r, int c)
{
	int k = sz(data);
	bool valid = true;
	loop(i, k) loop(j, k)
	{
		int i2 = r-c+j;
		int j2 = i-r+c;
		if(i2>=0 && i2<k && j2>=0 && j2<k && data[i2][j2]!=data[i][j])
		{
			valid = false;
			break;
		}
		int i3 = r+c+1-j;
		int j3 = r+c+1-i;
		if(i3>=0 && i3<k && j3>=0 && j3<k && data[i3][j3]!=data[i][j])
		{
			valid = false;
			break;
		}
	}
	if(!valid)
		return -1;
	else
	{
		int relai = abs(2*r-k+2);
		int relaj = abs(2*c-k+2);
		return max(relai, relaj);
	}
}

string solve(const vvi& data)
{
	int k = sz(data);
	vvi dist(3*k, vi(3*k));
	loop(i, 3*k) loop(j, 3*k)
		dist[i][j] = checksymmetry(data, i-k, j-k);
	vvi halfdist(3*k, vi(3*k));
	loop(i, 3*k) loop(j, 3*k)
		halfdist[i][j] = halfchecksymmetry(data, i-k, j-k);
	int minincrease = INT_MAX;
	loop(i, 3*k) loop(j, 3*k)
	{
		if(dist[i][j]!=-1 && dist[i][j]<minincrease)
			minincrease = dist[i][j];
		if(halfdist[i][j]!=-1 && halfdist[i][j]<minincrease)
			minincrease = halfdist[i][j];
	}
	int result = (minincrease+k)*(minincrease+k) - k*k;
	char answer[11];
	sprintf(answer, "%d", result);
	return answer;
}

void preprocess(){}

void readinput(vvi& data)
{
	int k;
	cin>>k;
	data.resize(k, vi(k));
	loop(i, 2*k-1)
	{
		if(i < k)
			loop(j, i+1)
				cin>>data[i-j][j];
		else
			for(int j=i-k+1; j<k; j++)
				cin>>data[i-j][j];
	}
}

vs getoutput()
{
	vvi data;
	readinput(data);
	string answer = solve(data);
	return vs(1, answer);
}

void main()
{
	FILE *p, *q;
//	p=freopen("in.txt", "r", stdin); q=freopen("out.txt", "w", stdout);
//	p=freopen("test\\A-small-attempt0.in", "r", stdin);q=freopen("test\\A-small-attempt0.out", "w", stdout);
	p=freopen("test\\A-large.in", "r", stdin);q=freopen("test\\A-large.out", "w", stdout);
	int testcase;
	cin>>testcase;
	preprocess();
	for (int i=1; i<=testcase; i++)
	{
		cout<<"Case #"<<i<<": ";
		vs answer = getoutput();
		loop(j, sz(answer))
			cout<<answer[j]<<endl;
		fflush(stdout);
	}
	fclose(p);
	fclose(q);
}