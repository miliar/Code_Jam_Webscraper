#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
//#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;


ifstream cin("A-Large.in");
ofstream cout("A-Large.out");

int main(){
	int T;
	cin >> T;
	for(int i=0;i<T;i++){
		int N;
		cin >> N;
		vector <long long> vdi;
		vector <long long> vli;
		vdi.push_back(0);
		vli.push_back(0);
		for(int j=0;j<N;j++){
			long long di,li;
			cin >> di >> li;
			vdi.push_back(di);
			vli.push_back(li);		
		}
		long long D;
		cin >> D;
		vdi.push_back(D);
		vli.push_back(0);
		vector <long long> vlb;
		vlb.assign(vli.size(),0);
		vlb[1]=vdi[1];
		queue<int> Q;
		Q.push(1);
		bool ret = false;
		while(!Q.empty()){
			int u = Q.front();
			Q.pop();
			for(int k=u+1;k<vdi.size();k++){
				//don't forget the one offset
				if(vlb[u]>=(vdi[k]-vdi[u])){
					if(k==vdi.size()-1){
						ret = true;
						break;
					}
					long long temp = min(vdi[k]-vdi[u],vli[k]);
					if(vlb[k]<temp){
						Q.push(k);
						vlb[k]=temp;						
					}
				}
			}
			if(ret) break;
		}
		if(ret) cout << "Case #" << i+1 << ": YES" << endl;
		else cout << "Case #" << i+1 << ": NO" << endl;
	}
	
	return 0;
}