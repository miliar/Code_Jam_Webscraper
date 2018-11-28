#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdio>
using namespace std;

class data
{
public:
	char c;
	bool f;
};

int main(){
	int T,n;
	int i,j,k,x,y;
	data d;
	string s;
	
	x = 1;
	scanf("%d",&T);
	while(T--){
		d.c = '-'; d.f = false;
		vector<vector<data> > vd(26,vector<data> (26,d));
		
		scanf("%d",&n);
		for(i=0;i<n;i++){
			cin>>s;
			j = s[0] - 65;
			k = s[1] - 65;
			vd[j][k].c = s[2];
			vd[k][j].c = s[2];
		}
		
		scanf("%d",&n);
		for(i=0;i<n;i++){
			cin>>s;
			j = s[0] - 65;
			k = s[1] - 65;
			vd[j][k].f = true;
			vd[k][j].f = true;
		}
		
		string a,ans;
		scanf("%d",&n);
		cin>>s;
		for(i=0;i<n;i++){
			if(a == "") a += s[i];
			else{
				j = a[a.size()-1] - 65;
				k = s[i] - 65;
				if(vd[j][k].c != '-') a[a.size()-1] = vd[j][k].c;
				else{
					bool flag = false;
					for(y=0;y<a.size();y++){
						j = a[y] - 65;
						if(vd[j][k].f){
							flag = true;
							break;
						}
					}
					if(flag) a = "";
					else a += s[i];
				}
			}
		}
		
		ans += '[';
		for(i=0;i<a.size();i++){
			if(i != 0) ans += ", ";
			ans += a[i];
		}
		ans += ']';
		
		printf("Case #%d: %s\n",x,ans.c_str());
		x++;
	}
	return 0;
}
