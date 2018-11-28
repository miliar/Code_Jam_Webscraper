#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
typedef vector<int> vi;
typedef long long int64;

int main() {

	int L,D,N;
	unsigned int Dic[5000][30] = {0};
	unsigned int temp,i, index;
	unsigned int out;
	string s;
	int cnt;

	cin>>L>>D>>N;	

	for(int dd=0;dd<D;dd++){    
		cin >>s;
		for (int ll=0; ll<L; ll++ ){			
			Dic[ll][s[ll]-'a'] |= (1 <<dd);
		}
	}

	for (int c=1; c <= N; c ++)
	{		
		out = (1<<D)-1;
		int ll = 0;
		while (ll < L){			
			cin >> s;	
			index = 0;
			while(s[index]){
			
				if (s[index]!='('){
					out &= Dic[ll][s[index]-'a'];
					ll ++;
					index ++;
				}
				else {
					temp = 0;
					index++;					
					while (s[index]!= ')'){
						temp |= Dic[ll][s[index]-'a'];
						index++;
					}
					index++;
					ll ++;
					out &= temp;
				}
			}
		}
		cnt = 0;
		for (i=0; i < D; i++){		
			if (out & (1<<i)) cnt ++;						
		}
		
		cout <<"Case #"<<c<<": "<< cnt <<endl;
		
		
	}
	return 0;
}
