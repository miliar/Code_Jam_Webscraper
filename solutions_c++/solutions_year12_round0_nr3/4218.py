#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>

using namespace std;

int main(){
	int T;
	int i=1;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	cin>>T;
	while(T--){
	int found=0;
	int llimit;
	int ulimit;
	cin>>llimit>>ulimit;
	int temp=llimit;
	int dig=0;
	while(temp>0){
	temp=temp/10;
	dig++;
	}
	for(int k=1;k<dig;k++){
		int istart=int(pow(10,k-1));
		int iend=int(pow(10,k));
		int jstart=int(pow(10,dig-k-1));
		int jend=int(pow(10,dig-k));
		for(int i=istart;i<iend;i++){
			//int iquot=i/istart;
			for(int j=jstart;j<jend;j++){
				//int jquot=j/jstart;

					int out=i*jend + j;
					int outrev=j*iend + i;
					if(outrev>out){
					if(out>=llimit && out<=ulimit && outrev>=llimit && outrev<=ulimit){
						found++;
					}
				}

			}
		}
	}
	cout<<"Case #"<<i++<<": "<<found<<endl;
	}
}
