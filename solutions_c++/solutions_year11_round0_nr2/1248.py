#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

int main()
{

	int T;
	int C, D, N;
	int nc;
	string c;
	vector<char> ans;
	map<char,map<char,char> > com;
	map<char,char> opo; 
	map<char,int> ap;
	
	nc=1;
	cin>>T;
	while(T--){
		cin>>C;
		com.clear();
		opo.clear();
		for(int i=0;i<C;i++){
			cin>>c;
			com[c[0]][c[1]]=c[2];
			com[c[1]][c[0]]=c[2];
		}
		
		cin>>D;
		for(int i=0;i<D;i++){
			cin>>c;
			opo[c[0]]=c[1];
			opo[c[1]]=c[0];
		}
		
		cin>>N;
		cin>>c;
		
		char ant=-1;
		
		ap.clear();
		ans.clear();
		for(int i=0;i<N;i++){
			int j=0, ok=0;
			ok=1;
			if(com[ant][c[i]]!=0){
				ans[ans.size()-1]=com[ant][c[i]];
				ant=com[ant][c[i]];
				ok=0;
			}else for(j=0;j<ans.size();j++)
				if(opo[c[i]]==ans[j]){
					ans.clear();
					ant=-1;
					ok=0;
					break;
				}
					
			if(ok){
				ans.push_back(c[i]);
				ant=c[i];
			}			
		}
		
		printf("Case #%d: [",nc);
		for(int i=0;i<ans.size();i++){
			if(i==0){
				printf("%c",ans[i]);
			}else{
				printf(", %c",ans[i]);
			}
		}
		printf("]\n");
		
		nc++;
	}
	return 0;
}
