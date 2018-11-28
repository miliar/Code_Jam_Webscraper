#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<hash_map>
using namespace std;
using namespace stdext;

bool check(vector<int> in)
{
	int size = in.size();
	bool ret = true;
	for(int i=0;i<size;i++) {
		if ( in[i] > i )
			return false;
	}
	return true;
}

class node
{
public:
	vector<int> m;
	int level;
};

int main()
{
	int test;
	cin >> test;
	for(int t=0;t<test;t++) {
		int n;
		cin >> n;
		vector<int> matrix(n,0);

		for(int i=0;i<n;i++) {
			int last = -1;
			for(int j=0;j<n;j++) {
				char input;
				cin >> input;
				if ( input == '1' )
					last = j;
			}
			matrix[i] = last;
		}

		queue< node > q;
		node mynode;
		mynode.m = matrix;
		mynode.level = 0;
		q.push(mynode);

		hash_map<string, bool> hmap;
		typedef pair<string,bool> pr;
		string str = "";
		for(int i=0;i<n;i++) {
			char temp[10] ;
			sprintf(temp,"%d|",matrix[i]);
			str+=temp;
		}
		hmap.insert(pr(str,true));

		bool fin = false;
		if ( check(matrix)) {
			fin = true;
			cout << "Case #" << t+1 <<": 0"<<endl;;
		}

		while(!q.empty() && !fin)
		{
			node old = q.front();
			q.pop();
			for(int i = 0;i<n-1 && !fin ;i++) {
				node newnode = old;
				swap(newnode.m[i], newnode.m[i+1]);
				if ( check(newnode.m) ) {
					fin = true;
					cout << "Case #" << t+1 << ": " <<newnode.level+1 << endl;;
				}
				newnode.level++;

				string ss;
				for(int i=0;i<n;i++) {
					char temp[10] ;
					sprintf(temp,"%d|",newnode.m[i]);
					ss+=temp;
				}
				if (hmap.find(ss)==hmap.end()) {
					q.push(newnode);
					hmap.insert(pr(ss,true));
				}
			}
		}
	}
}