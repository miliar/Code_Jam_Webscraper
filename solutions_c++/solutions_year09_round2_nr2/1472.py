#include<iostream>
#include<vector>
#include<iterator>
#include<string>

using namespace std;

int main()
{
    int t;
    cin >> t;
    string n,m,b;
    
    for(int p = 1;p<=t;p++)
    {
            cin >> n;
            b=n;
            sort(b.rbegin(),b.rend());
            if(equal(b.begin(),b.end(),n.begin()))
            {
                n.insert(0,"0");
            }
       //     copy(n.begin(),n.end(),ostream_iterator<char>(cout,""));
            m=n;
            sort(n.begin(),n.end());
            cout << "Case #" << p << ": ";
            do
            {
		     if(equal(m.begin(),m.end(),n.begin()))
             {  
              next_permutation(n.begin(),n.end());
              copy(n.begin(),n.end(),ostream_iterator<char>(cout,""));
              } 
	        }
	        while(next_permutation(n.begin(),n.end()));
	        
            if(p!=t)cout << endl;
	        m.clear();
    }    
    return 0;
}
