#include <iostream>
using namespace std;
int status[35];
int energy[35];
int i,j;
long tests,nSnaps,snaps;
void restart(){
    for(int i=0;i<nSnaps;i++){
    	status[i]=0;
    	energy[i]=0;
    }
    energy[0]=1;
}
void change(int pos){
	status[pos]=status[pos]==1?0:1;
}
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("RESULT_A_small.out","w",stdout);
    cin>>tests;
    for(j=1;j<=tests;j++){
        cin>>nSnaps>>snaps;
        restart();
        while(snaps--){
        	for(i=0;i<nSnaps;i++){
        		if(energy[i]==1){
        			change(i);
        		}
        	}
            for(i=0;i<nSnaps;i++){
            	if(energy[i]==1&&status[i]==1)
            		energy[i+1]=1;
                else
                    energy[i+1]=0;
            }
        }
        if(energy[nSnaps-1]==1&&status[nSnaps-1]==1)
            cout<<"Case #"<<j<<": ON"<<endl;
        else
        	cout<<"Case #"<<j<<": OFF"<<endl;
    }
    return 0;
}
