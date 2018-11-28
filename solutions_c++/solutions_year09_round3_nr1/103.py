#include<iostream>
#include<cstdio>
#include<string>
#include<set>
using namespace std;
string s ; 
set<char > S ; 
int mas[400] ;
int main(){
	freopen("avto.in","r", stdin);
	freopen("avto.out","w", stdout);
	int T ; 
	cin >> T ;
	for( int t = 1; t <= T ; t++){
		cin >> s ; 
		S.clear();
		int n = s.size(), i;
		
		for(i=0;i < 400; i++) mas[i] = -1;
		for(i=0;i < n; i++)
			S.insert(s[i]  );
		int Base = S.size();
		if(Base == 1) Base= 2 ; 
		long long val = 1;
		mas[s[0]] = 1; 
		int ind = 0; 
		for(i=1;i < n; i++){
			if( mas[s[i] ] != -1  ) 
				val = val*Base + mas[s[i]];
			else{ 
				if( ind == 1 ) ind++;
				mas[s[i]] = ind ; 
				val = val*Base + ind ; 
				ind++;
			}
		}
		cout << "Case #" << t << ": " << val << "\n" ;
	}

	return 0;

}