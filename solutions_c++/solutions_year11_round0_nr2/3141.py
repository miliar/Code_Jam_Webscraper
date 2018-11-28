#include <cstdio>
#include <vector>

using namespace std; 

#define pb push_back
#define pp pop_back

int t,c,d,n;
char sd[2];
char sc[3];
char str[30];
vector <char> s;
int main(){
	freopen("magi.in","r",stdin);
	freopen("magi.out","w",stdout);
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		s.erase(s.begin(),s.end());

		scanf("%d",&c);
		if (c>0){
			scanf("%s",sc);
		}else{
			sc[0]=' ';
			sc[1]=' ';
			sc[2]=' ';
		}

		scanf("%d",&d);
		if (d>0){
			scanf("%s",sd);
		}else{
			sd[0]=' ';
			sd[1]=' ';
		}

		scanf("%d",&n);
		scanf("%s",str);

		for(int j=0;j<n;j++){
			s.pb(str[j]);
			int h=s.size();
			while ((s.size()>1) 
				&& ((s[s.size()-1]==sc[0] && s[s.size()-2]==sc[1]) 
				 || (s[s.size()-1]==sc[1] && s[s.size()-2]==sc[0]))){
				s.pp();
				s.pp();
				s.pb(sc[2]);
			}
			if (s.size()>0 && s[s.size()-1]==sd[0]){
				int fnd=0;
				for (int k=0;(k<(s.size()-1)) && fnd==0;k++){
					if (s[k]==sd[1])fnd=1;
				}
				if (fnd==1)s.erase(s.begin(),s.end());
			}
			if (s.size()>0 && s[s.size()-1]==sd[1]){
				int fnd=0;
				for (int k=0;k<(s.size()-1);k++){
					if (s[k]==sd[0])fnd=1;
				}
				if (fnd==1)s.erase(s.begin(),s.end());
			}
		}

		printf("Case #%d: [",i+1);
		int flag=0;
		for(int j=0;j<s.size();j++){
			printf((flag==0)?"%c":", %c",s[j]);
			flag=1;
		}
		printf("]\n");
	}
	return 0;
}