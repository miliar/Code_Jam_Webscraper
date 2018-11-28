#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;

int main(){
	
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout); 
    
    string temp;
	int i,j,k,l;
	int t,c,d,n,w;
	vector < pair < pair<char, char>, char > > combine;
	vector < pair < char, char > > oppose;
	vector <char> out;
	int count=0,flag=0;
	char tmp1,tmp2;
	cin>>t;

	for ( k=1; k<=t; k++){
		
        cin>>c;
        for ( int z=0; z<c ; z++ ){
			cin>>temp;
			combine.push_back( make_pair( make_pair( temp[0], temp[1] ), temp[2] ) );
			combine.push_back( make_pair( make_pair( temp[1], temp[0] ), temp[2] ) );
		}
		
		cin>>d;
        for ( int z=0; z<d ; z++ ){
			cin>>temp;
			oppose.push_back( make_pair( temp[0], temp[1] )  );
			oppose.push_back( make_pair( temp[1], temp[0] )  );
		}
		
		cin>>n;
		cin>>temp;
		out.push_back(temp[0]);
		count=1;
		
		

		
		while ( count!=n ){
			
			
			out.push_back(temp[count]);
			count++;
				
			if( out.size() >= 2 ){
					
				tmp1=out.back();
                out.pop_back();
				tmp2=out.back();
                out.pop_back();
                
				for( i=0; i<combine.size(); i++ ){
					if ( combine[i].first == make_pair( tmp1, tmp2) ){
						out.push_back(combine[i].second);
						flag=1;
						break;
					}
				}
				
							
				if ( !flag ){
					out.push_back(tmp2);
				}
					
				if ( !flag ){
					for( i=0; i<oppose.size(); i++ ){
						if ( oppose[i].first == tmp1 ){
							for( w=0; w<out.size(); w++ ){
									if ( out[w] == oppose[i].second ){
										
										flag=1;
										out.clear();
										break;
									}
								}
							break;
						}
					}
				}

				if ( !flag ){
					out.push_back(tmp1);
				}
				
			}
			

			
		flag=0;
			
		}
	
		
		cout<<"Case #"<<k<<": [";
		for( i=0; i<((int)out.size()-1); i++ )  {
			cout<<out[i]<<", ";}
		if( out.size() )
			cout<<out[out.size()-1]<<"]"<<endl;
		else
			cout<<"]"<<endl;
		
		
		out.clear();
		oppose.clear();
		combine.clear();
	}
		
			
			
			
			
			
			
			
		



	return 0;
}
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
