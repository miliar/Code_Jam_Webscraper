#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D.out","w",stdout);
	
	int T,N,count=0,cnt,tmp;
	cin>>T;
	while(T--){
		cin>>N;
		cnt=0;
		count++;
		for(int i=1;i<=N;i++){
			cin>>tmp;
			if(tmp!=i)cnt++;
		}
		cout<<"Case #"<<count<<": ";
		printf("%.6f\n",(double)cnt);
	}
	
}
