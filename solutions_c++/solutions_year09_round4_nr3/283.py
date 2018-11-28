/*
  Name: Graph Class
  Copyright: liruqi
  Author: liruqi
  Date: 05-05-08
  Description: a collection for gragh algorithms.
*/

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

template<class T>
void show(T x){ cout<< "# "<< x <<endl; }
template<class T>
void show(T b,T e){ cout<<"$ "; for(T i=b;i!=e;i++) cout<<*i<<", ";cout<<endl; }

#define ni(x) scanf("%d",&x)
#define ns(x) scanf("%s",x)
//#define assert(x) if(!(x)){puts("err"); exit(0)};

/*node size*/
const int node_size=110;
const int inf = 0x0f0f0f0f;
typedef vector<int> VI;
int N, K;
int price[108][32];
void input()
{
	ni(K);
	for(int n=1;n<=N;n++)
	for(int k=1;k<=K;k++)
	ni(price[n][k]);
}

int sgn(int x) {if(x<0) return -1; if(x>0) return 1; return 0;}

bool _less(int s,int t)
{
	for(int k=1;k<=K;++k)
	{
		if(price[s][k] >= price[t][k])return 0;
		
	}
	return 1;
}

/*
in this Graph Class, node are labeled from 1
now I have two methods:
	max match	[OK]
	optimal match	[OK]
*/
struct MatchGraph{
	bool adj[node_size][node_size];
	bool v_left[node_size],v_right[node_size];
	int match[node_size];
	int left_num,right_num;
	int weight[node_size][node_size];
	int l_left[node_size],l_right[node_size];
	void init(){
		memset(adj,0,sizeof(adj));
		
		ni(N);
		left_num=N;
		right_num=N;
		input();
		for(int i=1; i<=left_num; ++i)
		{
			for(int j=1; j<=left_num; ++j) if(i!=j)
			{
				adj[i][j] = _less(i,j);
			}
			
		}
	}
	
	int max_match_dfs(int p){
		int v,t;
		for(v=1;v<=right_num;v++) if(!v_right[v] && adj[p][v]){
			t=match[v];
			v_right[v]=1;
			if(t==0 || max_match_dfs(t)){
				match[v]=p;
				return 1;
			}
		}
		return 0;
	}
	/*
	maximum match
	precodition: 
		weight[][] have been assigned
	*/
	int max_match(){
		int cnt=0;
		memset(match,0,sizeof(match));
		for(int i=1;i<=left_num;i++){
			memset(v_right,0,sizeof(v_right));
			cnt += max_match_dfs(i);
		}
		return cnt;
	}
	
	int min_cover_dfs(int p){
		int v,t;
		v_left[p]=1;
		for(v=1;v<=right_num;v++) if(!v_right[v] && adj[p][v]){
			v_right[v]=1;
			t=match[v];
			if(!v_left[t]){
				min_cover_dfs(t);
			}
		}
	}
	/*
	precondition:
		max match have been found, and matching edge stored in match[]
	postcodition:
		all the visited node are labled with v_left, v_right
		and the min cover node set is all nodes in left which are not labled and in right which are labled
	*/
	void min_cover_nodeset(){
		bool m_left[node_size];
		memset(v_left,0,sizeof(v_left));
		memset(v_right,0,sizeof(v_right));
		memset(m_left,0,sizeof(v_left));
		for(int i=1;i<=right_num;i++)
			if(match[i]){
				m_left[match[i]]=1;

			}
		for(int i=1;i<=left_num;i++)
			if(!m_left[i])//not matched
				min_cover_dfs(i);
		cout<<"left node(s): ";
		for(int i=1;i<=left_num;i++)
			if(!v_left[i])
				cout<<i<<" ";
		cout<<endl;
		cout<<"right node(s): ";
		for(int i=1;i<=right_num;i++)
			if(v_right[i])
				cout<<i<<" ";
		cout<<endl;
	}
	

} g;


int solve(){

	g.init();

	return N - g.max_match();
	//cout<<"max match: ";
	//cout<<g.max_match()<<" matchs"<<endl;
	//g.min_cover_nodeset();
}

int main()
{
    int nks;
	ni(nks);
    
    for(int k=1;k<=nks;k++)
    {
		
		printf("Case #%d: %d\n", k, solve());
	}
}
