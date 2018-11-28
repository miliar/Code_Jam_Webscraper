#include<stdio.h>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	long long T,N;
	string str;
	char buf[25];
	scanf("%lld\n",&T);
	for(int i=0;i<T;i++){
		gets(buf);
		
		str.assign(buf);
		int l=str.length();
		bool flag=false;
		for(int j=l-1;j>0;j--)
		 {
 			if(str[j]>str[j-1]){
				char temp=str[j-1];
				sort(str.begin()+j,str.end());
				if(str[j-1]=='0'||str[j-1]<=temp){
					for(int k=j;k<l;k++)
					if(str[k]>str[j-1]){swap(str[k],str[j-1]);break;}
				}
				flag=true;
				goto exit;
			}
		}
exit:
		if(!flag){
			
			str.insert(str.begin(),'0');
			sort(str.begin(),str.end());			
			for(int k=1;k<=l;k++)
				if(str[k]!='0'){swap(str[k],str[0]);break;}
			
		}
		printf("Case #%d: %s\n",i+1, str.c_str());

	}
	return 0;
}