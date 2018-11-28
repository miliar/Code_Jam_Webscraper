#include <iostream>
#include <map>
#include <string>
#include <cstdio>

using namespace std;

int main(){
    
    map<string, bool> mm;
    
    int casenum, enginenum, q, use=0, ans;
    cin>>casenum;
    for (int i=0; i<casenum; i++){
        cin>>enginenum;
        getchar();
        string temp;
		ans=0;
		
		
        for (int j=0; j<enginenum; j++){
            char tt[105];
            gets(tt);
            temp=tt;
            mm[temp]=false;
        }
        cin>>q;
        getchar();
		use=0;
        for (int j=0; j<q; j++){
            char tt[105];
            gets(tt);
            temp=tt;
	
			if (mm[temp]==false){
				use++;
				mm[temp]=true;
				if (use==enginenum){
					ans++;
					use=1;
					map<string, bool>::iterator iter2;
					for( iter2 = mm.begin(); iter2 != mm.end(); iter2++ ) {
						iter2->second=false;						
					}				
					mm[temp]=true;
				}				
				//cout<<"ans="<<ans<<"   q="<<q<<endl;
			}
        }
		
		//cout<<"q="<<q<<" Case #"<<(i+1)<<": "<<ans<<endl;
		cout<<" Case #"<<(i+1)<<": "<<ans<<endl;
    }
    
    return 0;    
}
