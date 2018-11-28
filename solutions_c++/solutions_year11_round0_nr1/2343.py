#include <stdio.h>
#include <vector>
using namespace std;

vector<pair<int, int> > O,B;
int T,N,C,o,b,t;

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int i,j; char v; int x;

	scanf ("%d",&T); while (T--){
		scanf ("%d ",&N); O.clear(); B.clear();
		for (i=0;i<N;i++){
			scanf ("%c %d ",&v,&x);
			if (v == 'O') O.push_back(make_pair(i,x));
			else B.push_back(make_pair(i,x));
		}
		o = b = 1; t = i = j = 0;
		while (1){
			if (i == O.size() && j == B.size()) break;
			else if (i == O.size()){
				t += abs(b-B[j].second) + 1;
				b = B[j].second; j++;
			}
			else if (j == B.size()){
				t += abs(o-O[i].second) + 1;
				o = O[i].second; i++;
			}
			else{
				int DO = abs(o-O[i].second);
				int DB = abs(b-B[j].second);

				if (O[i].first < B[j].first){
					DO++;
					if (DO >= DB) b = B[j].second;
					else{
						if (b < B[j].second) b += DO;
						else b -= DO;
					}
					o = O[i].second;
					t += DO ; i++;
				}
				else{
					DB++;
					if (DB >= DO) o = O[i].second;
					else{
						if (o < O[i].second) o += DB;
						else o -= DB;
					}
					b = B[j].second;
					t += DB; j++;
				}
			}
		}

		printf ("Case #%d: %d\n",++C,t);
	}

	return 0;
}