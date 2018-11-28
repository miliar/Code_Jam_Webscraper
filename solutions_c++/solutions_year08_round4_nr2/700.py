#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstdlib>
using namespace std;
#define Rep(i, a, b) for(i = (a); i <= (b); i++)
int main(){
	long long y1, x2,y2,x3,y3, n, m ,a;
	int c;
	cin >> c;
	for(int i = 1; i <= c; i++){
		cin >> n >> m >> a;
		cout<<"Case #"<<i<<": ";
		bool ans = false;
		/*
		Rep(y1, 0, m){
			Rep(x2, 0, n){
				Rep(y2, 0, m){
					Rep(x3, 0, n){
						Rep(y3, 0, m){
							if(x2*y3-x3*y2 + x3*y1-x2*y1 == a){
								ans = true; break;
							}
						}
						if(ans)
							break;
					}
					if(ans)
						break;
				}
				if(ans)
					break;
			}
			if(ans)
				break;
		}
		*/
		Rep(y1, 0, m){
			Rep(x2, 0, n){
				Rep(y2, 0, m){
					Rep(x3, 0, n){
						if(x2*m-x3*y2 + x3*y1-x2*y1 == a){
							ans = true; y3 = m; break;
						}
					}
					if(ans)
						break;
				}
				if(ans)
					break;
			}
			if(ans)
				break;
		}
		if(!ans){
			Rep(y1, 0, m){
				Rep(x2, 0, n){
					Rep(y3, 0, m){
						Rep(x3, 0, n){
							if(x2*y3 + x3*y1-x2*y1 == a){
								ans = true; y2 = 0; break;
							}
						}
						if(ans)
							break;
					}
					if(ans)
						break;
				}
				if(ans)
					break;
			}
		}
		if(ans){
			cout<<0<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<x3<<" "<<y3<<endl;
		}
		else
			cout<<"IMPOSSIBLE\n";
	}
	return 0;
}
