#include <iostream>
#include <vector>
#include <string>
using namespace std;

typedef long long LL;
typedef long double LD;

typedef vector<int> VI;

int main()
{
	int ttt;
	cin >> ttt;
	for(int cutest=1;cutest<=ttt;cutest++){
		int k;
		string S;
		cin >> k >> S;

		vector<int> p(k);
		
		int L=S.size();
		int BL=L;
		
		for(int i=0;i<k;i++)
			p[i]=i;
		
		do{
			string t=S;
			
			for(int x=0;x<L;x+=k){
				for(int j=0;j<k;j++)
				 t[x+j]=S[x+p[j]];
			}
			int a=1;
			for(int i=1;i<L;i++)
				if(t[i-1]!=t[i])
					a++;
			//printf(" got %s\n", t.c_str()); 
			BL=min(a,BL);
			
		}while( next_permutation(p.begin(), p.end()) );
		
		printf("Case #%d: %d\n",cutest,BL);
	}

}
