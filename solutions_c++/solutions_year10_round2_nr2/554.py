#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
using namespace std;

#define ulli unsigned long long int
#define lli long long int

#define f(i,n) for(ulli i = 0; i < n; i++)


int main(){
	int ntc = 0;
	cin>>ntc;
	
	f(tc,ntc){
		ulli n, k,b,t;
		cin>>n>>k>>b>>t;
		ulli pos[n];
		ulli v[n];
		ulli count = 0;
		ulli swap = 0;
		ulli reach = 0;
		f(i,n){
			cin >>pos[i];
		} 
		f(i,n){
			cin>>v[i];
		}
		//cout<<"here1"<<endl;
		for(lli i=n-1;i>=0;i--){
			if(((double)(b-pos[i]))/v[i] <= (double)t){
				//cout<<"reaches"<<endl;
				reach++;
				swap+= count;
				if(reach ==k)
					break;
			}else{
				//cout<<"count++"<<endl;
				count++;
			}
		}
		cout << "Case #"<<tc+1<<": ";
		if(reach < k){
			cout <<"IMPOSSIBLE"<<endl;
		}else{
			cout<<swap<<endl;
		}

	}
	return 0;
}
