#include<iostream>
#include<string>
using namespace std;

int t,n,k;
bool light[11];

void Handle(){
	memset(light,0,sizeof(light));
	for(int i=1;i<=k;++i){
		int cnt=1;
		for(int j=1;j<=n;++j)
			if(cnt==1){
				if(light[j])
					light[j]=false;
				else{
					light[j]=true; cnt=3;
				}
			}
			else 
				break;
	}
	bool on=true;
	for(int i=1;i<=n;++i)
		if(!light[i]){
			on=false;
			break;
		}
	if(on)
		printf("ON\n");
	else
		printf("OFF\n");
}

int main()
{
    freopen("A-small.in","r",stdin);
    freopen("test.out","w",stdout);
	cin>>t;
	for(int i=1;i<=t;++i){
		printf("Case #%d: ",i);
		cin>>n>>k;
		Handle();
	}
	return 0;
}
