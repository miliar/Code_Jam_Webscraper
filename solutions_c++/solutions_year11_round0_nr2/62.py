#include<iostream>
#include<string.h>
#include<stdio.h>
#include<vector>
#include<stack>
using namespace std;
int n1,n2,n3;
int c[27][27],d[27][27];  //c combine d delete
int s[105];
char a[105],b[5];
stack<int> st;
int main(){
	int T,r,i,t1,t2,t3,j,m;
	bool f;
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	for(r=1;r<=T;r++){
//		memset(c,0,sizeof(c));
//		memset(d,0,sizeof(d));
		for(i=0;i<27;i++)
			for(j=0;j<27;j++){
				c[i][j]=-1;
				d[i][j]=0;
			}
		cin>>n1;
		for(i=0;i<n1;i++){
			cin>>b;
			t1=b[0]-'A';
			t2=b[1]-'A';
			t3=b[2]-'A';
			c[t1][t2]=c[t2][t1]=t3;
		}
		cin>>n2;
		for(i=0;i<n2;i++){
			cin>>b;
			t1=b[0]-'A';
			t2=b[1]-'A';
			d[t1][t2]=d[t2][t1]=1;
		}
		cin>>n3;
		cin>>a;
		m=0;
		for(i=0;i<n3;i++){
			t1=a[i]-'A';
			if(st.empty()){
				st.push(t1);
				s[m++]=t1;
			}
			else{
				t2=st.top();
				t3=c[t1][t2];
				if(t3>=0){
					st.pop();
					st.push(t3);
					s[m-1]=t3;
				}
				else{
					f=false;
					for(j=0;j<m;j++){
						if(d[s[j]][t1]==1){
							f=true;
							break;
						}
					}
					if(f){
						while(!st.empty()){
							st.pop();
						}
						m=0;
					}
					else{
						st.push(t1);
						s[m++]=t1;
					}
				}
			}
		}
		cout<<"Case #"<<r<<": [";
		if(m>0)
			cout<<(char)(s[0]+'A');
		for(i=1;i<m;i++)
			cout<<", "<<(char)(s[i]+'A');
		cout<<']'<<endl;
		while(!st.empty())
			st.pop();
	}
}