#include <iostream>
#include <vector>
#include <string>

#define MIN(X,Y) ((X)<(Y)?(X):(Y))

using namespace std;

int calc(int i,int B){
	int kotae[10];
	int ans=0;
	int keta;
	int k=1;
	int buf=i;
	for(keta=1;keta*10<=i;k++) keta*=10;
	
	for(int j=1;j<k;j++){
		buf=buf/10+buf%10*keta;
//		cout<<buf<<endl;

		if(buf>=keta&&buf>i&&buf<=B){
			for(int n=0;n<ans;n++) if(kotae[n]==buf) goto loop_end;
			kotae[ans]=buf;
			ans++;
		}
loop_end: ;
	}
	return ans;
}

int main(){
	int T;
	cin>>T;

	int A,B;
	long long ans;


	for(int i=0;i<T;i++){
		cin>>A>>B;
		ans=0;
		for(int j=A;j<B;j++){
			ans+=calc(j,B);
		}

		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}
