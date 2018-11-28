#include <iostream>
#include <fstream>
#include <assert.h>
#include <queue>
using namespace std;
#define DISK
int main(){
	int T,R,k,N,s,sum;
	#ifdef DISK
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	if(!fin||!fout){
		cout<<"can not open the file"<<endl;
		system("pause");
		return 1;
	}
	//typedef fin File;
	#else
	//typedef cin File;
	#endif
	fin>>T;
	int i,j,kk,m,n,tmp;
	for(i=0;i<T;i++){
		fin>>R>>k>>N;
		queue<int> group;
		for(j=0;j<N;j++){
			fin>>tmp;
			group.push(tmp);
		}
		sum=0;
		int sz=group.size();
		for(j=0;j<R;j++){
			s=0;
			m=0;
			while(true){
				if(m>=sz)break;
				tmp=group.front();
				s+=tmp;
				if(s<=k){
				   group.pop();
			   	group.push(tmp);
				}
			   else{
				  s-=tmp;
				  break;
			   }
			   m++;
		  }
		 // cout<<"S ="<<s<<endl;
		  sum+=s;
		 // cout<<endl;
		}
		fout<<"Case #"<<i+1<<": "<<sum<<endl;
	}
	fin.close();
   fout.close();
	system("pause");
	return 0;
}
