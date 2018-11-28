#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
	int n,p,q,x,min,tot,ind;
	int galera[200];
	vector<int> pris;
	cin>> n;
	for(int y=1;y<=n;y++){
		cin >> p >> q;
		pris.clear();
		for(int h=0;h<q;h++){
			cin >> x;
			pris.push_back(x);
		}
		sort(pris.begin(),pris.end());
		min = -1;
		do{
			tot = 0;
			
			for(int i=0;i<p;i++)galera[i]=1;

			for(int i=0;i<q;i++){
				galera[pris[i]-1] = 0;
				ind = pris[i]-1;
				if(ind>0)ind--;
				while(ind>=0 && galera[ind]==1){
					tot++;
					ind--;
				}
				ind = pris[i]-1;
				if(ind<p-1)ind++;
				while(ind<p && galera[ind]==1){
					tot++;
					ind++;
				}
			}

			if(min<0 || tot<min)
				min = tot;
		}while(next_permutation(pris.begin(),pris.end()));
		cout<< "Case #"<<y<<": "<<min<<endl;
	}
}
