#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>

using namespace std;

int C, D, N;
string opposeds[28];
int opposedscheck[28][2];


//return 1 to clear list
//return 0 if list alright;
int check(char a){
    for (int d = 0; d<D; d++) {
        if(a == opposeds[d][0]) {
            if(opposedscheck[d][1]>0){
                for(int i1 = 0; i1<28; i1++) {
                    opposedscheck[i1][0]=0;
                    opposedscheck[i1][1]=0;
                }
                return 1;
            }else{
               opposedscheck[d][0]++;
            }
        }
        if(a == opposeds[d][1]) {
            if(opposedscheck[d][0]>0){
                for(int i1 = 0; i1<28; i1++) {
                    opposedscheck[i1][0]=0;
                    opposedscheck[i1][1]=0;
                }
                return 1;
            }else{
               opposedscheck[d][1]++;
            }
        }
    }
    return 0;
}

void uncheck(char a){
    for (int d = 0; d<D; d++) {
        if(a == opposeds[d][0]) {
               opposedscheck[d][0]--;
        }
        if(a == opposeds[d][1]) {
               opposedscheck[d][1]--;
        }
    }
}

int main(){
	freopen("B-large.in","rt", stdin);
	freopen("B-large.out","wt",stdout);
	int T;
	cin>>T;

	string pairs[36];

    string input;
    
	for(int t = 0; t<T; t++){
        memset( opposedscheck, 0, 28*2 );
        int outlen = 0;
		printf("Case #%d: ", t+1);
		cin>>C;
        for(int c = 0; c<C; c++) {
            cin>>pairs[c];
        }
        cin>>D;
        for(int d = 0; d<D; d++) {
            cin>>opposeds[d];
        }
        cin>>N;
        cin>>input;
        string output="";
        if(N>0) {
            char m1, m2;
            m1 = input[0];
            output = output + m1;
            outlen++;
            check(m1);
            for(int n=1;n<N;n++) {
                bool ispair = false;
                m2 = input[n];
                for(int c = 0; c<C; c++) {
                    if((pairs[c][0]==m1 && pairs[c][1]==m2) || (pairs[c][0]==m2 && pairs[c][1]==m1)) {
                        uncheck(m1);
                        string::iterator it = output.end() - 1;
                        output.erase(it);
                        ispair = true;
                        output = output + pairs[c][2];
                        m1 = ' ';
                        if(check(pairs[c][2])) {
                            output = "";
                            outlen = 0;
                            m1 = ' ';
                        }
                        break;
                    }
                }
                if(!ispair) {
                    output = output + m2;
                    outlen++;
                    m1 = m2;
                    if(check(m2)) {
                        output = "";
                        outlen = 0;
                        m1 = ' ';
                    }                    
                }
            }            
        }

        cout<<"[";
        for(int i = 0; i<outlen; i++) {
            cout<<output[i];
            if(i!=outlen-1) {
                cout<<", ";
            }
        }

        cout<<"]";

		cout<<"\n";
	}
	return 0;
}