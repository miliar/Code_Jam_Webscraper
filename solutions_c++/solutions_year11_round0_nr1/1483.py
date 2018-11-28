#include<cstdio>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
using namespace std;

vector<int> O;
vector<int> B;
vector<int> check;
vector<pair<int, int> > tab;

int x[10000010][2];

int t,temp,n;
char znak;
int main(){
	scanf("%d", &t);
	for(int i = 0; i < t; i++){
		scanf("%d",&n);
		for(int j = 0; j < n; j++){
			scanf(" %c %d", &znak, &temp);
			if(znak=='O'){
				tab.push_back(make_pair(temp,0));
				O.push_back(temp);
				check.push_back(1);
			}
			else{
				tab.push_back(make_pair(temp,1));
				B.push_back(temp);
				check.push_back(0);
			}
		}
		bool pop = false;
		int czas = 0;
		if(tab[0].second == 0)pop=true;
		else pop = false;
		int b_act, o_act;
		b_act = o_act = 1;
		int orange = 0, blue = 0;
		int o_wait = 0, b_wait = 0;
		for(int j = 0; j < tab.size(); j++){
			if(tab[j].second == 0){ // orange
				o_wait = abs(tab[j].first-o_act) - blue;
				if(o_wait <= 0)o_wait = 0;
				//printf("Mam orange i o.wait = %d, blue = %d\n", o_wait, blue);
				blue = 0;
				czas += o_wait +1;
				orange = orange + o_wait + 1;
				o_act = tab[j].first;
				//printf("Czas = %d orange = %d\n", czas, orange);
			}else{
				b_wait = abs(tab[j].first-b_act) - orange;
				if(b_wait <= 0)b_wait = 0;
				//printf("Mam blue i b.wait = %d, orange = %d\n", b_wait, orange);
				orange = 0;
				b_act = tab[j].first;
				czas += b_wait + 1;
				blue = blue + b_wait + 1;
			}
		}
		tab.clear();
		printf("Case #%d: %d\n", i+1,czas);
	}
	return 0;
}
