#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

const double EPS = 1e-10;
const double PI = 3.14159265358979323846264338328;

#define PB push_back
#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define INF INT_MAX
#define MSG(a) cout << #a << " = " << a << endl;
#define SORT(a) sort(a.begin(),a.end())

struct node
{
	int name;
	int leftDesc;
	int rightDesc;
	bool changeable;
	bool type;	
	int val;
	bool leaf;
};


long long dp[10005][2]; //#changes needed to make a node 0, #changes needed to make it 1

vector<node> vec;


int bitCnt(int mask) 
{
  return (mask==0 ? 0 : bitCnt(mask & (mask - 1)) + 1);
}



int rec(int curr, int desired)
{
	if(dp[curr][desired] != INF)
		return dp[curr][desired];


	
	if(vec[curr].leaf == 1)
	{
		if(vec[curr].val != desired)
		{
			dp[curr][desired] = 9999999;
			return 9999999;
		}
		else
		{
			dp[curr][desired] = 0;
			return 0;
		}
	}
	
//	cout << curr << " " << vec[curr].leaf << " " << vec[curr].type << endl;
	
	if(desired == 1 && vec[curr].type == 1)
	{
		dp[curr][desired] <?= rec(vec[curr].leftDesc, 1) + rec(vec[curr].rightDesc, 1);
		if(vec[curr].changeable == 1)
			dp[curr][desired] <?= 1 + min(rec(vec[curr].leftDesc,1), rec(vec[curr].rightDesc,1));
//		fout << dp[curr][desired] << " 1 " << endl;
//		return dp[curr][desired];
	}
	else if(desired == 1 && vec[curr].type == 0)
	{
		dp[curr][desired] <?= min(rec(vec[curr].leftDesc,1), rec(vec[curr].rightDesc,1));
		if(vec[curr].changeable == 1)
		dp[curr][desired] <?= 1 + rec(vec[curr].leftDesc, 1) + rec(vec[curr].rightDesc, 1);
//		cout << dp[curr][desired] << " 2 " << endl;
	//	return dp[curr][desired];
	}
	else if(desired == 0 && vec[curr].type == 1)
	{
		dp[curr][desired] <?= min(rec(vec[curr].leftDesc,0), rec(vec[curr].rightDesc,0));
		if(vec[curr].changeable == 1)
			dp[curr][desired] <?= 1 + rec(vec[curr].leftDesc,0) + rec(vec[curr].rightDesc,0);
//		cout << dp[curr][desired] << " 3 " << endl;
//		return dp[curr][desired];
	}
	else
	{
		dp[curr][desired] <?= rec(vec[curr].leftDesc,0) + rec(vec[curr].rightDesc,0);
		if(vec[curr].changeable == 1)
		dp[curr][desired] <?= 1 + min(rec(vec[curr].leftDesc,0), rec(vec[curr].rightDesc,0));		
//		cout << dp[curr][desired] << " 4 " << endl;
	
	}
//	cout << curr << " " << desired << " " << vec[curr].leftDesc << " " << vec[curr].rightDesc << " " << dp[curr][desired] << endl;
	
	return dp[curr][desired];
}

int main()
{
   ofstream fout;
   fout.open("outputAlarge.txt");
   ifstream fin("A-large.in");
    
   int N;
   fin >> N;
   
   FOR(k,1,N+1)
   {
		FOR(t,0,10005)
		FOR(u,0,2)
			dp[t][u] = INF;
		
		int M,V;
		fin >> M >> V;  //V is desired value of root, M is #nodes

		vec.clear();
		
		FOR(t,0,(M-1)/2)
		{
			node newNode;
			newNode.name = t;			
			int G,C;
			fin >> G >> C;
			newNode.type = G;  //G = 1 means OR
			newNode.changeable = C; //C = 1 means changeable
			newNode.leftDesc = 2*(t+1)-1;
			newNode.rightDesc = 2*(t+1);
			newNode.val = -1;
			newNode.leaf = 0;
			vec.PB(newNode);
		}
		
		FOR(t,(M-1)/2, M)
		{
			node newNode;
			int tmp;
			fin >> tmp;
			newNode.leaf = 1;
			newNode.val = tmp;
			vec.PB(newNode);
		}

		int TMP = rec(0,V);
		cout << TMP << endl;
	

		if(dp[0][V] > 999999)
			fout << "Case #" << k << ": IMPOSSIBLE" << endl;
		else fout << "Case #" << k << ": " << dp[0][V] << endl;
		
	}

  
   return 0; 
    
    
    
    
    
    
}

