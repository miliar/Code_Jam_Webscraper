#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

const int mx = 2000;

int maxs[mx]={0};
int maxns[mx]={0};

ifstream cin("B-Large.in");
ofstream cout("B-small-attempt0.out");
int main(){
	for(int i=0;i<mx;i++) {
		maxs[i] = -1;
		maxns[i] = -1;
	}
	for(int i=0;i<=10;i++)
		for(int j=0;j<=10;j++)
			for(int k=0;k<=31;k++)
				if(abs(i-j)<=2 && abs(i-k)<=2 && abs(j-k)<=2){
					int z = i+j+k;
					int y = max(i,max(j,k));
					if(abs(i-j)==2 || (abs(i-k)==2) || abs(j-k)==2)
						maxs[z]= max(maxs[z],y);
					else
						maxns[z] = max(maxns[z],y);

				}

	int T;
	cin >> T;
	for(int i=0;i<T;i++){
		int N,S,p;
		cin >> N >> S >> p;
		int ret =0;
		for(int j=0;j<N;j++){			
			int val;
			cin >> val;
			if(maxns[val]>=p){
				ret++;
			}
			else if(maxs[val]>=p && S>0){
				ret++;
				S--;
			}
		}
		cout << "Case #" << i+1 << ": " << ret << endl;

	}
	system("pause");
	return 0;
};