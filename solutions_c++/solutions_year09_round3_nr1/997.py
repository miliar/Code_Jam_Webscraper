#include<stdio.h>
#include<string>
#include<vector>
#include<math.h>
#include<stdio.h>
using namespace std;
int main(void)
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	char buf[70];
	string str;
	string st;
	
	scanf("%d\n",&T);
	for(int i=0;i<T;i++)
	{
		gets(buf);
		str.assign(buf);
		int l=str.length();
		int base=1;
		vector<int> vi(l,0);
		for(int j=0;j<l;j++){
			if(vi[j]==0){
				vi[j]=base;
				for(int k=j+1;k<l;k++){
					if(str[j]==str[k])vi[k]=base;
				}
				base++;
			}
		}
		
		for(int k=1;k<l;k++){
			if(str[0]!=str[k]){
				vi[k]=0;
				for(int p=0;p<l;p++){
					if(str[k]==str[p])vi[p]=0;
					else if(vi[p]!=1) vi[p]--;
				}
				base--;
				break;
			}
			
		}
		long long res=0;
		for(int k=0;k<l;k++)
			res+=powl(base,l-k-1)*vi[k];
		printf("Case #%d: %lld\n",i+1,res);

	}
	return 0;
}




