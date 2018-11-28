#include <iostream>
#include <vector>
#include <stack>
#include <iomanip>
#include <cstring>
#include <string>
#include <set>
#include <cmath>
#include <stdio.h>
using namespace std;

int main(){
	freopen("test.txt","r",stdin);
	freopen("test1.txt","w",stdout);
	int tc, time, surp, p, n;
	int q, r, sum,k=1;

	cin >> tc; 
	while(tc--){
		cin >> time >> surp >> p;
		sum = 0;
		while(time--){
			cin >> n;
			q = n/3;
			r = n%3;

			if(r==0){
				if(q>=p)
					sum++;
				else if(surp>0 && q>=1){
					if(q+1>=p){
						sum++;
						surp--;
					}
				}
			}
			else if(r==1){
				if(q+1>=p)
					sum++;
			}
			else{
				if(q+1>=p)
					sum++;
				else if(q+2>=p && surp>0){
					sum++;
					surp--;
				}
			}
		}
		cout<<"Case #"<<k++<<": "<<sum<<"\n";
	}

}