#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
typedef long long int lli;
typedef long double ld;
#define ZER(X) memset(X,0,sizeof(X));

const int MAX = 500 + 1;
int M[MAX][MAX];

int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);

	int Cases;
	cin >> Cases;
	for(int Case=1; Case <= Cases; ++Case){
		int R, C, D;
		cin >> R >> C >> D;
		for(int i = 0; i<R; ++i){
			string S;
			cin >> S;
			for(int j = 0; j<C; ++j){
				M[i][j] = S[j]-'0';
				//cerr << M[i][j] << " ";
			}
			//cerr << endl;
		}
		int max = 0;

		for(int t = 0; t<R; ++t){
			for(int l = 0; l<C; ++l){
				for(int s=3; t+s<=R && l+s<=C; ++s){
					int half = s/2;
					lli w=0;
					for(int i=0; i<half; ++i){
						for(int j=0; j<s; ++j){
							if(i!=0 || (j!=0 && j!=s-1))
								w+=M[t+i][l+j]*(half-i);
						}
					}
					//cerr << "t " << t << " l " << l << " s " << s << endl;
					/*if(t==1 && l==1 && s==5){
					cerr << "w " << w;
					}*/
					for(int i=0; i<half; ++i){
						for(int j=0; j<s; ++j){
							if(i!=0 || (j!=0 && j!=s-1))
								w-=M[t+s-1-i][l+j]*(half-i);
						}
					}

					if(w)
						continue;

					for(int i=0; i<half; ++i){
						for(int j=0; j<s; ++j){
							if(i!=0 || (j!=0 && j!=s-1))
								w+=M[t+j][l+i]*(half-i);
						}
					}

					for(int i=0; i<half; ++i){
						for(int j=0; j<s; ++j){
							if(i!=0 || (j!=0 && j!=s-1))
								w-=M[t+j][l+s-1-i]*(half-i);
						}
					}

					if(!w){
						if(s>max)
							max = s;
					}
				}
			}
		}
		cout << "Case #" << Case << ": ";
		if(max)
			cout << max << "\n";
		else
			cout << "IMPOSSIBLE\n";
	}
	return 0;
}