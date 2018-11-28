#include<iostream>
using namespace std;
int a[50];
int main(){
	int t;
	scanf("%d",&t);
	int count=1;
	while(t--){
		char str[100];
		scanf("%s",str);
		int i;
		for(i=0;i<50;i++)a[i]=-1;
		if(str[0]>='0'&&str[0]<='9')a[str[0]-'0']=1;
		else a[str[0]-'a'+10]=1;
		int l=strlen(str);
		int c=1;
		int j;
		for(j=1;j<l;j++){
			int k;
			if(str[j]>='0'&&str[j]<='9')k=str[j]-'0';
			else k=str[j]-'a'+10;
			if(a[k]==-1){
				if(c==1){
					a[k]=0;
					c=2;
				}
				else a[k]=c++;
			}
		}
		if(c==1)c=2;
		long long int ans=0;
		for(i=0;i<l;i++){
			int k;
			if(str[i]>='0'&&str[i]<='9')k=str[i]-'0';
			else k=str[i]-'a'+10;
			ans=ans*c+a[k];
		}
		cout<<"Case #"<<count<<": "<<ans<<endl;
		count++;
	}
	return 0;
}