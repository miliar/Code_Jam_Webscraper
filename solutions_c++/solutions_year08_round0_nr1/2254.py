# include <iostream>
# include <vector>
# include <map>
# include <string>
using namespace std;
string inp(){
	char buff[100];
	scanf("  %[^\n]",&buff);	
	return buff;
}
int main(){
	int ctr,sz,q,sw;
	int t;
	map<string,bool>::iterator iter;
	scanf("%d",&t);
	string tt;
	for(int i=0;i<t;i++){
		map <string,bool> a;
		scanf("%d",&sz);
		sw=ctr=0;
		for(int j=0;j<sz;j++)a[inp()]=false;
		scanf("%d",&q);		
		while(q--){
		       tt=inp();
		       if(a[tt]==false)a[tt]=true,ctr++;
			if(ctr==sz){
				sw++,ctr=1;
				for(iter =a.begin();iter!=a.end();++iter)
					if(iter->first!=tt)					
						iter->second = false;
			}			 	
		}
		cout << "Case #" << i+1 << ": " << sw << endl;
	}
	return 0;
}
