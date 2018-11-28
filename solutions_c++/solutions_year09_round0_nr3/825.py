#include<iostream>
using namespace std;
int main(){
	char pattern[20]="welcome to code jam";
	int T,cas=0;
	cin>>T;
	getchar();
	while(cas++<T){
		long long int coun[20]={0};
		coun[0]=1;
		int i=0,j=1,len;
		char inp[550];
		gets(inp);
		//len=strlen(inp);
//		cout<<inp<<endl;
		while(inp[i]!='\0'){
			j=1;
			while(j<=19){
				if(inp[i]==pattern[j-1]){
					coun[j]=(coun[j]+coun[j-1])%100000;
				}
				j++;
			}
			i++;
		}
		cout<<"Case #"<<cas<<": ";
		if(coun[19]>=10000)
			coun[19]=coun[19]%10000;
		if(coun[19]<10)
			cout<<"000"<<coun[19]<<endl;
		else if(coun[19]<100)
			cout<<"00"<<coun[19]<<endl;
		else if(coun[19]<1000)
			cout<<"0"<<coun[19]<<endl;
		else 
			cout<<coun[19]<<endl;
	}
	return 0;
}
