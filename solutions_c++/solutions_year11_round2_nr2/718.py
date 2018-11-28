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

#define maxn 210
#define datat int
#define ansdatat int

struct tpo
{
	int p,v;
};

bool cmp(const tpo &a, const tpo &b){
	return a.p<b.p;
};

tpo po[maxn];

int n, d, p[maxn], v[maxn], nv[maxn];

void init_deal(){
}

int main(){
	
	int tttt;
	scanf("%d", &tttt);
	for(int ttt = 1;ttt<=tttt;ttt++){
		printf("Case #%d: ",ttt);
		cin>>n>>d;

		for(int i = 1;i<=n;i++){
			cin>>po[i].p>>po[i].v;
		}

		sort(po+1,po+1+n,cmp);

		/*
		for(int i = 1;i<=n;i++){
			cout<<po[i].p<<" "<<po[i].v<<endl;
		}
		*/



		double ll, rr, mid;
		ll = 0;rr = 1e10;
		for(int i = 1;i<=300;i++){
			bool no = false;
			mid = (ll+rr)*0.5;
//			cout<<"mid =   "<<mid<<endl;
			double left = po[1].p-mid;

			for(int j = 1;j<=n;j++){
				nv[j] = po[j].v;
			}
			nv[1]--;

			
			for(int j = 1;j<=n;j++){

				for(int k = 1;k<=nv[j];k++){
//					cout<<left<<endl;
					double nleft = left+d;
					double gl = po[j].p-mid,
						   gr = po[j].p+mid;
					if(gr<nleft){
						no = true;
						break;
					}
					else{
						left = max(nleft,gl);
					}

				}
				if(no)break;
			}
//			cout<<"res =   "<<no<<endl;

			if(no){
				ll = mid;
			}
			else{
				rr = mid;
			}


		}

		cout<<ll<<endl;



	}
	

	return 0;
};

