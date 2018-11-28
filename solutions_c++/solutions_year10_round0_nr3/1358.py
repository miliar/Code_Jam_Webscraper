#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>
#include<cmath>
#include<stack>
#include<fstream>
#include<list>
#define f(i,n) for(int i=0;i<n;i++)
#define vi vector<int>
#define vs vector<string>
#define p_b push_back
using namespace std;
//stringstream ss (stringstream::in | stringstream::out);

int main(){
	fstream fin,fout;
	fin.open ("input.txt", fstream::in | fstream::out);
	fout.open ("output.txt", fstream::in | fstream::out);
	int t;
	fin>>t;
	f(k1,t){
		int r,k,n;
		fin>>r>>k>>n;
		vi v(n);
		f(i,n)
			fin>>v[i];
		vi v1(n),u;
		int i=0,x1=0,t1=1;
		u.p_b(0);
		while(t1<=r && !v1[i]){
			int x=0,j=0,i1=i;
			while(x+v[i]<=k && j<n){
				x+=v[i];
				i=(i+1)%n;
				j++;
			}
			
			x1+=x;
			u.p_b(x1);
			v1[i1]=t1;
			t1++;
			cout<<i1<<"  "<<x1<<" "<<t1<<endl;

		}
		cout<<"i="<<i<<endl;
		int tc;
		t1;
		if(!v1[i]){
			cout<<"nitin";
			tc=x1;
			
		}
		else{
			int c=t1-v1[i];
			if((r-v1[i]+1)%c==0)
				tc=u[v1[i]-1]+((r-v1[i]+1)/c)*(x1-u[v1[i]-1]);
			else
				tc=((r-v1[i]+1)/c)*(x1-u[v1[i]-1])+u[v1[i]+(r-v1[i])%c];
			/*if(i!=0){
				
				tc=u[v1[i]-1]+((r-v1[i])/c)*(x1-u[v1[i]-1])+u[v1[i]+(r-v1[i])%c];
			}
			else{
				tc=(r/t1)*x1+u[r%t1];
			}*/
		}
		cout<<"tc=="<<tc<<endl;
		fout<<"Case #"<<k1+1<<": "<<tc<<endl;


	}

}


 