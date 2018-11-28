#include<iostream>
using namespace std;
int cmb[9][9],oppo[9][9],change[255],t,n;
char z[200];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int Test;
	cin>>Test;
	change['Q']=1;
	change['W']=2;
	change['E']=3;
	change['R']=4;
	change['A']=5;
	change['S']=6;
	change['D']=7;
	change['F']=8;
	for (int test=1;test<=Test;test++){
		for (int i=0;i<9;i++)
			for (int j=0;j<9;j++){
				cmb[i][j]=0;
				oppo[i][j]=0;
			}
		cin>>n;
		for (int i=0;i<n;i++){
			char a,b,c;
			cin>>a>>b>>c;
			cmb[change[a]][change[b]]=c;
			cmb[change[b]][change[a]]=c;
		}
		cin>>n;
		for (int i=0;i<n;i++){
			char a,b;
			cin>>a>>b;
			oppo[change[a]][change[b]]=1;
			oppo[change[b]][change[a]]=1;
		}
		cin>>n;t=0;
		for (int i=0;i<n;i++){
			cin>>z[t];
			t++;
			if (t>=2 && cmb[change[z[t-2]]][change[z[t-1]]]!=0){
				z[t-2]=cmb[change[z[t-2]]][change[z[t-1]]];
				t--;
			}else{
				int flag=0;
				for (int j=0;j<t;j++)
					if (oppo[change[z[j]]][change[z[t-1]]]){
						flag=1;break;
					}
				if (flag)t=0;
			}
		}
		cout<<"Case #"<<test<<": [";
		if (t!=0)
			cout<<z[0];
		for (int i=1;i<t;i++)
			cout<<", "<<z[i];
		cout<<"]"<<endl;
	}
	return 0;
}
