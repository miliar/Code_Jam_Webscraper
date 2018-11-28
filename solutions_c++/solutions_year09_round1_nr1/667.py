#include<vector>
#include<iostream>
#include<string>
#include<algorithm>
#include<map>
#include<cstring>
#include<sstream>

using namespace std;

long long tolong(vector<long long> s){
	long long res = 0 , p = 1;
 	for(int i = s.size() -1 ; i >=0 ; i--){
	  	res+=(s[i])*p;
		p*=10;
	}
	return res;
}
long long tobase(long long base , long long num){
	vector<long long> res;
	while(num){
	  	res.push_back(num%base);
		num/=base;
	}
	reverse(res.begin() , res.end());
	return tolong(res);
}
bool happy( long long n, long long base){
	map<long long , bool> M;
	while(!M[n]){
	  	if(n == 1) break;
		M[n] = true;
		long long res = 0;
		while(n){
		  res+=(n%10)*(n%10);
		  n/=10;
		}
		n = tobase(base,res);
	}
	//cout<<"happy   "<<n<<endl;
	return n == 1;
}
bool bases[11];
int main(){
	long long T , base;
	cin>>T;
	string s;
	getline(cin,s);
	for(long long t = 0 ; t < T; t++){
		memset(bases,0,sizeof(bases));{
		getline(cin,s);
		istringstream is(s);
		while(is>>base){
			bases[base] = true;
			}
		}
		bool ok = true;
		long long num = 1;
		do
		{
			num++;
		 // 	cout<<"********************"<<num<<endl;
		  	ok = true;
			for(long long i = 0 ; i <= 10 ; i++){
				if(bases[i]){
				  	long long inbase = tobase(i, num);
					//cout<<inbase<<" "<<i<<" "<<num<<endl;
					if(!happy(inbase,i)){
					  	ok = false;
						break;
					}
				}
			}

		}while(!ok);
		cout<<"Case #"<<t+1<<": "<<num<<endl;
	}
	return 0;
}
