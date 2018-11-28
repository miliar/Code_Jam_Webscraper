#include<iostream>
#include<fstream>
#include<algorithm>
#include<set>
#include<vector>
using namespace std;
vector<int> rel;
int p,q;
int fn ( int p , int ind ) {
	int lower=0 , upper=p-1;
	for ( int i=0; i<ind; i++  ) {
		if ( rel[i]<p && rel[i]>lower ) lower=rel[i];
		if ( rel[i]>p && rel[i]<upper ) upper=rel[i];
	}
	return upper-lower+1;
}
int cost ( int ind ) 	{
	/*int upper=p-1 , lower=0;
	for ( int i=0; i<ind; i++ ) {
		if ( rel[i]<p && lower<rel[i]  ) lower=rel[i];
		if ( rel[i]>p && upper>rel[i]  ) upper=rel[i];
	}
	return rel[ind]-lower-1 + upper-rel[ind];*/
	int lower=-1 , upper=p;
	for( int i=0; i<ind; i++ ) {
		if ( rel[i]<rel[ind] && lower<rel[i]  ) lower=rel[i];
		if ( rel[i]>rel[ind] && upper>rel[i]  ) upper=rel[i];
	}
	cout<<"kjhdf"<<lower<<" "<<upper<<endl;	 
	return (rel[ind]-lower-1) + (upper-rel[ind]-1);
}
int main()	{
	int T,n,test=1,add,ans,temp;
	ifstream fin ( "iinp.in");
	ofstream fout ( "op.txt");
	
	fin>>T;
	int i;
	while ( T-- )  {
		ans=1000000000;
		rel.clear();
		fin>>p>>q;
		rel.resize(q);
		for ( i=0; i<q; i++ ) { fin>>rel[i]; rel[i]--;}
		sort ( rel.begin() , rel.end() );
		do {
			cout<<cost(1)<<endl;
			for ( i=0; i<rel.size(); i++) cout<<rel[i]<<" ";
		temp=p-1;
			for ( i=1; i<q;i++ ) {
				temp+=cost(i);
				cout<<"d"<<temp<<endl;
			}
			cout<<temp<<endl;
			if ( temp<ans ) ans=temp;
		}while ( next_permutation(rel.begin(),rel.end()));
		fout<<"Case #"<<test++<<": "<<ans<<endl;
	}
	return 0;
}
