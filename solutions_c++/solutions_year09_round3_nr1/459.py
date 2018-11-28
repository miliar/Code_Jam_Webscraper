#include <stdio.h>
#include <string.h>
#include <map>

using namespace std;


char in[100];
int num[100];
unsigned long long acc, t;
int id;

int main()
{
	int T, c, len, i;
	unsigned long long ans;
	scanf("%d",&T);
	c=1;
	while(T--){
		scanf("%s\n",in);
		len=strlen(in);
		for(i=0;i<len;i++)
			if(in[i]>='0' && in[i]<='9'){
				num[i]=in[i]-'0';
			}else{
				num[i]=in[i]-'a'+10;
			}
		
		map<int,int> mask;
		mask.clear();
		mask[num[0]]=2;
		num[0]=id=1;
		for(i=1;i<len;i++)
			if(!mask[num[i]]){
				if(id==2) id++; 
				mask[num[i]]=id;
				num[i]=id-1;
				id++;
			}else{
				num[i]=mask[num[i]]-1;
			}
			
		ans=0; acc=1; t=mask.size();
		if(t==1) t++;
		
		for(i=len-1;i>-1;i--){
			ans+= num[i]*acc;
			acc*=t;
		}
		printf("Case #%d: %I64u\n",c,ans,t);
		c++;
	}
	return 0;
}

