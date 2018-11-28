#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

#define ulli unsigned long long int
#define lli long long int

#define f(i,n) for(ulli i = 0; i < n; i++)


int main(){
	int ntc = 0;
	cin>>ntc;
	
	f(tc,ntc){
		ulli n, k;
		cin >> n >> k;
		char pos[n][n];
		char newp[n][n];
		int rnum[n];
		f(i,n){
			rnum[i]=0;
		}
		char row[n];
		char col[n];
		f(i,n){
			f(j,n){
				cin>> pos[i][j];
				newp[i][j]='.';
			}
		}
		f(j,n)
		{
			f(i,n){
				if(pos[n-1-j][n-1-i]=='R'||pos[n-1-j][n-1-i]=='B'){
					newp[j][rnum[j]]=pos[n-1-j][n-1-i];
					rnum[j]++;
				}
			}
		}
		//f(i,n){f(j,n){cout <<newp[i][j];}cout<<endl;}
		//cout <<"done"<<endl;
		int Red = 0; int Blue = 0;
		int count = 0;
		f(i,n){
			count=0;
			f(j,n){
				if(count > 0 && newp[i][j]==newp[i][j-1]){
					count++;
				}
				else if(newp[i][j]== 'R'||newp[i][j]== 'B'){
					count = 1;
				} else{
					count = 0;
				}
				if(count >= k){
					if(newp[i][j]=='R'){
						Red = 1;
					} else if(newp[i][j]=='B'){
						Blue = 1;
					}
				}
			}
		}
		
		f(j,n){
			count=0;
			f(i,n){
				if(count > 0 && newp[i][j]==newp[i-1][j]){
					count++;
				}
				else if(newp[i][j] == 'R'||newp[i][j] == 'B'){
					count = 1;
				} else{
					count = 0;
				}
				if(count >= k){
					if(newp[i][j]=='R'){
						Red = 1;
					} else if(newp[i][j]=='B'){
						Blue = 1;
					}
				}
			}
		}
		f(i,n){
			count = 0;
			f(j,n-i){
				if(count> 0 && newp[i+j][j]==newp[i+j-1][j-1]){
					count++;
				}else if(newp[i+j][j] == 'R'||newp[i+j][j] == 'B'){
					count = 1;
				} else{
					count = 0;
				}
				if(count >= k){
					if(newp[i+j][j]=='R'){
						Red = 1;
					} else if(newp[i+j][j]=='B'){
						Blue = 1;
					}
				}
			}
		}
		f(i,n){
			count = 0;
			f(j,n-i){
				if(count> 0 && newp[j][i+j]==newp[j-1][i+j-1]){
					count++;
				}else if(newp[j][i+j] == 'B'||newp[j][i+j] == 'R'){
					count = 1;
				} else{
					count = 0;
				}
				if(count >= k){
					if(newp[j][i+j]=='R'){
						Red = 1;
					} else if(newp[j][i+j]=='B'){
						Blue = 1;
					}
				}
			}
		}
		/*f(i,n){
			f(j,n-i-1){
				if(count > 0 && newp[n-1-i][n-1-i-j]==newp[n-i][n-i-j]){
					count++;
				}else if(newp[n-1-i][n-1-i-j] == 'B'||newp[n-1-i][n-1-i-j] == 'R'){
					count = 1;
				} else{
					count = 0;
				}
				if(count >= k){
					if(newp[n-1-i][n-1-i-j]=='R'){
						Red = 1;
					} else if(newp[n-1-i][n-1-i-j]=='B'){
						Blue = 1;
					}
				}
			}
		}*/
		for(int sum= 0; sum<n; sum++){
		count = 0;
			for(int c = 0; c < sum+1;c++){
				if(count > 0 && newp[c][sum-c]==newp[c-1][sum-c+1]){
					count++;
				}else if(newp[c][sum-c]=='R'||newp[c][sum-c]=='B'){
					count = 1;
				} else {
					count = 0;
				}
				if(count >= k){
					if(newp[c][sum-c]=='R'){
						Red = 1;
					} else if(newp[c][sum-c]=='B'){
						Blue = 1;
					}
				}
			}
		}
		for(int sum= n; sum<2*n - 1; sum++){
		count = 0;
			for(int c = n-1; c<sum-n-1;c--){
				if(count > 0 && newp[sum-c][c]==newp[sum-c-1][c+1]){
					count++;
				}else if(newp[sum-c][c]=='R'||newp[sum-c][c]=='B'){
					count = 1;
				} else {
					count = 0;
				}
				if(count >= k){
					if(newp[sum-c][c]=='R'){
						Red = 1;
					} else if(newp[sum-c][c]=='B'){
						Blue = 1;
					}
				}
			}
		}  
		
		
		cout << "Case #"<<tc+1<<": ";
		if(Red > 0 && Blue > 0){
			cout << "Both"<<endl;
		} else if(Red > 0){
			cout << "Red"<<endl;
		} else if(Blue > 0){
			cout << "Blue"<<endl;
		} else {
			cout << "Neither"<<endl;
		}
	}
	return 0;
}
