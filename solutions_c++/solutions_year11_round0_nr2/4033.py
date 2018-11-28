#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<ctime>

using namespace std;

int main(){
     int t;
     FILE * in = freopen("input.txt","r",stdin);
     FILE * out = freopen("output.txt","w",stdout);
     cin>>t;
     for(int j=0;j<t;j++){		
		int c,d,n;
		cin>>c;
		char C[c][4], D[d][4];
		for(int a=0;a<c;a++){
			cin>>C[a];
		}
		cin>>d;
		for(int b=0;b<d;b++){
			cin>>D[b];
		}
		cin>>n;
		char S[n];
		char F[n];
		cin>>S;
		int m=0,l=0;
		for(int k=0;k<n;k++){
			F[l]=S[k];
			l++;
			if(l==1)
				continue;
//			chkReplace();
			for(int o=0;o<c;o++){
				if((C[o][0]==F[l-2] && C[o][1]==F[l-1]) || (C[o][0]==F[l-1] && C[o][1]==F[l-2])){
					F[l-2]=C[o][2];
					l--;
					break;
				}
			}
			//chkClear();
			for(int p=0;p<d;p++){
				for(int q=0;q<l;q++){
					for(int r=q+1;r<l;r++){
						if((D[p][0]==F[q] && D[p][1]==F[r]) || (D[p][1]==F[q] && D[p][0]==F[r])){
							l=0;
						}
					}
				}
			}
		}
		cout<<"Case #"<<(j+1)<<": [";
		for(int i=0;i<l;i++){
			if(i==l-1)
				cout<<F[i];
			else
				cout<<F[i]<<", ";
		}
		cout<<"]"<<endl;		
	}
     return 0;
}
