/*
LANG: C++
TASK: candy
*/

#include <stdio.h>
#include <iostream>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <queue>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <iomanip>

using namespace std;

int T,N;
int bag[1001];

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
    cin>>T;
    for(int i=1; i<=T; i++){
        cin>>N;
        int temp=0;
        for(int j=0; j<N; j++){
            cin>>bag[j];
            temp^=bag[j];
        }
        if(temp!=0){
            cout<<"Case #"<<i<<": NO"<<endl;
            continue;
        }
        int maxpile=0;
        for(int j=1; j<(1<<N)-1; j++){
            int seanxor=0,seansum=0,patrickxor=0,patricksum=0;
            for(int k=0; k<N; k++){
                if(j&(1<<k)){
                    seanxor^=bag[k];
                    seansum+=bag[k];
                }
                else{
                    patrickxor^=bag[k];
                    patricksum+=bag[k];
                }
            }
            if(patrickxor==seanxor) maxpile=max(maxpile,seansum);
        }
        cout<<"Case #"<<i<<": "<<maxpile<<endl;
    }
	return 0;
}
