#include<iostream>
#include<vector>
#include<string.h>
#include<stdio.h>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<math.h>
#include<limits.h>
using namespace std;
#define FOR(i,a,b) for(i = (a); i < (b); i++)
#define RFOR(i,a,b)for(i = (b); i >= (a); i--)
#define FORI(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(v) (v).size()
#define ll long long int
#define ii pair<int,int>
void f(int i){
        cout << "Case #" << i << ": ";
}

	
bool fnd(char a[] , int cnt , char c){
	int i;
	int n = sizeof(a);
	FOR(i,0,cnt)
		if(a[i] == c)
			return 1;
	return 0;
}

int main()

{
//	ios_base::sync_with_stdio(0);	
	int i,j,k;
	int n;
	cin >> n;
	FOR(i,1,n+1){
		f(i);
		char a[30][30];
		FOR(j,0,30)
			FOR(k,0,30)
				a[j][k]='#';
		bool hate[30][30];
		CLEAR(hate,0);
		int n1;
		cin >> n1;
		string s;
		FOR(j,0,n1){
			cin >> s;
			//cout << s << "\n";
			//cout << s[0]-'A' << " " << s[1] - 'A' << " " << s[2] << "\n";
			a[s[0]-'A'][s[1]-'A'] = s[2] ;
			a[s[1]-'A'][s[0]-'A'] = s[2] ;	
		
		}
		//cout<<"value is " << a['A'-'A']['F'-'A']<<"\n";
		cin >> n1;
		FOR(j,0,n1){
                        cin >> s;
			//cout << "making " << s[0] << " " << s[1] << "\n";
                        hate[s[0]-'A'][s[1]-'A'] = 1;
                        hate[s[1]-'A'][s[0]-'A'] = 1;

		}
		//cout << "fuck "<<a['A'-'A']['F'-'A']<<"\n";
		cin >> n1;
		cin >> s;
		
		int cnt = 0;
		char aa[n1+10];
		aa[cnt++]=s[0];
		FOR(j,1,n1){
			aa[cnt++]=s[j];
			//cout << "curr " << s[j] << "\n";
			//FOR(k,0,cnt)
			//	cout << aa[k];
			//cout << "\n";		
			
			if(cnt>=2){
				char ch = a[aa[cnt-1]-'A'][aa[cnt-2]-'A'];
				//cout << ch << " " << aa[cnt-1] << " " << aa[cnt-2]<<"\n";
				if(ch!= '#' ){
					cnt -= 2;
					aa[cnt++]=ch;
					//cout << "writing "<<ch <<" at "<<cnt-1 <<"\n";
				}
				else{
					int tmp = cnt-1;
					FOR(k,0,tmp)
						if(hate[aa[k]-'A'][aa[cnt-1]-'A']){
							cnt = 0;
						//	cout << " nullifying \n";
							break;
						}
				}
				
			}
			
		}
			
		cout<<"[";
		FOR(j,0,cnt - 1)
			cout << aa[j] << ", ";
		if(cnt>0)
		cout << aa[cnt-1];
		cout << "]\n";		
		
	}

	return 0;
}
