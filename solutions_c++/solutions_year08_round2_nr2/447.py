#include <iostream>
#include <cmath>
#include <cstdio>
#include <sstream>
#include <queue>
#include <vector>
#include <string>
#include <cstdlib>
#include <map>
#include <fstream>
#include <set>
#include <cctype>
#include <stack>
#include <deque>

using namespace std;

#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)  //traverse por iterador
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define fo(i,n) for(int i=0;i<n;i++) 
#define foc(i,n) for(int i=0;i<n.size();i++)       //para vector
#define present(container, element) (container.find(element) != container.end())           //para set map
#define cpresent(container, element) (find(all(container),element) != container.end())     //para vector y similares
#define sz(a) int((a).size()) 
#define pb push_back 

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi>  vvi; 
typedef  pair<int,int> ii; 
typedef vector<string>  vs;
#define scan(in,s) fscanf(in,"%d",&(s))
vector<bool> p(1001,true);
	int C,A,P,B;


vector<int> visited;
vector<vector<int> > g;
vector<int> nums;

vector<vector<int> > factores(10001);

bool comparten(int a,int b){
	for(int i=0;i<factores[a].size();i++){
		for(int j=0;j<factores[b].size();j++){
			if(factores[a][i]>=P&&factores[b][j]>=P&&factores[a][i]==factores[b][j]) return true;
		}
	}
	return false;
}


void dfs(int i){
	if(visited[i]==0){
		visited[i]=1;
		for(int j=0;j<nums.size();j++){
				if(g[i][j]==1) dfs(j);
			}
	}
}

vector<int> factor(int n){
	vector<int> v;
	for(int i=2;i<=(int)ceil(double(n)/2.0);i++)
	{	
		if(p[i]==true&&n%i==0)
			v.push_back(i);
	}
	if(p[n]==true) v.push_back(n);
	return v;
}

int main(){
	p[1]=false;
	
	for(int i=2;i<=1000;i++){
		if(p[i]==false) continue;
		for(int j=i*2;j<=1000;j+=i){
			p[j]=false;
		}
	}

	for(int i=2;i<=1000;i++){
		factores[i]=factor(i);
	}

	FILE *in=fopen("C://B-small-attempt2.in","r");
	FILE *out=fopen("C://B.out.txt","w");


	scan(in,C);
	for(int h=1;h<=C;h++){

		scan(in,A);scan(in,B);scan(in,P);

		
		nums=vector<int>();
		for(int i=A;i<=B;i++) nums.push_back(i);
		g=vector<vector<int> > (nums.size(),vector<int>(nums.size(),0));
		for(int i=0;i<nums.size();i++){
			for(int j=i+1;j<nums.size();j++){
				if(comparten(nums[i],nums[j])) g[i][j]=g[j][i]=1;
			}
		}

		int conta=0;
		visited=vector<int>(nums.size(),0);
		for(int i=0;i<nums.size();i++){
			if(visited[i]==1) continue;
			visited[i]=1;
			for(int j=0;j<nums.size();j++){
				if(g[i][j]==1) dfs(j);
			}
			conta++;
		}

		fprintf(out,"Case #%d: %d\n",h,conta);
		cout<<h<<endl;
	}


	fclose(out);
	return 0;
}

