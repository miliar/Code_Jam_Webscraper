#include<iostream>
using namespace std;
int n,test;
char a[110];
int b[110],o[110],r[110],on,rn;
void move(int& a,int b){
	if (a<b)
		a++;
	else if (a>b)
		a--;
	return ;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>test;
	for (int casenum=1;casenum<=test;casenum++){
		cin>>n;
		for (int i=0;i<n;i++)
			cin>>a[i]>>b[i];
		o[n]=0;r[n]=0;
		for (int i=n-1;i>=0;i--){
			o[i]=o[i+1];r[i]=r[i+1];
			if (a[i]=='O')
				o[i]=b[i];
			else
				r[i]=b[i];
		}
		int num=0;
		on=1;rn=1;
		for (int i=0;i<n;i++){
			while (true){
				if (a[i]=='O'){
					num++;
					move(rn,r[i]);
					if (on==b[i])
						break;
					else
						move(on,o[i]);
				}else{
					num++;
					move(on,o[i]);
					if (rn==b[i])
						break;
					else
						move(rn,r[i]);
				}
			}
		}
		cout<<"Case #"<<casenum<<": "<<num<<endl;
	}
	return 0;
}
