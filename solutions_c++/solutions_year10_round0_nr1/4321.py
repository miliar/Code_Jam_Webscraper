#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <cstring>
#include <bitset>

using namespace std;

int main(){
    int T, N, K;
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    scanf("%d",&T);	
    bitset<30> snapchain;
    bitset<30> status;
    for(int i=0;i< T;i++){
	snapchain.reset();
	status.reset();
	scanf("%d%d",&N,&K);
	for(int j=0;j <K;j++){
	    status.set(0);
	    for(int l=0;l<N;l++){
		if(status.test(l))
		    snapchain.flip(l);
	    }
	    if(!snapchain.test(0)){
		status.reset();
	    }
	    else {
		int count=0;
		for(int l=1;l<N;l++){
		    if(count==l-1)
			status.set(l);
		    if(snapchain.test(l))
			count++;
		}
	    }
	}
	int count=0;
	for(int j=0;j<N;j++){
	    if(snapchain.test(j))
		count++;
	}
	if(count==N){
	    cout<<"Case #"<<i+1<<": ON"<<endl;
	}
	else
	    cout<<"Case #"<< i+1<<": OFF"<<endl;
    }
}
