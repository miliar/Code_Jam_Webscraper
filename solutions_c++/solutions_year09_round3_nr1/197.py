#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int ntc,n;
long long res,base,nowbase,value[100];
char buff[100];
vector <char> bases;

int main(){
	freopen("input2.txt","r",stdin);
	freopen("output2.txt","w",stdout);
	scanf("%d",&ntc);
	for (int tc=1;tc<=ntc;tc++){
		res=0;
		scanf("%s",buff);
		n=strlen(buff);
		bases.clear();
		for (int i=0;i<n;i++){
			bool ada=false;
			for (int j=0;j<bases.size();j++)
				if (bases[j]==buff[i]){
					ada=true;
					break;
				}
			if (!ada) bases.push_back(buff[i]);
		}
		nowbase=1;
		base=bases.size();
		if (base>=2) swap(bases[0],bases[1]);
		else base++;
		for (int i=n-1;i>=0;i--){
			int pos=0;
			for (int j=0;j<bases.size();j++)
				if (bases[j]==buff[i]){
					pos=j;
					break;
				}
			if (bases.size()==1) pos++; 
			res+=(nowbase*pos);
			if (i>0) nowbase*=base;
		}
		printf("Case #%d: %lld\n",tc,res);
	}
	return 0;
}
