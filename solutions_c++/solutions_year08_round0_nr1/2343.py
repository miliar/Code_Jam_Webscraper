#include <iostream>
#include <string>
#include <map>
#include <sstream>
using namespace std;

int main()
{
	int N;
	cin >> N >>ws;
	//cout << "N: " << N <<endl;
	for(int t = 0; t < N;t++)
	{
		//cout << "-----------" <<t <<"--------------"<<endl;
		int S;
		cin >>ws;
		string s;
		getline(cin, s);
		//cout <<"s: " << s << endl;
		 stringstream ss (stringstream::in | stringstream::out);
		ss <<s;
		ss >> S;
		string engine [100];
		map<string, int> en_map; 
		for(int a = 0; a < S;a++)
		{
			getline(cin, engine[a]);
			//cout << "read: "  << engine [a] << endl;
			cin>>ws;
			en_map[engine[a]] = a;
		}
		int Q;
		string s2;
		getline(cin, s2);
		//cout << "s2: " << s2 <<endl;
		stringstream ss2 (stringstream::in | stringstream::out);
		ss2 << s2;
		ss2 >> Q;
		cin >> ws;
		//for(int a = 0; a < S;a++)
			//cout << engine[a] << endl;
		
		bool occur [100];
		int num_swtch = 0;
		if(Q > 0)
		{
		int num_occur = 0;
		memset(occur, 0,S*sizeof(occur[0]));
		string q;
		getline(cin,q);
		cin >>ws;
		
		//cout << "S: " <<S << endl;
		//cout << "Q: " << Q <<endl;
		for(int a = 0; a < Q;a++)
		{
			
			int ind = en_map[q];
			//cout << q << " " <<ind << " " << num_occur <<endl;

			if(!occur[ind])
			{
				occur[ind] = true;
				num_occur++;
			}
			if(num_occur == S)
			{
				num_swtch++;
				num_occur = 0;
				memset(occur, 0,S*sizeof(occur[0]));
				a--;
			}
			else if(a < Q-1)
			{
				getline(cin, q);
				//cout << "loop: " << q;
				cin >>ws;
			}
			
		}
		}
		cout << "Case #" << (t+1) << ": " << num_swtch << endl;
		
	}
	return 0;
}
