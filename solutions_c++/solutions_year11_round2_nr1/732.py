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

char ch[10000];

string s[maxn];

double tot[maxn], win[maxn], lose[maxn], 
		wp[maxn], owp[maxn], oowp[maxn];

void init_deal(){
}

int main(){
	
	int tttt;
	scanf("%d", &tttt);
	for(int ttt = 1;ttt<=tttt;ttt++){
		printf("Case #%d:\n",ttt);
		scanf("%d", &n);
		for(int i = 1;i<=n;i++){
			scanf("%s", ch);
			s[i] = ch;
			s[i] = ' '+s[i];
			tot[i] = 0;
			win[i] = 0;
			lose[i] = 0;
		}

		for(int i = 1;i<=n;i++){

			for(int j = 1;j<=n;j++){
				//cout<<s[i][j]<<" ";
				if(s[i][j] == '1'){
					tot[i]++;
					win[i]++;
				}
				else
				if(s[i][j] == '0'){
					tot[i]++;
					lose[j]++;
				}
			}

			//cout<<endl;
			//cout<<s[i]<<" "<<win[i]<<" "<<tot[i]<<endl;
			wp[i] = win[i]/tot[i];
		}

		for(int i = 1;i<=n;i++){
			double sum = 0;

			for(int j = 1;j<=n;j++)
			if(s[i][j] == '1'){
				sum+=win[j]/(tot[j]-1);//wp[j];
			}
			else
			if(s[i][j] == '0'){
				sum+=(win[j]-1)/(tot[j]-1);
			}
			//cout<<"owp "<<sum<<" "<<tot[i]<<" "<<owp[i]<<endl;
			owp[i] = sum/tot[i];
		}

		for(int i = 1;i<=n;i++){
			double sum = 0;

			for(int j = 1;j<=n;j++)
			if(s[i][j] == '1'){
				sum+=owp[j];
			}
			else
			if(s[i][j] == '0'){
				sum+=owp[j];
			}
			oowp[i] = sum/tot[i];
		}

		for(int i = 1;i<=n;i++){
			double ans = 0.25*wp[i]+
						 0.50*owp[i]+
						 0.25*oowp[i];
			//cout<<wp[i]<<" "<<owp[i]<<" "<<oowp[i]<<" ";
			cout<<ans<<endl;
		}




	}
	

	return 0;
};

