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
typedef unsigned long long uint64;

int main() {

	int L,D,N;
	uint64 Dic[20][30][100] = {0};
	uint64 out[100];
	int index;	
	int i;
	string s;
	int cnt;

	cin>>L>>D>>N;	

	int countdd = 0;	
	int ddd = 0;
	for(int dd=0;dd<D;dd++){    			
		if (ddd >= 50) {ddd = 0; countdd++;}
		cin >>s;
		for (int ll=0; ll<L; ll++ ){					
			Dic[ll][s[ll]-'a'][countdd] |= (((uint64)1) <<ddd);
		}
		ddd++;
	}

	for (int c=1; c <= N; c ++)
	{		
		for (int icount =0; icount <= countdd; icount++)
			out[icount] = (((uint64)1)<<50)-1;

		int ll = 0;
		while (ll < L){			
			cin >> s;	
			index = 0;
			while(s[index]){
			
				if (s[index]!='('){
					for (int icount =0; icount <= countdd; icount++)
						out[icount] &= Dic[ll][s[index]-'a'][icount];
					ll ++;
					index ++;
				}
				else {
					uint64 temp[100] = {0};
					index++;					
					while (s[index]!= ')'){
						for (int icount =0; icount <= countdd; icount++)
							temp[icount] |= Dic[ll][s[index]-'a'][icount];
						index++;
					}
					index++;
					ll ++;
					for (int icount =0; icount <= countdd; icount++)
						out[icount] &= temp[icount];
				}
			}
		}
		cnt = 0;
		for (int icount =0; icount <= countdd; icount++)
			for (i=0; i < 50; i++){		
				if (out[icount] & (((uint64)1)<<i)) cnt ++;						
			}
		
		cout <<"Case #"<<c<<": "<< cnt <<endl;
		
		
	}
	return 0;
}
