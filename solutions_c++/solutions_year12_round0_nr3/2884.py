#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;
int mat[1000][1000];

int main()
{
	int i, j, k;
	for(i = 0; i<1000; i++){
		for(j = 0; j<1000; j++){
			mat[i][j] = -1;
		}
	}
	
	int T;
	cin>>T;
	for(i = 0; i<T; i++){
		int A, B;
		cin>>A>>B;
		int y = 0;
		for(j = A; j<=B; j++){
			for(k = j+1; k<=B; k++){
				if(mat[j][k] == 1) y++;
				else if(mat[j][k] == -1){
					char s1[5], s2[5];
					sprintf(s1, "%d", j);
					sprintf(s2, "%d", k);
					int s1length = strlen(s1);
					int s2length = strlen(s2);
					int startInd = 0, m, n, possible = 0;
					while(startInd < s1length){
						for( ; startInd<s1length; startInd++){
							if(s1[startInd] == s2[0]){
								possible = 1;
								break;
							}
						}
						m = (startInd+1)%s1length;
						n = 1;
						while(possible && n<s2length){
							if(s1[m] == s2[n]){
								n++;
								m = (m+1)%s1length;
							}
							else possible = 0;
						}
						if(possible){
							mat[j][k] = 1;
							y++;
							break;
						}
						mat[j][k] = 0;
						startInd++;
					}
				}
			}
		}
		cout<<"Case #"<<(i+1)<<": "<<y<<endl;
	}
}