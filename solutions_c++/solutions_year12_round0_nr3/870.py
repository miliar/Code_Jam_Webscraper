#include<iostream>
#include<cmath>
#include<algorithm>
#include<cctype>
#include<vector>
#include<cassert>
#include<set>
#include<string>
#include<ctime>
#include<map>
using namespace std;
vector<pair<int,int> > v;
int p10[10] ;
int main (){
	freopen ( "C-large.in","r" , stdin);
	freopen ( "C-large.out","w" , stdout);

	p10[0] = 1;
	for ( int i=1 ; i<10 ; i++ ) p10[i] = p10[i-1]*10;
	char buff [40];
	for ( int i=1 ; i<=2000000 ; i++){
		//i = 1023;
		if ( i%1000 == 0 ) cerr << i << endl;
		sprintf(buff,"%d",i);
		int len = strlen ( buff ) ;
		for ( int i=0 ; i<len ; i++ )
			buff[i+len] = buff[i];
		buff[len+len] = 0;
		int second = 0 ;
		for ( int j=0 ; j<len ; j++ )
			second = second*10 + buff[j+1]-'0';
		if ( buff[1] != '0' && i!=second)
			v.push_back(make_pair(min(i,second),max(i,second)));
		for ( int j=2 ; j<len ; j++ ){
			second -= p10[len-1]*(buff[j-1]-'0');
			second *= 10 ;
			second += buff[j+len-1]-'0';
			if ( buff[j] != '0' && i!=second)
				v.push_back(make_pair(min(i,second),max(i,second)));
		}
		
	}
	sort(v.begin(),v.end());
	v.resize(unique(v.begin(),v.end())-v.begin());
	cerr << v.size() << endl;
	int tc;
	cin >> tc;
	for ( int C=1 ; C<=tc ; C++ ){
		int a , b;
		cin >> a >> b;
		int low = 0 , high = v.size() - 1;
		int start = -1 ;
		while ( low<=high ){
			int mid=(low+high)/2;
			if ( v[mid].first >= a ){
				start = mid ;
				high = mid - 1;
			}
			else low = mid + 1;
		}
		int answer = 0 ;
		if ( start == -1 );
		else{
			for ( int i=start ; i<v.size() && v[i].first <= b ; i++ ){
				if ( v[i].second <= b ) answer ++ ;
			}
		}
		cout << "Case #" << C << ": " << answer << endl;
	}
	
}