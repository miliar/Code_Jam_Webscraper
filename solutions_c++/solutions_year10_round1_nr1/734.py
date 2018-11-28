#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
	int z,n,k,ind;
	int red, blue,si,sj,cnt;
	cin>> z;
	for(int y=1;y<=z;y++){
		vector<string> v,vv;
		string s;
		cin>>n>>k;
		red=blue=0;
		for(int i=0;i<n;i++){
			cin>>s;
			v.push_back(s);
		}
		s=string(n,'.');
		for(int i=0;i<n;i++){
			vv.push_back(s);
			ind=n-1;
			for(int j=n-1;j>=0;j--)
				if(v[i][j]!='.')
					vv[i][ind--]=v[i][j];
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<=n-k;j++){
				if(!red){
					si=i;
					sj=j;
					cnt=0;
					while(sj<n && vv[sj][si]=='R'){
						cnt++;
						sj++;
					}
					if(cnt>=k)red=1;
					si=i;
					sj=j;
					cnt=0;
					while(sj<n && vv[si][sj]=='R'){
						cnt++;
						sj++;
					}
					if(cnt>=k)red=1;
					if(i<=n-k){
					si=i;
					sj=j;
					cnt=0;
					while(si<n && sj<n && vv[si][sj]=='R'){
						cnt++;
						si++;
						sj++;
					}
					if(cnt>=k)red=1;
					si=i+k-1;
					sj=j;
					cnt=0;
					while(si>=0 && sj<n && vv[si][sj]=='R'){
						cnt++;
						si--;
						sj++;
					}
					if(cnt>=k)red=1;
					}
				}
				if(!blue){
					si=i;
					sj=j;
					cnt=0;
					while(sj<n && vv[sj][si]=='B'){
						cnt++;
						sj++;
					}
					if(cnt>=k)blue=1;
					si=i;
					sj=j;
					cnt=0;
					while(sj<n && vv[si][sj]=='B'){
						cnt++;
						sj++;
					}
					if(cnt>=k)blue=1;
					if(i<=n-k){
					si=i;
					sj=j;
					cnt=0;
					while(si<n && sj<n && vv[si][sj]=='B'){
						cnt++;
						si++;
						sj++;
					}
					if(cnt>=k)blue=1;
					si=i+k-1;
					sj=j;
					cnt=0;
					while( si >=0 && sj<n && vv[si][sj]=='B'){
						cnt++;
						si--;
						sj++;
					}
					if(cnt>=k)blue=1;
					}
				}
			}
		}/*
		for(int i=0;i<n;i++){
			cout<<vv[i]<<endl;
		}*/
		if(red && blue){
			cout<< "Case #"<<y<<": Both"<<endl;
		}else if(red)
			cout<< "Case #"<<y<<": Red"<<endl;
		else if(blue)
			cout<< "Case #"<<y<<": Blue"<<endl;
		else
			cout<< "Case #"<<y<<": Neither"<<endl;
	}
}
