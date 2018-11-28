#include<set>
#include<map>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
#include<queue>
using namespace std;


int walk(int now, int wnext, int wtime)
{
	if(wtime>=abs(now - wnext)){
		return wnext;
	}
	if(wnext>now) return now+wtime;
	else return now - wtime;
}


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outl.txt","w",stdout);
    
	int m;
	int n;
	
	vector<pair<int,int>> orange;
	vector<pair<int,int>> blue;

	int o,b,t;
	char typ;
	int num;
	cin >> m;
	for(int i = 0; i!= m; i++){
		cin >> n;
		orange.clear();
		blue.clear();
		for(int j = 0; j != n; j++){
			cin >> typ >> num;
			if(typ == 'O')
			{
				orange.push_back(make_pair<int,int>(j,num));
			}
			else {
				blue.push_back(make_pair<int,int>(j,num));
			}
		}
		orange.push_back(make_pair<int,int>(1000,num));
		blue.push_back(make_pair<int,int>(1000,num));

		o=0;b=0;t=0;
		int o1,b1,t1;
		o1=1;b1=1;
		int osize = orange.size();
		int bsize = blue.size();
		for(int j = 0; j != n; j++)
		{
			if(orange[o].first < blue[b].first )
			{
				t1 = abs(orange[o].second - o1)+1;
				t += t1;
				o1=orange[o].second;
				b1=walk(b1,blue[b].second,t1);
				if(osize-1 != o)o++;				
			}
			else{
				t1 =abs(blue[b].second - b1)+1;
				t += t1;
				b1=blue[b].second;
				o1=walk(o1,orange[o].second,t1);
				if(bsize-1 != b)b++;
				
			}
		}
		cout << "Case #" << i+1 << ": " <<  t << endl;	
	}
}