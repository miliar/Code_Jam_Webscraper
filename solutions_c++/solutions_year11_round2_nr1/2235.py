#include<iostream>
using namespace std;
inline void f(long long &a,long long &b){
	if(a&&b){
		long long x=a,y=b;
		while((x=x%y)&&(y=y%x));
		a/=(x+y);
		b/=(x+y);
	}
	else if(a)
		a=1;
	else if(b)
		b=1;
}
inline void add(long long s[2],long long a[2]){
	if(s[0]&&a[0]){
		s[1]=s[1]*a[0]+a[1]*s[0];
		s[0]=s[0]*a[0];
		f(s[0],s[1]);
	}
	else if(a[0]){
		s[0]=a[0];
		s[1]=a[1];
	}
}
int main(){
	long long wp[100][2],owp[100][2],oowp[100][2],ans[100][2];
	double dowp[100],doowp[100];
	char in[100][101];
	int t,n;
	cin>>t;
	for(int x=1;x<=t;++x){
		cin>>n;
		for(int i=0;i<n;++i)
			dowp[i]=doowp[i]=wp[i][0]=owp[i][0]=oowp[i][0]=wp[i][1]=owp[i][1]=oowp[i][1]=ans[i][0]=ans[i][1]=0;
		for(int i=0;i<n;++i){
			cin>>in[i];
			for(int j=i+1;j<n;++j){
				if(in[i][j]=='1'){
						wp[i][0]++;
						wp[i][1]++;
						wp[j][0]++;
				}
				else if(in[i][j]=='0'){
						wp[j][0]++;
						wp[j][1]++;
						wp[i][0]++;
				}
			}
		}
		for(int i=0;i<n;++i){
			int wc=0;
			for(int j=0;j<n;++j){
				if(in[i][j]=='1'){
					++wc;
					wp[j][0]--;
					dowp[i] += ((double)(wp[j][1])/(double)(wp[j][0]));
					//add(owp[i],wp[j]);
					wp[j][0]++;
				}
				else if(in[i][j]=='0'){
					++wc;
					wp[j][0]--;
					wp[j][1]--;
					dowp[i] += (double)(wp[j][1])/(double)(wp[j][0]);
					//add(owp[i],wp[j]);
					wp[j][0]++;
					wp[j][1]++;
				}
			}
			////////cout<<i<<":"<<dowp[i]<<endl;
			dowp[i]/=wc;
			////////cout<<i<<"::"<<owp[i][1]<<'/'<<owp[i][0]<<endl;
			////cout<<i<<"..:"<<dowp[i]<<endl;
			//owp[i][0]*=wc;
		}
		printf("Case #%d:\n",x);
		for(int i=0;i<n;++i){
			//////////cout<<i<<endl;
			int wc=0;
			for(int j=0;j<n;++j){
				if(in[i][j]=='1'||in[i][j]=='0'){
					wc++;
					doowp[i]+=dowp[j];
					//add(oowp[i],owp[j]);
					////////cout<<j<<':'<<owp[j][1]<<'/'<<owp[j][0]<<endl;
				}
			}
			//oowp[i][0]*=wc;
			//doowp[i]/=4;
			doowp[i]/=wc;
			////cout<<i<<":"<<doowp[i]<<endl;
			//////////cout<<i<<':'<<oowp[i][1]<<'/'<<oowp[i][0]<<endl;
			//////////cout<<endl;
		}
		for(int i=0;i<n;++i){
			printf("%.12lf\n",( ((double)(wp[i][1])/(double)(wp[i][0]))/4 + dowp[i]/2 + doowp[i]/4));

			/*wp[i][0]*=4;
			owp[i][0]*=2;
			oowp[i][0]*=4;

			add(ans[i],wp[i]);
			add(ans[i],owp[i]);
			add(ans[i],oowp[i]);
			if(ans[i][0]){
				double a0=ans[i][0],a1=ans[i][1];
				//printf("%.12lf\n",a1/a0);
			}
			else{
				//printf("0\n");
			}*/
		}
	}
		
	
}
