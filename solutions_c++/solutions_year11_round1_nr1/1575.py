#include <iostream>
#include <string>
using namespace std;

int main(){
	int T;
	cin>>T;
	for (int t=0;t<T;t++){
		bool possible=true;
		int d, g;
		string s;
		cin>>s;
		cin>>d;
		cin>>g;

		if (s.length()<=3){
			int n = atoi(s.c_str());
			possible=false;
			for (int i=1;i<=n;i++){
				double doublei=(double)i;
				double doubled=((double)d)/100;
				if (doubled*doublei==(double)(int)(doubled*doublei)){
					possible=true;
					//cout<<doublei<<" "<<doubled<<" "<<doubled*doublei<<" ";
					break;
				}
				
			}
		}

		if (g==100 && d!=100)
			possible=false;
		if (d==100 && g==0)
			possible=false;
		if (g==0 && d!=0)
			possible=false;
		
		cout<<"Case #"<<(t+1)<<": ";
		if (possible){
			cout<<"Possible";
		}else
			cout<<"Broken";
		cout<<"\n";

	}
}