#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
	int  n , a , b , i , j;
	char s[10];
	while( scanf("%d",&n) != EOF ){
		for( int tc = 1 ; tc <= n;tc++ ){
			scanf("%d%d",&a,&b);
			int res = 0 ;
			for( i = a ; i <= b;i++ ) {
				sprintf(s,"%d",i);
				//cout<<i<<endl;
				string tmp = string(s);
				vector<int>ivec; ivec.clear();
				 {
					for( j = 1 ; j < tmp.length();j++ ) {
						string cur = tmp.substr( j, tmp.length()-j ) + tmp.substr( 0 , j);
						//cout<<cur<<endl;
						int itmp = atoi( cur.c_str() );
						if( itmp > i && itmp <= b){
							 ivec.push_back( itmp );
							// cout<<i<<" "<<itmp<<endl;
						}
					}
					//tmp = "0" + tmp;
				}
				res += unique( ivec.begin() , ivec.end() ) - ivec.begin();
				
			}
			printf("Case #%d: %d\n",tc,res);
		}
	}
	return 0;
}