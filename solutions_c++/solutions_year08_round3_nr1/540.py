#include<iostream>
#include<vector>
#include<cstdio>
#include<algorithm>
#include<string>
#include<map>
using namespace std;


int main()
{
    freopen("al.in.txt" , "r" , stdin);
	freopen("al.out.txt" , "w" , stdout);
    
	int caseNo;
	cin >> caseNo;
	
	for(int c=1; c<=caseNo; c++) {
        map<int, vector<int> > m;
        int p, k, l;
        cin >> p >> k >>l;
        
        vector<int> f(l,0);
        for(int i = 0; i < l; i++) {
            cin >> f[i];
        }
        
        sort(f.rbegin(),f.rend());
        
        long long r = 0;
        
        int idx = 0;
        for(int i = 0; i < f.size(); i++) {
            m[idx].push_back(f[i]);
            idx++;
            idx %= k;
        }
        
        for(int i = 0; i < k; i++) {
            vector<int> vv = m[i];
            //for(int j = 0; j < vv.size(); j++) cout <<"vv:"<< vv[j] <<" ";
            //cout<< endl;
            for(int j = 0; j < vv.size(); j++) {
                //cout <<"vv:"<< vv[j] << endl;
                r += vv[j]*(j+1);
            }
        }
            
            
        cout << "Case #" << c << ": " <<r<< endl;
    }
    
	//system("pause");
	return 0;
}
