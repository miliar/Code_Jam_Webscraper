#include<iostream>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<stack>
using namespace std;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int i,j,k;
	int C,D,N;
	string str;
	int nca;

	cin>>nca;
	for(int cid=1;cid<=nca;cid++){
		map<string,map<string,int> >opp;
		map<string,string>com;
		cin>>C;
		string str;
		while(C--){
			cin>>str;
			string a=str.substr(0,1),
				b=str.substr(1,1),
				c=str.substr(2,1);
			if( a > b )swap(a,b);
			com[a+b] = c;
		}
		cin>>D;
		while(D--){
			cin>>str;
			string a=str.substr(0,1),
				b=str.substr(1,1);
			opp[a][b] = 1;
			opp[b][a] = 1;
		}
		cin>>N;
		stack<string>st;
		cin>>str;
		for(int i=0;i<N;i++){
			string tmp = str.substr(i,1);
			
			
			bool is_opp = false;

			if( st.empty() ){
				st.push(tmp);
			}else {
				string topstr = st.top();
				
				
				//combine
				if( com[min(tmp,topstr) + max(tmp,topstr)] != "" ){
					st.pop();
					st.push( com[min(tmp,topstr) + max(tmp,topstr)] );
				}
				//opp
				else 
				{
					stack<string>ts = st;
					while( !ts.empty() ){
						if( opp[tmp][ ts.top() ] == 1 ){
							while( !st.empty() )st.pop();
							is_opp = true;
							break ;
						}

						ts.pop();
					}

					if( !is_opp ) st.push(tmp); 
				}
			}
		}
		
		

		string ret = "";
		while( !st.empty() ){
			string tmp = st.top();
			st.pop();

			if( ret == "" )ret += tmp ;
			else ret = tmp + ", " + ret ;
		}

		ret = "[" + ret + "]";
		cout<<"Case #"<<cid<<": "<<ret<<endl;
	}
}