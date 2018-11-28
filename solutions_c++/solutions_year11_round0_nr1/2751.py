#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <cmath>
#include <deque>
#include <stack>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <ctime>

using namespace std;

#define maxn 110
#define datat int
#define ansdatat int

int n;

struct tpo
{
	char c;
	int p;
};

tpo seq[maxn], blue[maxn], ora[maxn];

string s;

void init_deal(){
}

void up_ps(int &from, int to, int ti){
	int left_t = abs(to-from);
	if(left_t<=ti){
		from = to;
	}
	else{
		if(to>from){
			from = to-(left_t-ti);
		}
		else{
			from = to+(left_t-ti);
		}
	}
}

int main(){
	
	int tttt;
	scanf("%d", &tttt);
	getline(cin,s);
	for(int ttt = 1;ttt<=tttt;ttt++){
		int ans = 0;

		getline(cin,s);
//		cout<<s<<endl;
		stringstream ss(s);
		int nn;
		ss>>nn;
//		cout<<nn<<endl;
		char col;
		int ps;
		int t_b = 0, t_o = 0, tot = 0;
		for(int i = 1;i<=nn;i++){
			ss>>col>>ps;
			//cout<<col<<" "<<ps<<endl;
			tot++;
			seq[tot].c = col;
			seq[tot].p = ps;
			//cout<<seq[tot].c<<" "<<seq[tot].p<<endl;

			if(col == 'B'){
				t_b++;
				blue[t_b].c = col;
				blue[t_b].p = ps;
			}
			else{
				t_o++;
				ora[t_o].c = col;
				ora[t_o].p = ps;
			}
		}

		int b_ps = 1, o_ps = 1,
			b_top = 1, o_top = 1;
		
		for(int i = 1;i<=tot;i++){
			int ti = 0;
			if(seq[i].c == 'B'){
				ti = abs(blue[b_top].p-b_ps)+1;
				up_ps(o_ps,ora[o_top].p,ti);
				b_ps = blue[b_top].p;
				b_top++;
			}
			else{
				ti = abs(ora[o_top].p-o_ps)+1;
				up_ps(b_ps,blue[b_top].p,ti);
				o_ps = ora[o_top].p;
				o_top++;
			}
			//printf("b_ps = %d, o_ps = %d, %d\n", b_ps, o_ps, ti);
			ans+=ti;
			
		}



		printf("Case #%d: ",ttt);
		printf("%d\n", ans);


	}

	

	return 0;
};

