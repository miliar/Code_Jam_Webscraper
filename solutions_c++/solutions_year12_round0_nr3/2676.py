#include <stdio.h>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>

int t,T;

int count(const std::string& str,int a,int b){
	std::vector<std::string> strv; 
	int ret=0;
	for (int i=1;i<(int)str.length();++i){
		std::string st;
		if (str[i] == '0');
		else{
			for (int j=0;j<(int)str.length();++j){
				st = st + str[(i+j)%str.length()];
			}
			strv.push_back(st);
		}
	}
	std::sort(strv.begin(),strv.end());
	strv.resize(std::unique(strv.begin(),strv.end())-strv.begin());
	for (int i=0;i<(int)strv.size();++i){
		int x,y;
		x = atoi(str.c_str());
		y = atoi(strv[i].c_str());
		if (x < y && a <= y && y <= b){
			++ret;
			//printf("%d %d\n",x,y);
		}
	}
	return ret;
}

int main(){
	freopen("c.in","rt",stdin);
	freopen("c.out","wt",stdout);
	scanf("%d",&T);
	for (t=1;t<=T;++t){
		int a,b;
		scanf("%d %d",&a,&b);
		int ans = 0;
		for (int i=a;i<=b;++i){
			std::ostringstream os;
			os << i;
			std::string str = os.str();
			ans += count(str,a,b);
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}