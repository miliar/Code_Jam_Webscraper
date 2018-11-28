#include<iostream>
#include<map>
#include<vector>

using namespace std;
int main() {
map <char,int> m1;
map <int,char> m2;
m1['Q']=0; m1['W']=1; m1['E']=2; m1['R']=3; m1['A']=4; m1['S']=5; m1['D']=6; m1['F']=7;
m2[0]='Q'; m2[1]='W'; m2[2]='E'; m2[3]='R'; m2[4]='A'; m2[5]='S'; m2[6]='D'; m2[7]='F'; 
int c[8][8];
int w[8];
vector<int> list;
vector<vector<int> > d;
d.resize(8);
int T,N,D,C,i,j,k,l,aaa;
char a,b,aa;

cin>>T;
for(i=0;i<T;++i) {
	//zerowanie!!!
	for(j=0;j<8;++j) {w[j]=0;d[j].clear();for(k=0;k<8;k++) c[j][k]=-1;}
	list.clear();
	cin>>C;
	for(j=0;j<C;++j) {
	cin>>a;cin>>b;cin>>aa;
	c[m1[a]][m1[b]]=(int)aa;
	c[m1[b]][m1[a]]=(int)aa;
	}		
	cin>>D;
	for(j=0;j<D;++j) {
	cin>>a;cin>>b;
	d[m1[a]].push_back(m1[b]);
	d[m1[b]].push_back(m1[a]);
	}
	cin>>N;
	for(j=0;j<N;++j) {
	cin>>a;
	
	if ( list.size()>0 && list[list.size()-1]<10 &&  c [m1[a]] [list[list.size()-1] ] >-1 ) {
		//cout<<"kombinuje"<<endl;
		aaa=c [m1[a]] [list[list.size()-1] ];
		if (list[list.size()-1]<10) w[list[list.size()-1] ]--; 
		list.pop_back();
		list.push_back(aaa);
		}
	else {
		//cout<<"deletuje"<<endl;
		w[m1[a]]++;
		list.push_back(m1[a]);
		for(k=0;k< d[m1[a]].size();++k) {
		if (w [ d[m1[a]][k] ] >0) {
			list.clear();
			for(l=0;l<8;++l) w[l]=0;
			}
		}
		}	
	/*cout<<"krok "<<j<<endl;
	for(k=0;k<list.size();++k) cout<<m2[list[k]]<<"  ";
	cout<<endl;
	*/
	}
cout<<"Case #"<<i+1<<": [";
if (list.size()>0) {
		for(k=0;k<list.size()-1;++k) {
			if (list[k]<10) cout<<m2[list[k]]<<", ";
			else cout<<(char)list[k]<<", ";
			}
		if (list[list.size()-1]<10) cout<<m2[list[list.size()-1]]<<"]";
		else cout<<(char)list[list.size()-1]<<"]";
		}
else cout<<"]";
cout<<endl;
}

return 0;
}
