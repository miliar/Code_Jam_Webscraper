#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main(){
	freopen("A-large.in","rt", stdin);
	freopen("A-large.out","wt",stdout);
	int T;
	cin>>T;
    int N;
	char P[1000];
    int R[1000];
	for(int t = 0; t<T; t++){
		printf("Case #%d: ", t+1);
		cin>>N;
        int posO = 1;
        int posB = 1;
        int time = 0;
        for(int n =0; n<N; n++) {
            cin>>P[n]>>R[n];
        }
        for(int n =0; n<N; n++) {
            //cout<<P[n]<<" "<<R[n]<<" ";
            int dist = 0;
            int absdist = 0;
            if(P[n]=='O') {
                if(R[n]==posO) {
                    time++;
                    absdist = 1;
                }else{
                    
                    absdist = abs(R[n] - posO) + 1; 
                    time += absdist;
                    posO = R[n];
                }
                int n2 = n + 1;
                while (P[n2]!='B') {
                    n2++;
                }
                if(R[n2]!=posB) {
                    int dist2 = R[n2] - posB;
                    if(absdist <= abs(dist2)) {
                        if(dist2 < 0) {
                            posB -= absdist;
                        }else{
                            posB += absdist;
                        }
                    }else{
                        posB += dist2;
                    }
                }
            }else{
                if(R[n]==posB) {
                    time++;
                    absdist = 1;
                }else{
                    
                    absdist = abs(R[n] - posB) + 1; 
                    time += absdist;
                    posB = R[n];
                }
                int n2 = n + 1;
                while (P[n2]!='O') {
                    n2++;
                }
                if(R[n2]!=posO) {
                    int dist2 = R[n2] - posO;
                    if(absdist <= abs(dist2)) {
                        if(dist2 < 0) {
                            posO -= absdist;
                        }else{
                            posO += absdist;
                        }
                    }else{
                        posO += dist2;
                    }
                }
            }
        }			
		cout<<time<<"\n";
	}
	return 0;
}