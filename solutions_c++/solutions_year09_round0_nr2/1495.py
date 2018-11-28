#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;
struct par{
	int pari;
	int parj;
}temp;


void func(vector<vector<int> >a,int i,int j,struct par &parent,int W,int H,vector<vector<char> >&b,char &ch){
	int dx[]={-1,0,0,1};
	int dy[]={0,-1,1,0};
	int minm=a[i][j],mini=i,minj=j;
	int k;
	for(k=0;k<4;k++){
		if(i+dx[k]>=0 && j+dy[k]>=0 && i+dx[k]<H && j+dy[k]<W){
			if(a[i+dx[k]][j+dy[k]]<minm){
		//		cout<<i+dx[k]<<" "<<j+dy[k]<<k<<"\n";
				mini=i+dx[k];
				minj=j+dy[k];
				minm=a[mini][minj];
			}
		}
	}
//	cout<<minm<<" "<<mini<<" "<<minj<<" \n";	
	if(!(mini==i && minj==j)){
			
//		cout<<"aa\n";
		if(b[mini][minj]=='#'){
			func(a,mini,minj,parent,W,H,b,ch);
		//	parent.pari=temp.pari;
		//	parent.parj=temp.parj;
		}
		else{
			parent.pari=mini;
			parent.parj=minj;
		//	temp.pari=mini;
		//	temp.parj=minj;
//			cout<<mini<<" "<<minj<<" "<<b[mini][minj]<<"\n";
			ch--;
		}

	}
	else{
		
	//	cout<<b[parent.pari][parent.parj]<<" \n";
		b[i][j]=b[parent.pari][parent.parj];

		return;
	}
	
//	cout<<b[parent.pari][parent.parj]<<" \n";
	b[i][j]=b[parent.pari][parent.parj];
	return;
}
int main(){
	int t,cnt=1,H,W,k,i,j;
	cin>>t;
	while(cnt<=t){
		cin>>H>>W;
		vector<vector<int> >a(H);
		vector<vector<char> >b(H);
		for(i=0;i<H;i++){
			for(j=0;j<W;j++){
				cin>>k;
				a[i].push_back(k);
				b[i].push_back('#');
			}
		}
/*		for(i=0;i<H;i++){
			for(j=0;j<W;j++){
				cout<<a[i][j]<<" ";
			}cout<<"\n";
		}*/
		char ch='a';
		struct par parent;
		b[0][0]='a';
		for(i=0;i<H;i++){
			for(j=0;j<W;j++){
				if((i==0 && j==0) || b[i][j]=='#'){
					parent.pari=i;
					parent.parj=j;
					b[i][j]=ch;
					
					func(a,i,j,parent,W,H,b,ch);
	//				goto A;
					ch++;
				}
			}
		}
		cout<<"Case #"<<cnt<<":\n";
		for(i=0;i<H;i++){
			for(j=0;j<W;j++){
				cout<<b[i][j]<<" ";
			}
			cout<<"\n";
		}
		cnt++;

	}
	return 0;
}


