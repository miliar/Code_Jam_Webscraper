#include<iostream>
#include<set>
#include<string>
#include<vector>
#include<map>
#include<fstream>
#include<algorithm>
//#include<sstream>
#define f(i,n) for(int i=0;i<n;i++)
struct node{
	string s;
	float f;
	node *left,*root;
};

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	//stringstream ss (stringstream::in | stringstream::out);
	int t;
	int c1=1;
	fin>>t;
	while(t--){
		int p,q;
		fin>>p>>q;
		vector<int>u(q);
		int c=0,m=100000000;
		f(i,q){
			int x;
			fin>>u[i];
		}
		sort(u.begin(),u.end());
		do{
			c=0;

			vector<int>v(p,1);
			f(i,q){
				int x=u[i];
				v[x-1]=0;
				int j=x-2;
				while(j>=0 && v[j]==1){
					c++;
					j--;
				}
				j=x;
				while(j<p && v[j]==1){
					c++;
					j++;
				}
			}
			m=min(m,c);
		}while(next_permutation(u.begin(),u.end()));
		fout<<"Case #"<<c1<<": "<<m<<endl;


		c1++;
	}


	fin.close();
	fout.close();
	return 0;
}
		




		

