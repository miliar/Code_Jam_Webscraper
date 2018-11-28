#include <stdio.h>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

int main(){
	int ntc;
	scanf("%d",&ntc);
	for (int tc=1;tc<=ntc;tc++){
		map<string,char> magic;
		int c,d,n,reslen;
		char opp[30][3];
		char buff[200];
		int count[200];
		string res;
		magic.clear();
		memset(count,0,sizeof(count));
		scanf("%d",&c);
		for (int i=0;i<c;i++){
			scanf(" %s",buff);
			string tbuff1 (buff,2);
			magic[tbuff1]=buff[2];
			swap(buff[0],buff[1]);
			string tbuff2 (buff,2);
			magic[tbuff2]=buff[2];
		}
		scanf("%d",&d);
		for (int i=0;i<d;i++) scanf(" %s",opp[i]);
		scanf("%d",&n);
		scanf(" %s",buff);
		reslen=1;
		res=buff[0];
		for (int i=1;i<n;i++){
			res=res+buff[i];
			while((res.length()>1)&&(magic.count(res.substr(res.length()-2,2)))){
				res=res+magic[res.substr(res.length()-2,2)];
				res.erase(res.length()-3,2);
			}
			for (int j=0;j<d;j++)
				if (((int)res.find(opp[j][0])>=0)&&((int)res.find(opp[j][1])>=0))
					res.clear();
		}
		printf("Case #%d: [",tc);
		for (int i=0;i<(int)res.length()-1;i++) printf("%c, ",res[i]);
		if (res.length()>0) printf("%c",res[res.length()-1]);
		printf("]\n");
	}
	return 0;
}