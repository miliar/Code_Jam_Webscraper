/*
 * snapper.cpp
 *
 *  Created on: May 7, 2010
 *      Author: sainath
 */

#include <iostream>
#include <fstream>
#include <cmath>
#include <string.h>

using namespace std;

int main(){

	ifstream fp("A-large.in", ios::in);

	int T;

	fp>>T;

	int count = 1;

/*
	while(T>0){

		int N,K;

		fp>>N>>K;

		int *snappers = new int[N+1];
		memset(snappers, 0, (N+1)*sizeof(int));

		snappers[0] = 1;

		int *snappers_new = new int[N+1];
		memcpy(snappers_new, snappers, (N+1)*sizeof(int));

		for(int i=0; i<K; i++){
			for(int j=1; j<=N; j++){
				int flag = 1;
				for(int k=j-1; k>0; k--){
					if(snappers[k]==0)
						flag =0;
				}
				if(flag)
					snappers_new[j] = snappers[j]^1;
			}
			memcpy(snappers, snappers_new, (N+1)*sizeof(int));
		}

		int flag=1;
		for(int k=N; k>0; k--)
			if(snappers[k]==0)
				flag = 0;


		if(flag)
			cout<<"Case #"<<count<<": ON\n";
		else
			cout<<"Case #"<<count<<": OFF\n";

		count++;
		T--;
	}

*/
	while(T>0){

		int N,K;

		fp>>N>>K;

		int flag = 1;
		for(int i=1; i<=N; i++){
			unsigned int pow2 = (unsigned int) pow(2,i);
			if(K%pow2 < pow2/2){
				flag = 0;
				break;
			}
		}

		if(flag)
			cout<<"Case #"<<count<<": ON\n";
		else
			cout<<"Case #"<<count<<": OFF\n";

		count++;
		T--;

	}

	return 0;

}
