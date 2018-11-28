#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main(){
	int casos;
	cin>>casos;
	for (int cas=1; cas<=casos; cas++){
		int s, q;
		cin>>s;
		cin.ignore();
		vector <string> sea (s);
		for (int i=0; i<s; i++) getline (cin, sea[i]);
		cin>>q;
		if (q>0){
			cin.ignore();
			vector <string> que (q);
			for (int i=0; i<q; i++) getline (cin, que[i]);
			vector <vector <int> > v (q, vector <int> (s, q+1));
			for (int i=0; i<s; i++) if (que[0]!=sea[i]) v[0][i]=0;
			for (int i=1; i<q; i++)for (int j=0; j<s; j++){
				int a=v[i-1][j];
				if (v[i][j]==q+1) v[i][j]=a;
				if (que[i]==sea[j]){
					for (int h=0; h<s; h++) if (v[i-1][h]>a) v[i][h]=a+1;
					v[i][j]=q+1;
				}
			}
			int res=*min_element (v[v.size()-1].begin(), v[v.size()-1].end());
			//for (int i=0; i<q; i++){for (int j=0; j<s; j++)cout<<v[i][j]<<" "; cout<<endl;}
			cout<<"Case #"<<cas<<": "<<res<<endl;
		}
		else cout<<"Case #"<<cas<<": "<<0<<endl;
	}
}
  
  