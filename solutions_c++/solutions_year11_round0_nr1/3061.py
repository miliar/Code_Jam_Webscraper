#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
	freopen("A-large.out","w",stdout);
	int t,n,i,j,a;
	char c;
	cin >> t;
	for(j = 1; j<=t; j++){
		cin >> n;
		int res = 0,res1=0,res2=0,pos1=1,pos2=1;
		bool pos = true;
		for(i = 1; i<=n; i++){
			cin >> c;
			cin >> a;
			if(c == 'O'){
				if(pos == false){
					res1 += abs(a-pos1)+1;
					res += abs(a-pos1)+1;
				}
				else{
					res1 = abs(a-pos1)+1;
					if(res1>res2){
						res+= res1-res2;
						res1-=res2;
					}
					else{
						res++;
						res1=1;
					}
				}
				pos1 = a;
				pos = false;
			}
			if(c == 'B'){
				if(pos == true)
				{
					res2 += abs(a-pos2)+1;
					res += abs(a-pos2)+1;
				}
				else
				{
					res2 = abs(a-pos2)+1;
					if(res2>res1){
						res+= res2-res1;
						res2-=res1;
					}
					else{
						res++;
						res2=1;
					}
			}
			pos2 = a;
			pos = true;
			}
		}
		cout << "Case #" << j << ": " << res << endl;
	}
	return 0;
}