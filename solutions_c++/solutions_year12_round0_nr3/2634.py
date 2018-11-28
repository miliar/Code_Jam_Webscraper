#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define rei(i,a,b) for(int i=a;i<b;i++)
#define red(i,a,b) for(int i=a;i>=b;i--)
#define ree(i,a,b) for(int i=a;i<=b;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define pb(a,x) a.push_back(x)
#define all(a) a.begin(),a.end()
#define srt(a) sort(all(a))
#define rev(a) reverse(all(a))

int main(){
	
	int test;
	scanf("%d",&test);

	ree(caseNo,1,test){
		unsigned long long ret=0llu;
		int a,b;
		scanf("%d%d",&a,&b);
		ree(num,a,b){

			int n=num;
			int dig=0;
			while(n){
				n/=10;
				dig++;
			}	
			set<int> goon;
			rei(pos,1,dig){
				int pre=num%( (int) pow(10.,pos*1.));
				int suf=num/( (int) pow(10.,pos*1.));
				int newNum= pre*( (int) pow(10.,dig-pos+0.))+suf;	

				int digNew=0;
				int nn=newNum;
				while(nn){
					nn/=10;
					digNew++;
				}
				if(digNew==dig && newNum>=a && newNum<=b){
					if(newNum>num){
						goon.insert(newNum);
					}

				}
			}		
			ret+=(unsigned long long)goon.size();	
			
		}
		cout<<"Case #"<<caseNo<<": "<<ret<<endl;
		
	}
	return 0;
}
